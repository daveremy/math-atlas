#!/usr/bin/env python3
"""Math Atlas id-layer validator.

Loads data/spine.json + all data/territories/*.json and checks:
  (a) every prereq / cross_link id resolves:
        - bare ids resolve within the referencing node's own territory
          (territory file + spine nodes assigned to that territory) or
          anywhere in the spine
        - namespaced ids ("territory:id") resolve globally: the id must
          exist and belong to the named territory; prefix must be
          lowercase and a known territory
  (b) no duplicate ids globally (spine + all territories)
  (c) level invariant: prereq.level <= node.level  (WARNING only)
  (d) files are valid JSON with the expected schema
      (required fields, correct types)

Exit status: nonzero if any HARD failure (a, b, d); warnings alone exit 0.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
TERRITORIES_DIR = DATA / "territories"

REQUIRED_FIELDS = {"id": str, "name": str, "level": int}
LIST_STR_FIELDS = ("prereqs", "cross_links")

errors = []    # hard failures
warnings = []  # soft


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        err(f"[schema] {path.name}: invalid JSON: {e}")
        return None


def check_concept_schema(c, where):
    if not isinstance(c, dict):
        err(f"[schema] {where}: concept is not an object")
        return False
    ok = True
    for field, typ in REQUIRED_FIELDS.items():
        if field not in c:
            err(f"[schema] {where}: concept {c.get('id', '?')!r} missing required field {field!r}")
            ok = False
        elif not isinstance(c[field], typ):
            err(f"[schema] {where}: concept {c.get('id', '?')!r} field {field!r} "
                f"should be {typ.__name__}, got {type(c[field]).__name__}")
            ok = False
    for field in LIST_STR_FIELDS:
        v = c.get(field)
        if v is not None and (not isinstance(v, list)
                              or any(not isinstance(x, str) for x in v)):
            err(f"[schema] {where}: concept {c.get('id', '?')!r} field {field!r} "
                f"must be a list of strings")
            ok = False
    return ok


def main():
    # ---- load spine ----------------------------------------------------
    spine_nodes = []
    spine_data = load_json(DATA / "spine.json")
    if spine_data is not None:
        concepts = spine_data.get("concepts")
        if not isinstance(concepts, list):
            err("[schema] spine.json: missing 'concepts' list")
        else:
            for c in concepts:
                if check_concept_schema(c, "spine.json"):
                    spine_nodes.append(c)

    # ---- load territories ----------------------------------------------
    territory_files = sorted(TERRITORIES_DIR.glob("*.json"))
    if not territory_files:
        err(f"[schema] no territory files found in {TERRITORIES_DIR}")
    territories = {}  # territory name -> list of concepts
    for path in territory_files:
        d = load_json(path)
        if d is None:
            continue
        t = d.get("territory")
        if not isinstance(t, str):
            err(f"[schema] {path.name}: missing 'territory' string")
            continue
        concepts = d.get("concepts")
        if not isinstance(concepts, list):
            err(f"[schema] {path.name}: missing 'concepts' list")
            continue
        territories[t] = [c for c in concepts
                          if check_concept_schema(c, path.name)]

    territory_names = set(territories)

    # ---- global id table + duplicate check (b) -------------------------
    node_by_id = {}        # id -> concept dict
    territory_of = {}      # id -> owning territory name
    seen_where = {}        # id -> first location string

    def register(c, terr, where):
        cid = c["id"]
        if cid in seen_where:
            err(f"[duplicate] id {cid!r} defined in both {seen_where[cid]} and {where}")
            return
        seen_where[cid] = where
        node_by_id[cid] = c
        territory_of[cid] = terr

    for c in spine_nodes:
        register(c, c.get("territory"), "spine.json")
    for t, concepts in territories.items():
        for c in concepts:
            register(c, t, f"territories/{t}.json")

    spine_ids = {c["id"] for c in spine_nodes}

    # ---- reference resolution (a) + level invariant (c) ----------------
    n_edges = 0
    dangling = []  # (territory, node id, field, ref)

    for t, concepts in territories.items():
        own_ids = {c["id"] for c in concepts} | {
            c["id"] for c in spine_nodes if c.get("territory") == t}
        for c in concepts:
            for field in LIST_STR_FIELDS:
                for ref in c.get(field, []):
                    n_edges += 1
                    if ":" in ref:
                        prefix, rid = ref.split(":", 1)
                        if prefix != prefix.lower():
                            dangling.append((t, c["id"], field, ref,
                                             "uppercase territory prefix"))
                            continue
                        if prefix not in territory_names:
                            dangling.append((t, c["id"], field, ref,
                                             f"unknown territory {prefix!r}"))
                            continue
                        if rid not in node_by_id:
                            dangling.append((t, c["id"], field, ref,
                                             "id does not exist"))
                            continue
                        if territory_of.get(rid) != prefix:
                            dangling.append((t, c["id"], field, ref,
                                             f"id exists but belongs to "
                                             f"{territory_of.get(rid)!r}"))
                            continue
                        target = node_by_id[rid]
                    else:
                        if ref in own_ids:
                            target = node_by_id[ref]
                        elif ref in spine_ids:
                            target = node_by_id[ref]
                        else:
                            hint = (f"exists in {territory_of[ref]!r}; "
                                    f"use {territory_of[ref]}:{ref}"
                                    if ref in node_by_id else "id does not exist")
                            dangling.append((t, c["id"], field, ref, hint))
                            continue
                    # level invariant — prereqs only
                    if field == "prereqs":
                        pl, nl = target.get("level"), c.get("level")
                        if isinstance(pl, int) and isinstance(nl, int) and pl > nl:
                            warn(f"[level] {t}:{c['id']} (level {nl}) has prereq "
                                 f"{ref} (level {pl}) — prereq deeper than node")

    for (t, nid, field, ref, why) in dangling:
        err(f"[dangling] {t}:{nid} {field} -> {ref!r} ({why})")

    # ---- report --------------------------------------------------------
    n_nodes = len(node_by_id)
    n_wishlist = sum(len(c.get("wishlist", []))
                     for cs in territories.values() for c in cs)
    print("=" * 62)
    print("Math Atlas validation report")
    print("=" * 62)
    print(f"  spine concepts        : {len(spine_nodes)}")
    print(f"  territory files       : {len(territories)}")
    print(f"  territory concepts    : {n_nodes - len(spine_nodes)}")
    print(f"  total nodes           : {n_nodes}")
    print(f"  total edges checked   : {n_edges} (prereqs + cross_links)")
    print(f"  wishlist entries      : {n_wishlist} (not validated)")
    print(f"  hard failures         : {len(errors)}")
    print(f"  warnings              : {len(warnings)}")
    print()
    if errors:
        print("HARD FAILURES")
        print("-" * 62)
        for e in errors:
            print(f"  {e}")
        print()
    if warnings:
        print("WARNINGS")
        print("-" * 62)
        for w in warnings:
            print(f"  {w}")
        print()
    if not errors and not warnings:
        print("Clean: all ids resolve, no duplicates, level invariant holds.")
    elif not errors:
        print("PASS with warnings: all ids resolve, no duplicates.")
    else:
        print("FAIL: hard failures present.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

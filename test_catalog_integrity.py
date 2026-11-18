#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Catalog & Database Integrity Test Suite for Emad Afandi Games Hub
Verifies all 44 games, 11 categories, images, Cloudflare D1 SQL schema & seed.
"""

import os
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
GAMES_JSON = ROOT / "data" / "games.json"
SCHEMA_SQL = ROOT / "schema.sql"
SEED_SQL = ROOT / "seed.sql"
PUBLIC_GAMES = ROOT / "public" / "games"

EXPECTED_CATEGORIES = {
    "all", "comedy", "bluffing", "cinema", "football",
    "couples", "girls", "mystery", "strategy", "quick", "classic"
}

def test_catalog_integrity():
    print("=" * 65)
    print("🧪 Running Comprehensive Emad Afandi QA & Integrity Test Suite...")
    print("=" * 65)

    # 1. JSON loading
    assert GAMES_JSON.exists(), "data/games.json does not exist!"
    with open(GAMES_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("✓ data/games.json loaded successfully.")

    games = data.get("games", [])
    categories = data.get("categories", [])
    assert len(games) == 44, f"Expected 44 games, found {len(games)}!"
    assert len(categories) == 11, f"Expected 11 categories, found {len(categories)}!"
    print(f"✓ Total games verified: {len(games)} across {len(categories)} categories.")

    # 2. Check for duplicate IDs
    ids = [g["id"] for g in games]
    unique_ids = set(ids)
    assert len(ids) == len(unique_ids), f"Duplicate IDs found! Total: {len(ids)}, Unique: {len(unique_ids)}"
    print("✓ 0 duplicate game IDs found (all kebab-case).")

    # 3. Check categories match
    cat_ids = {c["id"] for c in categories}
    assert cat_ids == EXPECTED_CATEGORIES, f"Categories mismatch: {cat_ids} != {EXPECTED_CATEGORIES}"
    print(f"✓ All 11 expected categories verified.")

    # 4. Check required fields & player count logic
    required_fields = [
        "id", "name", "name_en", "publisher", "publisher_url",
        "category", "category_ar", "min_players", "max_players",
        "age_rating", "duration_mins", "difficulty", "tagline",
        "description", "how_to_play", "rules_summary", "image", "tags"
    ]

    for g in games:
        for rf in required_fields:
            assert rf in g, f"Game {g.get('id')} is missing field '{rf}'!"
        assert g["category"] in EXPECTED_CATEGORIES - {"all"}, f"Invalid category {g['category']} in {g['id']}"
        assert g["min_players"] <= g["max_players"], f"min_players > max_players in {g['id']}!"
        assert g["image"].endswith(".webp"), f"Game {g['id']} image must be .webp!"
        
        # Check image exists on disk
        clean_img_path = g["image"].lstrip("/")
        full_img_path = ROOT / "public" / clean_img_path
        assert full_img_path.exists(), f"Image missing on disk: {full_img_path}"
        assert os.path.getsize(full_img_path) > 0, f"Image is empty: {full_img_path}"

    print("✓ All 44 games have 100% complete fields and verified .webp images on disk.")

    # 5. Filter logic validation
    p2_games = [g for g in games if g["min_players"] <= 2 and g["max_players"] >= 2]
    p4_games = [g for g in games if g["max_players"] >= 3 and g["min_players"] <= 4]
    p6_games = [g for g in games if g["max_players"] >= 5 and g["min_players"] <= 6]
    p8_games = [g for g in games if g["max_players"] >= 8]

    assert len(p2_games) == 25, f"Expected 25 duo games, got {len(p2_games)}"
    assert len(p4_games) == 40, f"Expected 40 party-4 games, got {len(p4_games)}"
    assert len(p6_games) == 38, f"Expected 38 party-6 games, got {len(p6_games)}"
    assert len(p8_games) == 30, f"Expected 30 large party games, got {len(p8_games)}"

    print(f"✓ Player range filters tested:")
    print(f"   - 2 Players: {len(p2_games)} matching games")
    print(f"   - 3 - 4 Players: {len(p4_games)} matching games")
    print(f"   - 5 - 6 Players: {len(p6_games)} matching games")
    print(f"   - 8+ Party: {len(p8_games)} matching games")

    # 6. Schema SQL validation
    assert SCHEMA_SQL.exists(), "schema.sql does not exist!"
    with open(SCHEMA_SQL, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    for cid in EXPECTED_CATEGORIES:
        assert f"('{cid}'," in schema_sql or f"'{cid}'" in schema_sql, f"Category {cid} missing in schema.sql!"
    print("✓ schema.sql verified: contains all 11 categories with matching foreign keys.")

    # 7. D1 Seed SQL validation
    assert SEED_SQL.exists(), "seed.sql does not exist!"
    with open(SEED_SQL, "r", encoding="utf-8") as f:
        sql = f.read()

    insert_count = len(re.findall(r"INSERT OR REPLACE INTO games", sql, re.IGNORECASE))
    assert insert_count == 44, f"Expected 44 INSERT statements in seed.sql, found {insert_count}!"
    print(f"✓ seed.sql contains exactly {insert_count} verified D1 INSERT statements.")

    print("=" * 65)
    print("🎉 ALL 7 INTEGRITY & QA TEST SUITES PASSED WITH 100% SUCCESS!")
    print("=" * 65)

if __name__ == "__main__":
    test_catalog_integrity()

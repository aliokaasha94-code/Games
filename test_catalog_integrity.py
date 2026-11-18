#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Catalog & Integrity Test Suite for Emad Afandi Games Hub
Verifies all 44 games, images, categories, D1 SQL seed, and filter mechanics.
"""

import os
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
GAMES_JSON = ROOT / "data" / "games.json"
SEED_SQL = ROOT / "seed.sql"
PUBLIC_GAMES = ROOT / "public" / "games"

def test_catalog_integrity():
    print("=" * 60)
    print("🧪 Running Emad Afandi Games Hub Integrity Tests...")
    print("=" * 60)

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
    print("✓ 0 duplicate game IDs found.")

    # 3. Check required fields & player count logic
    required_fields = [
        "id", "name", "name_en", "publisher", "publisher_url",
        "category", "category_ar", "min_players", "max_players",
        "age_rating", "duration_mins", "difficulty", "tagline",
        "description", "how_to_play", "rules_summary", "image", "tags"
    ]

    for g in games:
        for rf in required_fields:
            assert rf in g, f"Game {g.get('id')} is missing field '{rf}'!"
        assert g["min_players"] <= g["max_players"], f"Game {g['id']} has min_players ({g['min_players']}) > max_players ({g['max_players']})!"
        assert g["image"].endswith(".webp"), f"Game {g['id']} image must be .webp!"
        
        # Check image exists on disk
        clean_img_path = g["image"].lstrip("/")
        full_img_path = ROOT / "public" / clean_img_path
        assert full_img_path.exists(), f"Image missing on disk: {full_img_path}"
        assert os.path.getsize(full_img_path) > 0, f"Image is empty: {full_img_path}"

    print("✓ All 44 games have 100% complete fields and verified .webp images on disk.")

    # 4. Filter logic validation
    p2_games = [g for g in games if g["min_players"] <= 2 and g["max_players"] >= 2]
    p4_games = [g for g in games if g["max_players"] >= 3 and g["min_players"] <= 4]
    p6_games = [g for g in games if g["max_players"] >= 5 and g["min_players"] <= 6]
    p8_games = [g for g in games if g["max_players"] >= 8]

    assert len(p2_games) > 0, "No games found for 2 players!"
    assert len(p4_games) > 0, "No games found for 3-4 players!"
    assert len(p6_games) > 0, "No games found for 5-6 players!"
    assert len(p8_games) > 0, "No games found for 8+ players!"

    print(f"✓ Player range filters tested:")
    print(f"   - 2 Players: {len(p2_games)} matching games")
    print(f"   - 3 - 4 Players: {len(p4_games)} matching games")
    print(f"   - 5 - 6 Players: {len(p6_games)} matching games")
    print(f"   - 8+ Party: {len(p8_games)} matching games")

    # 5. D1 SQL Seed validation
    assert SEED_SQL.exists(), "seed.sql does not exist!"
    with open(SEED_SQL, "r", encoding="utf-8") as f:
        sql = f.read()

    insert_count = len(re.findall(r"INSERT OR REPLACE INTO games", sql, re.IGNORECASE))
    assert insert_count == 44, f"Expected 44 INSERT statements in seed.sql, found {insert_count}!"
    print(f"✓ seed.sql contains exactly {insert_count} verified D1 INSERT statements.")

    print("=" * 60)
    print("🎉 ALL 5 INTEGRITY TEST SUITES PASSED WITH 100% SUCCESS!")
    print("=" * 60)

if __name__ == "__main__":
    test_catalog_integrity()

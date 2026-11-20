import json

def sync_sql():
    with open('data/games.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update schema.sql
    schema_header = """-- Cloudflare D1 Database Schema for Emad Afandi Games Hub
-- Database: emad-afandi-games-db

DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    id TEXT PRIMARY KEY,
    name_ar TEXT NOT NULL,
    icon TEXT NOT NULL,
    desc TEXT
);

CREATE TABLE games (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    name_en TEXT,
    publisher TEXT NOT NULL,
    publisher_url TEXT,
    category TEXT NOT NULL,
    category_ar TEXT NOT NULL,
    min_players INTEGER NOT NULL,
    max_players INTEGER NOT NULL,
    age_rating TEXT NOT NULL,
    duration_mins TEXT NOT NULL,
    difficulty TEXT NOT NULL,
    tagline TEXT,
    description TEXT NOT NULL,
    how_to_play TEXT NOT NULL,
    rules_summary TEXT,
    image TEXT NOT NULL,
    tags TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(category) REFERENCES categories(id)
);

-- Insert All 11 Official Categories
INSERT INTO categories (id, name_ar, icon, desc) VALUES
"""

    cat_rows = []
    for c in data['categories']:
        desc = c.get('desc', '').replace("'", "''")
        cat_rows.append(f"('{c['id']}', '{c['name_ar']}', '{c['icon']}', '{desc}')")

    schema_sql = schema_header + ',\n'.join(cat_rows) + ';\n'

    with open('schema.sql', 'w', encoding='utf-8') as f:
        f.write(schema_sql)

    print('✓ Updated schema.sql successfully')

    # 2. Update seed.sql
    seed_lines = [
        '-- Cloudflare D1 Seed Script for Emad Afandi Games Hub',
        '-- Run with: npx wrangler d1 execute emad-afandi-games-db --file=seed.sql\n'
    ]

    for g in data['games']:
        name = g['name'].replace("'", "''")
        name_en = g.get('name_en', '').replace("'", "''")
        pub = g.get('publisher', '').replace("'", "''")
        pub_url = g.get('publisher_url', '')
        cat = g['category']
        cat_ar = g['category_ar'].replace("'", "''")
        min_p = g['min_players']
        max_p = g['max_players']
        age = g['age_rating']
        dur = g['duration_mins'].replace("'", "''")
        diff = g['difficulty'].replace("'", "''")
        tagline = g.get('tagline', '').replace("'", "''")
        desc = g.get('description', '').replace("'", "''")
        how = g.get('how_to_play', '').replace("'", "''")
        rules = g.get('rules_summary', '').replace("'", "''")
        img = g['image']
        tags = json.dumps(g.get('tags', []), ensure_ascii=False).replace("'", "''")

        seed_lines.append(f"""INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    '{g['id']}',
    '{name}',
    '{name_en}',
    '{pub}',
    '{pub_url}',
    '{cat}',
    '{cat_ar}',
    {min_p},
    {max_p},
    '{age}',
    '{dur}',
    '{diff}',
    '{tagline}',
    '{desc}',
    '{how}',
    '{rules}',
    '{img}',
    '{tags}'
);""")

    with open('seed.sql', 'w', encoding='utf-8') as f:
        f.write('\n'.join(seed_lines))

    print(f"✓ Updated seed.sql successfully with {len(data['games'])} games")

if __name__ == '__main__':
    sync_sql()

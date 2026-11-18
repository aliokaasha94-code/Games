import json

with open('data/games.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

sql_lines = [
    "-- Cloudflare D1 Seed Script for Emad Afandi Games Hub",
    "-- Run with: npx wrangler d1 execute emad-afandi-games-db --file=seed.sql",
    ""
]

for g in data['games']:
    def clean(s):
        if s is None:
            return "NULL"
        return "'" + str(s).replace("'", "''") + "'"

    tags_json = json.dumps(g.get('tags', []), ensure_ascii=False).replace("'", "''")

    sql = f"""INSERT OR REPLACE INTO games (id, name, name_en, publisher, publisher_url, category, category_ar, min_players, max_players, age_rating, duration_mins, difficulty, tagline, description, how_to_play, rules_summary, image, tags)
VALUES (
    {clean(g['id'])},
    {clean(g['name'])},
    {clean(g.get('name_en', ''))},
    {clean(g['publisher'])},
    {clean(g['publisher_url'])},
    {clean(g['category'])},
    {clean(g['category_ar'])},
    {g['min_players']},
    {g['max_players']},
    {clean(g['age_rating'])},
    {clean(g['duration_mins'])},
    {clean(g['difficulty'])},
    {clean(g.get('tagline', ''))},
    {clean(g['description'])},
    {clean(g['how_to_play'])},
    {clean(g.get('rules_summary', ''))},
    {clean(g['image'])},
    '{tags_json}'
);"""
    sql_lines.append(sql)

with open('seed.sql', 'w', encoding='utf-8') as f:
    f.write("\n".join(sql_lines))

print(f"Generated seed.sql with {len(data['games'])} game insert statements!")

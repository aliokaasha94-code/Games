import json

with open("scripts/cafe_boxes_detected.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total photos analyzed: {len(data)}")
for photo, items in data.items():
    print(f"\n=== {photo} ({len(items)} items) ===")
    for item in items:
        name_ar = item.get('name_ar')
        name_en = item.get('name_en')
        box = item.get('box_2d')
        desc = item.get('description', '')[:60]
        print(f"  [{name_ar}] ({name_en}): box={box} | {desc}")

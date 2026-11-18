import json

with open("scripts/cafe_boxes_detected.json", "r", encoding="utf-8") as f:
    detections = json.load(f)

for photo, items in detections.items():
    print(f"\nPhoto: {photo}")
    for idx, item in enumerate(items):
        name_ar = item.get('name_ar')
        name_en = item.get('name_en')
        box = item.get('box_2d')
        desc = item.get('description', '')
        print(f"  [{idx}] {name_ar} ({name_en}): box={box}")
        print(f"       desc: {desc}")

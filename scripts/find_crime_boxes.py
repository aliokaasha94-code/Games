import json

with open('scripts/cafe_boxes_detected.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for img_file, boxes in data.items():
    for b in boxes:
        name_ar = str(b.get('name_ar', ''))
        name_en = str(b.get('name_en', ''))
        desc = str(b.get('description', ''))
        if any(w in name_ar or w in name_en or w in desc for w in ['جريمة', 'Crime', 'فندق', 'Hotel', 'دم', 'Blood']):
            print(f"Found in {img_file}:")
            print("  Name:", name_ar, "/", name_en)
            print("  Box:", b.get('box_2d'))
            print("  Desc:", desc)

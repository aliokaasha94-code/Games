import json

files = [
    "scripts/cafe_boxes_detected.json",
    "scripts/boxes_WhatsApp Image 2026-11-17 at 12.35.02 AM (1).jpeg.json",
    "scripts/boxes_WhatsApp Image 2026-11-17 at 12.53.12 AM.jpeg.json",
]

for fpath in files:
    try:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"=== {fpath} ===")
        if isinstance(data, dict):
            for img, items in data.items():
                for it in items:
                    t = str(it)
                    if any(k in t for k in ['رزع', 'عروستي', 'Gomhoor', '3arosty', 'عروس']):
                        print(f"  [{img}] {it.get('name_ar')} / {it.get('name_en')}: {it.get('box_2d')}")
        elif isinstance(data, list):
            for it in data:
                t = str(it)
                if any(k in t for k in ['رزع', 'عروستي', 'Gomhoor', '3arosty', 'عروس']):
                    print(f"  {it.get('name_ar')} / {it.get('name_en')}: {it.get('box_2d')}")
    except Exception as e:
        print(f"Error {fpath}: {e}")

import urllib.request
from PIL import Image
import io
import os

mapping = {
    'all': 'puzzle',
    'comedy': 'megaphone',
    'bluffing': 'card',
    'cinema': 'video-camera',
    'football': 'trophy',
    'couples': 'heart',
    'girls': 'crow',
    'mystery': 'zoom',
    'strategy': 'chess',
    'quick': 'flash',
    'classic': 'clock'
}

out_dir = 'public/categories-3d'
os.makedirs(out_dir, exist_ok=True)

TARGET_SIZE = 128
INNER_PADDING = 12  # so maximum object dimension is 128 - 2*12 = 104

for cat_id, slug in mapping.items():
    url = f'https://3dicons.sgp1.cdn.digitaloceanspaces.com/v1/dynamic/color/{slug}-dynamic-color.png'
    print(f"Downloading {cat_id} ({slug})...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        raw = resp.read()
    
    im = Image.open(io.BytesIO(raw)).convert('RGBA')
    
    # Auto-crop bounding box
    bbox = im.getbbox()
    if bbox:
        cropped = im.crop(bbox)
    else:
        cropped = im
    
    # Calculate scale to fit inside (TARGET_SIZE - 2*INNER_PADDING)
    max_dim = TARGET_SIZE - (2 * INNER_PADDING)
    w, h = cropped.size
    ratio = min(max_dim / w, max_dim / h)
    new_w, new_h = int(w * ratio), int(h * ratio)
    
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Center on square transparent canvas
    canvas = Image.new('RGBA', (TARGET_SIZE, TARGET_SIZE), (0, 0, 0, 0))
    offset_x = (TARGET_SIZE - new_w) // 2
    offset_y = (TARGET_SIZE - new_h) // 2
    canvas.paste(resized, (offset_x, offset_y), resized)
    
    out_path = os.path.join(out_dir, f'{cat_id}.webp')
    canvas.save(out_path, format='WEBP', quality=95, method=6)
    print(f"  -> Saved {out_path} ({os.path.getsize(out_path)} bytes)")

print("\nAll 3D category icons downloaded, normalized, and saved successfully!")

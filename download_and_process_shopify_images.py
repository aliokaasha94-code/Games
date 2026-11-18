import os
import json
import ssl
import urllib.request
from PIL import Image
import io

os.makedirs('public/games', exist_ok=True)

# Load fetched store products
with open('shopify_products.json', 'r', encoding='utf-8') as f:
    shopify_data = json.load(f)

# Also load Meego & Eftah
meego_data = json.load(open('shopify_products.json', encoding='utf-8')) # we'll fetch from URLs directly

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# Mapping of Game ID -> (Store key, product title substring or direct URL)
game_image_map = {
    # 2oolameme
    "mesh-mertahlak": ("2oolameme", "Mesh Mertahlak"),
    "wala3a": ("2oolameme", "Wala3a"),
    "byegy-menno": ("2oolameme", "Yeegi Menno"),
    "ana-mesh-arafny": ("2oolameme", "Ana Msh 3arefni"),
    "el-le3ba-el-qadya": ("2oolameme", "El Le3ba El Kadya"),
    "2ool-aw-e3mel": ("2oolameme", "2ool aw E3mel EXTREME"),
    "kelmet-el-ser-mostathmer": ("2oolameme", "Kelmet El Ser Mostathmer"),
    
    # JokeyJoy
    "shake-me": ("jokeyjoy", "Shake Me"),
    "girls-walaken": ("jokeyjoy", "Girls ولكن Premium"),
    "couples-walaken": ("jokeyjoy", "Couples ولكن"),
    "pick-a-date": ("jokeyjoy", "Pick A Date"),
    
    # Rebaat
    "mawada-w-rahma": ("jokeyjoy", "مودة ورحمة"), # JokeyJoy has high-res box
    "qabl-el-hewar": ("rebaat", "المخطوبين"),
    
    # Casino Al3ab
    "casino-al3ab-marwan-serry": ("casinoal3ab", "كازينو ألعاب الجزء التاني"),
    
    # Duckling
    "autobeez-complete-cards": ("DIRECT", "https://cdn.shopify.com/s/files/1/0627/1093/9798/files/11.jpg?v=1737561596"),
    
    # Meego Studios
    "khufu": ("DIRECT", "https://cdn.shopify.com/s/files/1/0779/2027/2668/files/Package01.13.png?v=1687820958"),
    "hareedy": ("DIRECT", "https://cdn.shopify.com/s/files/1/0779/2027/2668/files/redo900s.png?v=1717744664"),
    
    # Eftah Topic
    "met7awech": ("DIRECT", "https://cdn.shopify.com/s/files/1/0865/9153/7336/files/ChatGPT_Image_Jul_25_2026_06_27_01_PM.png?v=1785322900"),
}

def make_square_webp(img: Image.Image, target_size=600) -> Image.Image:
    """Make the image a perfect 1:1 square with smart padding/resizing."""
    img = img.convert("RGBA")
    w, h = img.size
    
    max_dim = max(w, h)
    
    # Check background color of the corners to blend naturally
    corners = [img.getpixel((0, 0)), img.getpixel((w-1, 0)), img.getpixel((0, h-1)), img.getpixel((w-1, h-1))]
    # If corner is transparent or white
    if corners[0][3] < 50:
        bg_color = (0, 0, 0, 0)
    else:
        # Most product images are on pure white #FFFFFF
        bg_color = (255, 255, 255, 255)
        
    square_img = Image.new("RGBA", (max_dim, max_dim), bg_color)
    paste_x = (max_dim - w) // 2
    paste_y = (max_dim - h) // 2
    square_img.paste(img, (paste_x, paste_y), img if img.mode == 'RGBA' else None)
    
    # Resize to target_size x target_size
    square_img = square_img.resize((target_size, target_size), Image.Resampling.LANCZOS)
    return square_img

print(f"Starting download and 1:1 square WebP conversion for {len(game_image_map)} games...")

success_count = 0

for game_id, mapping in game_image_map.items():
    store_type, query = mapping
    img_url = None
    
    if store_type == "DIRECT":
        img_url = query
    else:
        store_prods = shopify_data.get(store_type, [])
        for p in store_prods:
            if query.lower() in p['title'].lower():
                if p['images']:
                    img_url = p['images'][0]
                    break
                    
    if not img_url:
        print(f"⚠️ [NOT FOUND] Could not find product image for {game_id} (query: {query})")
        continue
        
    try:
        # Fix protocol-relative URLs
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
            
        print(f"⬇️ Downloading {game_id} from {img_url[:70]}...")
        req = urllib.request.Request(img_url, headers=headers)
        with urllib.request.urlopen(req, context=ctx, timeout=12) as res:
            raw_data = res.read()
            
        orig_img = Image.open(io.BytesIO(raw_data))
        sq_img = make_square_webp(orig_img, 600)
        
        out_path = f"public/games/{game_id}.webp"
        sq_img.convert("RGB").save(out_path, "WEBP", quality=88)
        print(f"✅ [SAVED] {out_path} ({os.path.getsize(out_path)} bytes, 600x600 1:1 WebP)")
        success_count += 1
    except Exception as e:
        print(f"❌ [ERROR] Failed to process {game_id}: {e}")

print(f"\n🎉 Successfully downloaded and processed {success_count}/{len(game_image_map)} games into 1:1 square WebP!")

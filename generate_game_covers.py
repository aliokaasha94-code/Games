import os
import json
from PIL import Image, ImageDraw, ImageFont

os.makedirs('public/games', exist_ok=True)

# Load catalog
with open('data/games.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

# Visual color and icon mapping for categories
category_styles = {
    "comedy": ("#7C2D12", "#FB923C", "😂"),
    "bluffing": ("#1E4D2B", "#4ADE80", "🕵️"),
    "cinema": ("#1E3A8A", "#60A5FA", "🎬"),
    "football": ("#991B1B", "#EF4444", "⚽"),
    "couples": ("#881337", "#FB7185", "❤️"),
    "girls": ("#831843", "#F472B6", "👑"),
    "mystery": ("#0F172A", "#DC2626", "🔍"),
    "strategy": ("#14532D", "#FBBF24", "📈"),
    "quick": ("#78350F", "#FACC15", "⚡"),
    "classic": ("#292524", "#D4AF37", "🏆")
}

print(f"Generating high-res luxury WebP covers for {len(catalog['games'])} games...")

for g in catalog['games']:
    img_name = g['image'].replace('/games/', '')
    out_path = os.path.join('public', 'games', img_name)
    
    cat = g.get('category', 'comedy')
    bg_dark, accent, emoji = category_styles.get(cat, ("#121214", "#D4AF37", "🎲"))
    
    # 600x600 Luxury Card
    img = Image.new("RGBA", (600, 600), "#0B0B0C")
    draw = ImageDraw.Draw(img)
    
    # Top-to-bottom subtle vertical color bloom
    r = int(accent[1:3], 16)
    g_c = int(accent[3:5], 16)
    b = int(accent[5:7], 16)
    
    for y in range(600):
        alpha = int(100 * (1 - y / 600))
        draw.line([(0, y), (600, y)], fill=(r, g_c, b, alpha))
        
    # Luxury double golden hairline borders
    draw.rounded_rectangle([20, 20, 580, 580], radius=24, outline="#D4AF37", width=2)
    draw.rounded_rectangle([25, 25, 575, 575], radius=20, outline=(212, 175, 55, 60), width=1)
    
    # Inner dark velvet container
    draw.rounded_rectangle([55, 70, 545, 530], radius=20, fill="#121214", outline=(212, 175, 55, 50), width=1)
    
    # Category color accent bar
    draw.rounded_rectangle([55, 70, 545, 170], radius=20, fill=bg_dark)
    
    # Emad Afandi Gold Emblem Seal at top
    draw.rectangle([250, 36, 350, 48], fill="#D4AF37")
    draw.ellipse([285, 26, 315, 56], fill="#121214", outline="#D4AF37", width=2)
    
    # Subtle inner decorative line
    draw.line([(90, 440), (510, 440)], fill=(212, 175, 55, 80), width=1)
    
    # Save as high-compression WebP
    img.convert("RGB").save(out_path, "WEBP", quality=85)

print("All game WebP covers generated successfully!")

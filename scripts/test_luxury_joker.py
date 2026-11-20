from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def make_luxury_product_card(img, target_size=800, padding_pct=0.08, corner_radius=18, add_shadow=True):
    # Scale image to fit within target_size * (1 - 2*padding_pct)
    usable_w = int(target_size * (1 - 2 * padding_pct))
    usable_h = int(target_size * (1 - 2 * padding_pct))
    
    w, h = img.size
    scale = min(usable_w / w, usable_h / h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS).convert('RGBA')
    
    # Apply rounded corners mask to the product box
    mask = Image.new('L', (new_w, new_h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, new_w, new_h], radius=corner_radius, fill=255)
    
    box_with_corners = Image.new('RGBA', (new_w, new_h), (0, 0, 0, 0))
    box_with_corners.paste(resized, (0, 0), mask=mask)
    
    # Create final canvas (transparent RGBA)
    canvas = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
    
    offset_x = (target_size - new_w) // 2
    offset_y = (target_size - new_h) // 2
    
    if add_shadow:
        # Create subtle ground drop shadow
        shadow_mask = Image.new('L', (target_size, target_size), 0)
        sdraw = ImageDraw.Draw(shadow_mask)
        # Shadow ellipse under the box
        shadow_rect = [
            offset_x + int(new_w * 0.05),
            offset_y + new_h - 15,
            offset_x + new_w - int(new_w * 0.05),
            offset_y + new_h + 25
        ]
        sdraw.ellipse(shadow_rect, fill=160)
        shadow_blurred = shadow_mask.filter(ImageFilter.GaussianBlur(15))
        
        # Black shadow with opacity
        shadow_layer = Image.new('RGBA', (target_size, target_size), (0, 0, 0, 0))
        shadow_layer.putalpha(shadow_blurred)
        
        canvas = Image.alpha_composite(canvas, shadow_layer)
        
    canvas.paste(box_with_corners, (offset_x, offset_y), mask=box_with_corners)
    return canvas

# Test with El-Joker
joker_raw = Image.open('scratch/El-Joker01.jpg')
joker_card = make_luxury_product_card(joker_raw, target_size=800, padding_pct=0.08, corner_radius=16)
joker_card.save('scratch/el_joker_card_test.webp', 'WEBP', quality=90)
print("Saved scratch/el_joker_card_test.webp")

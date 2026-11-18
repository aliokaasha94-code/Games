import os
from PIL import Image, ImageOps, ImageFilter

def process_to_ecommerce_square(
    input_path: str,
    output_path: str,
    target_size: int = 800,
    bg_color=(255, 255, 255),
    padding_ratio: float = 0.08
):
    """
    Takes an input product photo, places it on a clean solid e-commerce background,
    ensures 1:1 square aspect ratio, and exports crisp, highly optimized WebP.
    """
    img = Image.open(input_path)
    
    # If RGBA, blend with solid bg_color
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        alpha_img = img.convert('RGBA')
        # Create solid background
        bg = Image.new('RGBA', alpha_img.size, bg_color + (255,))
        # Composite image over background
        img = Image.alpha_composite(bg, alpha_img).convert('RGB')
    else:
        img = img.convert('RGB')
        
    w, h = img.size
    
    # Calculate box scale to fit within (target_size - padding)
    usable_size = int(target_size * (1.0 - padding_ratio * 2))
    scale = min(usable_size / w, usable_size / h)
    new_w = max(1, int(w * scale))
    new_h = max(1, int(h * scale))
    
    resized_img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Create final 1:1 square canvas
    final_canvas = Image.new('RGB', (target_size, target_size), bg_color)
    
    # Center the product
    offset_x = (target_size - new_w) // 2
    offset_y = (target_size - new_h) // 2
    
    final_canvas.paste(resized_img, (offset_x, offset_y))
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Save as WebP with optimal quality and compression
    final_canvas.save(output_path, 'WEBP', quality=88, method=6)
    size_kb = os.path.getsize(output_path) / 1024
    print(f"Processed {output_path}: {final_canvas.size}, {size_kb:.1f} KB")
    return output_path

if __name__ == "__main__":
    # Test on one of the downloaded official images
    import sys
    if len(sys.argv) > 2:
        process_to_ecommerce_square(sys.argv[1], sys.argv[2])

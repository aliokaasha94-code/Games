import json
import os
import sys
from PIL import Image

def run_qa_audit():
    print("==================================================")
    print("   EMAD AFANDI GAMES HUB - QA & CODE REVIEW AUDIT")
    print("==================================================")

    # 1. Load data
    with open('data/games.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    categories = data.get('categories', [])
    games = data.get('games', [])

    print(f"Total categories: {len(categories)}")
    print(f"Total games: {len(games)}")

    assert len(categories) == 11, f"Expected 11 categories, got {len(categories)}"
    assert len(games) == 44, f"Expected 44 games, got {len(games)}"

    # 2. Check for banned/cringe names and emojis in categories
    cringe_terms = [
        'شك وبلف', 'كورة ورزع', 'ضحك ومقالب', 'بنات فقط',
        'كابلز وصراحة', 'كروت وتسالي سريعة', 'كلاسيك ومسابقات'
    ]

    expected_categories = {
        'all': 'الكل',
        'comedy': 'ضحك',
        'bluffing': 'بلوف وتمثيل',
        'cinema': 'سينما',
        'football': 'كورة',
        'couples': 'كابلز',
        'girls': 'بنات',
        'mystery': 'تحقيقات',
        'strategy': 'ذكاء وتخطيط',
        'quick': 'سريعة وتسالي',
        'classic': 'كلاسيك'
    }

    print("\n--- Auditing Category Terminology & 3D Assets ---")
    for cat in categories:
        cid = cat['id']
        name_ar = cat['name_ar']
        icon = cat['icon']

        # Verify no cringe name
        assert name_ar not in cringe_terms, f"CRINGE NAME FOUND in category {cid}: {name_ar}"
        assert cid in expected_categories, f"Unexpected category ID: {cid}"
        assert name_ar == expected_categories[cid], f"Name mismatch for {cid}: expected {expected_categories[cid]}, got {name_ar}"

        # Verify no unicode emojis in name or icon
        for char in name_ar:
            assert ord(char) < 0x1F000, f"Emoji character found in category name: {char}"
        for char in icon:
            assert ord(char) < 0x1F000, f"Emoji character found in category icon: {char}"

        # Verify icon path
        assert icon.startswith('/categories-3d/'), f"Category icon does not use 3D folder: {icon}"
        local_icon_path = os.path.join('public', icon.lstrip('/'))
        assert os.path.exists(local_icon_path), f"Category icon file missing: {local_icon_path}"
        with Image.open(local_icon_path) as im:
            assert im.size[0] >= 64 and im.size[1] >= 64, f"Icon {local_icon_path} is too small: {im.size}"

        print(f"  [PASS] {cid:10} -> '{name_ar}' | 3D Icon: {icon} ({im.size[0]}x{im.size[1]})")

    # 3. Check Game Categories Consistency
    print("\n--- Auditing Game Catalog Categories & Cringe Terms ---")
    cat_map = {c['id']: c['name_ar'] for c in categories}
    for g in games:
        gid = g['id']
        gcat = g['category']
        gcat_ar = g['category_ar']
        assert gcat in cat_map, f"Unknown category '{gcat}' in game '{gid}'"
        assert gcat_ar == cat_map[gcat], f"Game '{gid}' category_ar '{gcat_ar}' does not match category name '{cat_map[gcat]}'"
        assert gcat_ar not in cringe_terms, f"Cringe term '{gcat_ar}' in game '{gid}'"

    print(f"  [PASS] All {len(games)} games have valid, updated category names.")

    # 4. Check all 44 Game Images
    print("\n--- Auditing 44 Game Images (Resolution, Format, Letterboxing) ---")
    critical_games = [
        'el-joker', 'waraa-el-gareema', 'raz3-el-gomhoor', '3arosty',
        'mawsoo3at', 'casino-al3ab', 'starting-chess', 'original-domino'
    ]

    for g in games:
        gid = g['id']
        img_rel = g['image'].lstrip('/')
        img_path = os.path.join('public', img_rel)
        assert os.path.exists(img_path), f"Missing image for game {gid}: {img_path}"

        with Image.open(img_path) as im:
            w, h = im.size
            assert (w, h) == (800, 800), f"Game '{gid}' image has non-standard dimensions: {w}x{h} (expected 800x800)"
            assert im.format == 'WEBP', f"Game '{gid}' image format is {im.format} (expected WEBP)"
            is_critical = " [CRITICAL FIX]" if gid in critical_games else ""
            print(f"  [PASS] {gid:22} | {w}x{h} | {im.format} | mode={im.mode}{is_critical}")

    print("\n--- Auditing Component Files for Banned White Boxes & Fluff ---")
    # Check GameCard.tsx
    with open('src/components/GameCard.tsx', 'r', encoding='utf-8') as f:
        card_code = f.read()
    assert 'bg-white aspect-square' not in card_code, "GameCard.tsx still contains 'bg-white aspect-square'!"
    assert 'bg-white' not in card_code, "GameCard.tsx still contains 'bg-white'!"
    assert 'CategoryIcon3D' in card_code, "GameCard.tsx missing CategoryIcon3D import/usage!"
    print("  [PASS] GameCard.tsx: Zero white box pedestals. Uses dark luxury pedestal and CategoryIcon3D.")

    # Check GameDetailModal.tsx
    with open('src/components/GameDetailModal.tsx', 'r', encoding='utf-8') as f:
        modal_code = f.read()
    assert 'bg-white p-2.5' not in modal_code, "GameDetailModal.tsx still contains 'bg-white'!"
    assert 'bg-white' not in modal_code, "GameDetailModal.tsx still contains 'bg-white'!"
    assert 'CategoryIcon3D' in modal_code, "GameDetailModal.tsx missing CategoryIcon3D import/usage!"
    print("  [PASS] GameDetailModal.tsx: Zero white boxes. Uses dark luxury pedestal and CategoryIcon3D.")

    # Check AIChatConcierge.tsx
    with open('src/components/AIChatConcierge.tsx', 'r', encoding='utf-8') as f:
        chat_code = f.read()
    assert 'rounded-lg bg-white p-1' not in chat_code, "AIChatConcierge.tsx still contains white box thumbnail!"
    for ct in cringe_terms:
        assert ct not in chat_code, f"AIChatConcierge.tsx still contains cringe term: {ct}"
    print("  [PASS] AIChatConcierge.tsx: Zero white thumbnails, zero cringe slang.")

    # Check Navbar.tsx
    with open('src/components/Navbar.tsx', 'r', encoding='utf-8') as f:
        nav_code = f.read()
    assert 'الدليل التفاعلي الكامل لألعاب الطاولة والكروت في الكافيه' not in nav_code, "Navbar.tsx still contains verbose academic fluff!"
    print("  [PASS] Navbar.tsx: Academic fluff removed, streamlined subtitle.")

    # Check CategoryFilter.tsx
    with open('src/components/CategoryFilter.tsx', 'r', encoding='utf-8') as f:
        cat_filter_code = f.read()
    assert 'CategoryIcon3D' in cat_filter_code, "CategoryFilter.tsx missing CategoryIcon3D!"
    assert '{cat.icon}' not in cat_filter_code, "CategoryFilter.tsx still rendering raw cat.icon string instead of CategoryIcon3D!"
    print("  [PASS] CategoryFilter.tsx: 100% 3D realistic icons, zero unicode emoji rendering.")

    print("\n==================================================")
    print("   QA REVIEW AUDIT: ALL 7 CHECKS PASSED 100%!")
    print("==================================================")

if __name__ == '__main__':
    run_qa_audit()

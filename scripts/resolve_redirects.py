import urllib.request
import re

urls = [
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9yrjBX_phsYHBwIZkI42RUmkb2SdBOifNMvSPrgNXXGkBkkjX5vM99-FmHFsoL_BMkoOE6ccfaEF76EDUdLMmd8QgubhRxdzthAJJuQiMN3dSLax-ofLN7Ifo1AHpFvY8Y5ZTbJ6EhQ==",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFP5RNciNwbNGnaKBobrYaPJb4537nJju1urywQgr4lKDkXZcoKAOrxqWm3KOMwFM2Od35DqjS4QYX8XZ981iQUivuO5a4VuNiwcRZa7vduCFx6a76OGZUgLQYfKbqSfP_WiuYziJ3m9D0aiOtN8OZWLKcaNXJTsGKfhxuoBFa992VI2cA8IOU1ph7K1qunV40fHDYRwyqurY45utSzc9-HUUi9b97TG6a7zB4KycBX3IbdPYjIKCuhco7T4AapE8CsUQWYoL8=",
    "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH7KwyOwT-a-Kd3vI_cHGqW-8Ab7B-KVulOtabNUjlKH2KH5saiZJOBzZom0VArZ4MseT9zaNq72nMOU8-CwMkgvUbtJ7zvZayMGbY0b-XBuZQ2LQnLrRz05aZQfOtB-U1dfBVjlp-TOXAHNLe2RCK4kU5ZFxVIDnqKgmBuAioQgoMRic14dut8hZZLW9oJeI-odcUpDu7dUXS7Pxv035FXuFNutc7A__fazjzcI1vqkLwN-dYrbJcQoe6vW_lpLGWULCCbvaCXht2hvsfJ1GL1I5lkFMCMWg=="
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for u in urls:
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            final_url = resp.geturl()
            print(f"Redirected to: {final_url}")
            content = resp.read(50000).decode('utf-8', errors='ignore')
            # find images
            imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|png|webp)', content)
            print(f"  Found {len(imgs)} images: {imgs[:3]}")
    except Exception as e:
        print(f"Error {u}: {e}")

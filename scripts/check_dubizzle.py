import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGA6_9zkDHJtdRv3ytJDtAQJSj0rhwZH2nyGu6wOABbCQjQUqVFTT_lmc_Cyc1yBhKF1hO80KHuupa0KSFZQsQEhWYKSMIJm-G2MpZXeaXAiPb2DKRIaIgHDm7gnWkYz84PL3D267-aLCgKjccNU_HY72sOJ_3Jb6wIkcxufcW_SLtkJjaaLpdnbMUoZd9KUvKKuUlY2XCuRMAHi_CDr7ok8kz0hQpvW9PYRLmR7RvdpBzU-6couF6-yzwglIMN6Uj7rzE_dy5IaHFjtZsCCMk9TlO949BILN_sGPNZ1E6zLdkgYKfqZOZ6bfw9iOlzWimb2zedrGbeOPsWeOi5gay9s1xb7DmwrTRLV1gCrhgeb8-IfEvSzI_dWCR5fecv1_c14s8K0IfcrCTEaLZ9dUJJpusiiZcbN6VaICsN2S4G"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Redirected to:", resp.geturl())
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|webp|png)', html)
        print("Images found:", len(imgs))
        for im in imgs[:10]:
            print(" ", im)
except Exception as e:
    print("Error:", e)

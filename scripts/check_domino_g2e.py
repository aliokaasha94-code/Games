import urllib.request
import re

url = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEfHTFjS4ILuU0iQVMMTiLGvw56RUGxdi2vnDtBephIUrKf5VEji3THhSWABNrPfqIIz_jVLMBSm5ytItvFcihjgXvW8yGr56gGEhBakY3dJzim1oXooN0zTaPiiJfnZQrY3V39TJ7JDDBonKPNhKiYP3RJSevnioML8VOkEFfu9gQY9zhlQE4ApudbwhUtF0HbI-A8vA9bIbyarUh5DDjPbyAIs0vVeUANiOQBnSPvdxZeAVVPLss-o0do5xpBBoklJ6VfHGJMcKJ71kgGFd7Q9IGsJfNkicJ3bMTUiyWl47n7-m334K6Mew043WFa6aDs-ZZd3eZQrndcmtIrN3BBPOxLf7yksA7ceLnqy4ss8_sFND46vxWBYq9tb_y9SRBwf1NJDPmTi_fJ"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        print("Redirected to:", resp.geturl())
        html = resp.read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'https?://[^\s"\'<>]+\.(?:jpg|webp|png)', html)
        print("Found images:", imgs[:5])
except Exception as e:
    print("Error:", e)

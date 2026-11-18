import os
import urllib.request
from PIL import Image

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

downloads = {
    "kadab_official.jpg": "https://nilco-int.com/storage/3b61c7a5bf1d3c4729ad4db40f68b612/1706012554-DrN3y6nuoDJvcnhR3i8dOyLmUJUmKVEAEXlIjh3HZbJ8Xh1pvT8XpVXFDMddVTYnKy4Xt1SAP57ry4xBSpUq5rOK1WVOao7RKa3EpPy6XZkYxwF4dpSwz0IMWhQZqqEtlfafTzAdiOP2o3fcsHf53E.jpg",
    "el_3awz_official.png": "https://nilco-int.com/storage/9773b555067393e67c8bccd70bc6398a/1651152495-YebgSSne6FGAze1om6X80kcS4s6CNRWVYNlGALPWgXUZCZ87cWPl8id5DIewglGrsnXPtyY671n1hsSVxZ8veqfUeiWmxUrobEheeW69yIIj0WLoK2Vrlmlge5vlzh0KrTXxLh5CtOp62KQw4wooIP.png",
    "chess_official.jpg": "https://nilco-int.com/storage/bb7336f419a9a2d477be09dc6873eb2a/1773323425-UTtvnSthK3M7U7NUeJsroLIvQuIsgWNeIIJy4FVqamsQD5wAWgOOGjVMXkhWDsL2MM13UnI8Eoe02SHdRG5f6KAaJfs6AguinVKmn0k07byPcAGa6vFAUBFGTbUR5kBYL99ni7d4GfZlxK64vQySth.jpg",
    "sahseh_official.jpg": "https://saleenyeg.com/wp-content/uploads/2024/03/469535854_17912513349024739_2687275329685537307_n.jpg",
    "ew3a_weshak_official.jpg": "https://saleenyeg.com/wp-content/uploads/2024/03/IMG_2731-scaled-1-1.jpg",
    "2oolameme_official.webp": "https://cdn.shopify.com/s/files/1/0721/9822/6214/products/2oolawe3melegypt.webp?v=1716284222"
}

os.makedirs("downloads_official", exist_ok=True)
for fname, url in downloads.items():
    out_path = os.path.join("downloads_official", fname)
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp, open(out_path, 'wb') as f:
            f.write(resp.read())
        im = Image.open(out_path)
        print(f"Downloaded {fname}: size={im.size}, mode={im.mode}, filesize={os.path.getsize(out_path)} bytes")
    except Exception as e:
        print(f"Error downloading {fname}: {e}")

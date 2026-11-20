from PIL import Image

im = Image.open('scratch/crop_waraa_gareema.jpg')
W, H = im.size
print("Crop size:", W, H)

# Crop top text
top_txt = im.crop((int(W*0.35), 0, W, int(H*0.35)))
top_txt.save('scratch/waraa_top.jpg')

# Crop bottom text
bot_txt = im.crop((0, int(H*0.7), W, H))
bot_txt.save('scratch/waraa_bot.jpg')

from PIL import Image
im = Image.open(r"özelqr\1025438697.png")
width, height = im.size

left = 0
top = 0
right = 0

for i in range(41):
    top = height-(height-i)
    bottom = height-(height-(i+1))
    im1 = im.crop((left, top, right+width, bottom))

    im1.save(f"cropped_qr_00000000/{i:03d}.png")
     
from PIL import Image
im=Image.open("bike.png")
jpg=im.convert("RGB")
jpg.save("bike.jpg")
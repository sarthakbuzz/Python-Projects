from turtle import fillcolor
import qrcode

qr=qrcode.QRCode(version=1,box_size=10,border=5)

data=("https://lingarajtechhub.com/python-programmer-roadmap/")

qr.add_data(data)

img=qr.make_image(fill_color="black",back_color="white")

img.save("roadmap.jpg") 
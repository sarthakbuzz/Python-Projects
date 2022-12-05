import qrcode

file=qrcode.make("https://www.youtube.com/watch?v=QrQVrXQqRlo")

file.save("code.png")
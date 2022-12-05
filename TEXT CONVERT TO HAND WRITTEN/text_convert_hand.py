import pywhatkit as pw
txt="The share market is a platform where buyers and sellers come together to trade on publicly listed shares during specific hours of the day."
pw.text_to_handwriting(txt,"mk.txt",[255,0,0])
print(" END ")
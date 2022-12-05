from pdf2docx import Converter

pdf_file="ShareMarket1.pdf"
word_file="ShareMarket1.docx"

cv=Converter(pdf_file)
cv.convert(word_file,start=0,end=None)
cv.close()
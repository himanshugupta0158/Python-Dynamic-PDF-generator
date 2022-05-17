from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt

# pdf file creation with password protected 
# test = pdfencrypt.StandardEncryption('1234')
# pdf = canvas.Canvas("./reportlib_pdf.pdf",bottomup=0,encrypt=test)
pdf = canvas.Canvas("./reportlib_pdf.pdf",bottomup=0)

pdf.drawString(10,10,"test_pdf")
pdf.showPage()


pdf.save()

print("PDF Generated.")
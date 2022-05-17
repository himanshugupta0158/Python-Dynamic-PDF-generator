from reportlab.pdfgen import canvas


pdf = canvas.Canvas("./reportlib_pdf.pdf",bottomup=0)
pdf.drawString(10,10,"test_pdf")
pdf.showPage()

pdf.drawString(10,20,"test_pdf")
pdf.drawString(20,30,"test_pdf")


pdf.save()

print("PDF Generated.")
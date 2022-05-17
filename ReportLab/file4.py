from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch

# reportlab_directory = os.path.dirname(reportlab.__file__)
# print(reportlab_directory)

# String alignment in PDF.

pdf = canvas.Canvas("file5_pdf.pdf",bottomup=0)
pdf.translate(inch,inch)
pdf.setFont("Helvetica",12)
pdf.setFillColorRGB(0.1,0.22,0.31)

pdf.drawString(0,5,"normaltext")
pdf.drawRightString(10,10,"right aligned")

pdf.setFillColorRGB(0.1,0.5,0.31)
pdf.drawAlignedString(10,20,"abcde") # y, x, text
pdf.drawAlignedString(10,30 ,"abcdef")

pdf.save()





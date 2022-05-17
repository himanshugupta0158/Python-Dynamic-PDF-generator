from turtle import color
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors


pdf = canvas.Canvas("file_pdf5.pdf", bottomup=0)
pdf.translate(inch,inch)

# text rotation.
pdf.setFillColor(colors.aquamarine)
pdf.rotate(45)
pdf.drawString(1,5,"45 degrees")



pdf.save()
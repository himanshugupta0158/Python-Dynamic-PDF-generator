from reportlab.pdfgen import canvas
from reportlab.lib import pdfencrypt

c = canvas.Canvas("home.pdf")
c.save()

print("PDF Generated.")
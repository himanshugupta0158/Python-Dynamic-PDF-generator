from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

pdf = canvas.Canvas("fonttutorial.pdf")
fonts = pdf.getAvailableFonts()

print(fonts)
y=760

pdf.translate(inch,inch)

for font in fonts:
    pdf.setFont(font,15)
    pdf.setFillColorRGB(0,0.1,0.5)
    pdf.drawString(30,y,font)
    y -= 20


pdf.save()


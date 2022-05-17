from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm

pdf = canvas.Canvas("ReportLab/text3_pdf.pdf")

pdf.translate(cm ,cm)




pdf.save()
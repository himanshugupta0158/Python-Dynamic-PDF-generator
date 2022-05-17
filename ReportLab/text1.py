from reportlab.pdfgen import canvas 
from reportlab.lib.units import cm , inch 
from reportlab.lib import colors
import io

with io.open('ReportLab/chp1.txt') as f1 :
    data = f1.read()
    f1.close()

data = data.split('\n')
# print(data)

pdf = canvas.Canvas("ReportLab/text_pdf1.pdf")
pdf.translate(cm ,cm)

to = pdf.beginText()
to.setTextOrigin(15,700)

to.setFillColor(colors.blue)

# for i in range(len(data)):
#     to.textLine(data[i])

# or

to.textLines(data)

pdf.drawText(to)

pdf.drawImage("ReportLab/fox_face.png",150,730,80,80)

pdf.save()
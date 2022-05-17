from turtle import color
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm

c1 = [
    ["name","dob"],
    ["address","contact"],
    ["courses","session"],
    ["payment","mode"],
    ["reference","experience"]
    ]

pdf = canvas.Canvas("ReportLab/text_pdf2.pdf",bottomup=0)
pdf.translate(cm,cm)


pdf.rect(10,20,500,30,fill=1)
pdf.setFillColor(colors.blueviolet)
pdf.drawString(200,35,"Application Form")

k=20
for i in range(len(c1)):
    k += 30
    pdf.rect(10,k,255,30)
    pdf.drawString(40,k+20,c1[i][0])
    pdf.rect(255,k,255,30,)
    pdf.drawString(290,k+20,c1[i][1])




pdf.save()

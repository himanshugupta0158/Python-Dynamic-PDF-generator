from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch


pdf = canvas.Canvas("file_pdf9.pdf",bottomup=0)
pdf.translate(inch , inch)

pdf.setFillColor(colors.chocolate)
pdf.setStrokeColorRGB(0.01,0.07,0.067)
"""
reportlab circle format :-
pdf.circle(x_centre,y_centre, radius, stroke=1, fill=0)
"""
pdf.circle(0,0,20)


for i in range(100,1,-5):
    if i <= 50 and i > 40 :
        pdf.setStrokeColorRGB(0,0,0)
        pdf.setFillColor(colors.grey)
        pdf.circle(100,100,50,fill=1)
    elif i <= 40 :
        pdf.setStrokeColor(colors.whitesmoke)
        pdf.setFillColor(colors.royalblue)
        pdf.circle(100,100,i,fill=1)
    else:
        if i <= 100 and i > 95 :
            pdf.setStrokeColor(colors.black)
        else:
            pdf.setStrokeColor(colors.wheat)
        pdf.setFillColor(colors.azure)
        pdf.circle(100,100,i,fill=1)

p = 1
for i in range(100,1,-2):
    if p == 1 :
        pdf.setStrokeColor(colors.violet)
        p = 2
    elif p == 2:
        p = 3
        pdf.setStrokeColor(colors.white)
    elif p == 3:
        p = 4
        pdf.setStrokeColor(colors.blue)
    else:
        p = 1
        pdf.setStrokeColor(colors.blueviolet)
    pdf.setFillColor(colors.whitesmoke)
    pdf.circle(400,40,i,fill=1)

pdf.setStrokeColor(colors.black)
pdf.ellipse(x1=200,y1=150,x2=250,y2=250,fill=1)
pdf.setFillColor(colors.coral)
pdf.ellipse(10,400,100,200,fill=1)



# pdf.wedge(x1=200,y1=500,x2=450,y2=600,startAng=500,extent=50,fill=0)

pdf.wedge(x1=50,y1=500,x2=100,y2=700,startAng=50,extent=90,fill=1)


pdf.save()
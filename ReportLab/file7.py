from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

# Drawing different figure/shapes/polygons

pdf = canvas.Canvas("file_pdf7.pdf",bottomup=0)

pdf.translate(inch, inch)

"""
pdf.rect format :-
pdf.rect(x,y,width,height,stroke=1,fill=0)

"""
(x1,y1) = (10,20)
w,h = 70,40

pdf.setStrokeColorRGB(0.1,0.37,0.3)
pdf.setFillColor(colors.bisque)
pdf.rect(1,1,width=200,height=230,stroke=1,fill=1)

pdf.setStrokeColor(colors.blueviolet) # border color of rect/polygon/figure
pdf.rect(x1,y1,w,h,1,0)
pdf.rect(x1+5,y1+4,w-10,h-10,1,0)

# pdf.setFillColor(colors.aqua) # background fill color
pdf.setFillColorCMYK(0.2,0.1,0.7,0.2) #(CMYK = Cyan,Meganta,Yellow,Key)
pdf.rect(x1,y1+50,w,h,1,1)
pdf.setFillColor(colors.blue) # background fill color
pdf.rect(x1+5,y1+54,w-10,h-10,1,1)




pdf.save()
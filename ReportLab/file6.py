from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from math import pi

pdf = canvas.Canvas("file_pdf6.pdf",bottomup=0)

x1,y1 = (10,20)
x2,y2 = (200,20)
y = 5
pdf.setLineWidth(4)
pdf.setStrokeColor(colors.blueviolet)

# TO get the dimension of pdf page.
print(pdf._pagesize)
w,h = pdf._pagesize
x2=int(w)

for i in range(15):
    pdf.line(x1,y1,x2,y)
    y += 15
    x2 -= 5
    x1 += 5

# pdf.rotate(-45) # it will rotate -45 Degree 
for i in range(15):
    pdf.line(0,y,200,y)
    y += 10

# pdf.rotate(90)
pdf.rect(10,10,w-20,h-20)

def star(canvas, title="Title Here", aka="Comment here.",xcenter=None, ycenter=None, nvertices=5):
    from math import pi
    from reportlab.lib.units import inch
    radius=inch/3.0
    if xcenter is None: xcenter=2.75*inch
    if ycenter is None: ycenter=1.5*inch
    canvas.drawCentredString(xcenter, ycenter+1.3*radius, title)
    canvas.drawCentredString(xcenter, ycenter-1.4*radius, aka)
    p = canvas.beginPath()
    p.moveTo(xcenter,ycenter+radius)
    from math import pi, cos, sin
    angle = (2*pi)*2/5.0
    startangle = pi/2.0
    for vertex in range(nvertices-1):
        nextangle = angle*(vertex+1)+startangle
        x = xcenter + radius*cos(nextangle)
        y = ycenter + radius*sin(nextangle)
        p.lineTo(x,y)
    if nvertices==5:
        p.close()
    canvas.drawPath(p)


star(canvas=pdf,xcenter=100,ycenter=700)


pdf.save()
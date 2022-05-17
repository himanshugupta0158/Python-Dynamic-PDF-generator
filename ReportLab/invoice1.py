from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

pdf = canvas.Canvas("./ReportLab/invoice2.pdf",bottomup=0)
w,h = pdf._pagesize

"""
origin/border/corner point -> 
left-top (x=0,y=10), 
left-bottom = (x = 0,y = pagesize.height-2)
right-top (x = pagesize.width-10,y = 10)
right-bottom (x = pagesize.width-10, y = pagesize.height-2)
"""
pdf.drawString(0,10,"A")
pdf.drawString(w-10,10,"B")
pdf.drawString(0,h-2,"C")
pdf.drawString(w-10,h-2,"D")


pdf.save()
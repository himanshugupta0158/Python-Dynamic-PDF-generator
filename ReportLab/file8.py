from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib import colors

from reportlab.pdfgen import pdfimages

# Setting Image in pdf with origin starts from left-bottom

pdf = canvas.Canvas("file_pdf8.pdf")

"""
canvas.drawImage(PartnerLogo, line_x_start, line_y, width=line_width, 
                 preserveAspectRatio=True, mask='auto', anchor='c') 
"""
w,h = pdf._pagesize
pdf.setFillColor(colors.gray)
for i in range(100,1,-10):
    pdf.circle(300,550,i,fill=1)
pdf.drawImage("ReportLab/fox_face.png",250,500,width=100,height=100)

pdf.showPage()
pdf.drawImage("ReportLab/fox_face.png",0,0,width=100,height=100)
pdf.showPage()
pdf.drawImage("ReportLab/fox_face.png",0,h-100,width=100,height=100)
pdf.showPage()
pdf.drawImage("ReportLab/fox_face.png",w-100,0,width=100,height=100)
pdf.showPage()
pdf.drawImage("ReportLab/fox_face.png",w-100,h-100,width=100,height=100)


# work same but not recommended for normal purpose
# pdf.drawInlineImage("ReportLab/fox_face.png",w-100,h-100,width=100,height=100)







pdf.save()
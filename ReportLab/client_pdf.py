from tkinter import font
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase.pdfmetrics import stringWidth

s = ["""1.   he following Letter of Intent is drafted with reference to the Tenancy Agreement template written by
Digitalised Property Transactions Workgroup*(DPTWG). 
""",
"""
2.  The fields are auto filled up based on standard market practices and information provided in the mobile 
application. 
""",
"""
. 
""",
"""
3.  Please note that use of this Letter of Intent template is not mandated. Parties are free to negotiate 
the terms and conditions that will govern their contractual relationship when entering into an agreement. 
Please ensure that you fully understand the nature and implications of the contractual terms you will be
 agreeing to before signing the Letter of Intent.
"""

]

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))



pdf = canvas.Canvas("ReportLab/client_pdf2.pdf")
pdf.translate(cm, cm)

fonts = pdf.getAvailableFonts()
print(fonts)
text = pdf.beginText()
text.setTextOrigin(10,700)

text.setFont("Vera",10)

textWidth = stringWidth(s[3], 'Helvetica-Bold', 8) 


text.textLines(s[0])
text.textLines(s[1])
text.textLines(s[3])

pdf.drawText(text)

pdf.save()

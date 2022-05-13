from fpdf import FPDF, HTMLMixin

class PDF(FPDF,HTMLMixin):
    pass

pdf = PDF("P", "mm", "A4")

pdf.add_page()

# PDF border
pdf.line(10,10,pdf.w-10,10)# up line
pdf.line(10,pdf.h-10,10,10) # left line
pdf.line(10,pdf.h-10,pdf.w-10,pdf.h-10) # down line
pdf.line(pdf.w-10,10,pdf.w-10,pdf.h-10) # right line

"""# Setting font for text
pdf.set_font("courier", "B", 20)
pdf.set_text_color(0,0,0)

# INVOICE HEADER
pdf.cell(pdf.w-70)
pdf.cell(100,20,"INVOICE",ln=1)
pdf.line((pdf.w//2)-50,25,pdf.w-29,25) # down line


pdf.set_font("courier", "B", 10)

# Information
pdf.cell(20)
pdf.cell(0,20,"COMPANY NAME")

pdf.cell(-74)
pdf.cell(0,20,"CUSTOMER COMPANY NAME")
pdf.ln()

pdf.cell(20)
pdf.cell(0,20,"COMPANY NAME")

pdf.cell(-74)
pdf.cell(0,20,"CUSTOMER COMPANY NAME")
pdf.ln()

pdf.cell(20)
pdf.cell(0,20,"COMPANY NAME")

pdf.cell(-74)
pdf.cell(0,20,"CUSTOMER COMPANY NAME")
pdf.ln()
"""
html = """
<H1 align="center">html2fpdf</H1>
<h2 bgcolor="red">Basic usage</h2>
<p>You can now easily print text mixing different
styles : <B>bold</B>, <I>italic</I>, <U>underlined</U>, or
<B><I><U>all at once</U></I></B>!<BR>You can also insert links
on text, such as <A HREF="http://www.fpdf.org">www.fpdf.org</A>,
or on an image: click on the logo.<br>
<center>
</center>
<h3>Sample List</h3>
<ul><li>option 1</li>
<ol><li>option 2</li></ol>
<li>option 3</li></ul>

<table border="0" align="center" width="50%">
<thead><tr><th width="30%">Header 1</th><th width="70%">header 2</th></tr></thead>
<tbody>
<tr><td>cell 1</td><td>cell 2</td></tr>
<tr><td>cell 2</td><td>cell 3</td></tr>
</tbody>
</table>
"""

pdf.write_html(html)




pdf.output("invoice-report/pdf_invoice2.pdf")
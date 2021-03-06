from fpdf import FPDF, HTMLMixin

class PDF(FPDF,HTMLMixin):
    pass


pdf = PDF('P',"mm",'A4')

pdf.add_page()
name = "hitman"
# specify font
pdf.set_font('helvetica', '', 16)

pdf.cell(pdf.w-20, pdf.h-30,border=True)

html1 = """
<H1 align="center">html2fpdf</H1>
<h2>Basic usage</h2>
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

html2 = f"""
<body>
    This is sample .
    <table  border=1>
      <thead>
        <tr>
          <th align="left" width="30%">ID</th>
          <th align="left" width="70%">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Alice</td>
        </tr>
        <tr>
          <td>2</td>
          <td>{name}</td>
        </tr>
      </tbody>
    </table>
  </section>
  </body>
"""

pdf.write_html(html1)

pdf.output("invoice-report/pdf_invoice1.pdf")
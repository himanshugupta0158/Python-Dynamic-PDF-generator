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

# Setting font for text
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





pdf.output("FPDF/invoice-report/pdf_invoice2.pdf")
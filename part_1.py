from fpdf import FPDF

# create FPDF object

# Layout ('P','L') where P = Portrait mode and L is Landscape mode
# Unit ('mm','cm','inch')
# format ('A3', 'A4', (default), 'A5', 'Letter', 'Legal', (100,150))



pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()


# specify font
# fonts ('times', 'courier', 'helvetica','symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e.,('BU')->Bold and Underline)

# pdf.set_font('helvetica', '', 16)
pdf.set_font('helvetica', 'BIU', 16)
pdf.set_text_color(220,50,50)


# Add text 
# w = width
# h = height
# text = Your text
# ln = (0 False ; 1 True - move cursor down to next line.)
# border = (0 False; 1 True - add border around cell)

pdf.cell(120, 100, 'Hello World!', ln=1, border=True)

pdf.set_font('helvetica', '', 16)
pdf.cell(80, 10, "Hay World.",ln=1)
pdf.cell(80, 10, "Go Bye World.")

pdf.output('pdf_1.pdf')
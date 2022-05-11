from fpdf import FPDF


class PDF(FPDF):
    # Header
    def header(self):
        # logo
        self.image('fox_face.png', 10, 8, 25) # img , x, y, width

        # font
        self.set_font('helvetica', 'B', 20) 

        # Padding 
        self.cell(80)

        # Title
        self.cell(30,10,'Title', border=True, ln=1, align='C')

        # Line break
        self.ln(20)

    # Page Footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 10) 
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')




# Create PDF object
pdf = PDF('P', 'mm', 'A4')

# get total page number
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# specify font
pdf.set_font('times', '', 12)


for i in range(1,41):

    # Add text
    pdf.cell(0, 10, f'This is line {i} :D', ln=True)

pdf.output('pdf_2.pdf')
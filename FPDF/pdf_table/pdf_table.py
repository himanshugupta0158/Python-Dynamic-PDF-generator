from fpdf import FPDF
from create_table_fpdf2 import PDF


data = {
    "Name":["Himanshu", "Shivam","kartik", "Navin"],
    "Lastname":["Gupta",'Singh',"Gupta","Reddy"]
}
data_as_lst = [
    ["Name","SurName","B.tech_branch","Age"],
    ["Himanshu", "Gupta","CSE", "21"],
    ["Navin","Reddy","Mechanical","24"]
]

pdf = PDF()

pdf.add_page()

pdf.set_font("helvetica", size=10)

pdf.create_table(table_data=data, title="Test Table",cell_width='even')
pdf.ln(25)
pdf.create_table(table_data = data_as_lst,title="Test Table2",cell_width='uneven',x_start=10) 
pdf.ln(25)
pdf.create_table(table_data=data, title="Test Table3",align_header='R', align_data='R', cell_width=[20,25,10,45,], x_start='C', emphasize_data=['Himanshu'], emphasize_style='BIU',emphasize_color=(255,0,0))
pdf.ln(25)

pdf.output("Test_Table1.pdf")

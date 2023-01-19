from fpdf import FPDF

pdf = FPDF(format='A4')

pdf.add_page(orientation="P")
pdf.image("shirtificate.png", 15, 70, 180)
pdf.set_font("helvetica", "B", 50)
pdf.cell(65)
pdf.cell(70, 35, "CS50 Shirtificate", align="C")
pdf.set_text_color(255, 255,255)
pdf.set_y(-170)
pdf.set_font("helvetica", "I", 25)
pdf.cell(0, 1, "Vlad Maslianko took CS50", align="C")
pdf.output("page.pdf")

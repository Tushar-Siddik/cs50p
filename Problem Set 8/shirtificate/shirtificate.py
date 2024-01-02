from fpdf import FPDF
# pip install fpdf2
# https://pypi.org/project/fpdf2/
# https://py-pdf.github.io/fpdf2/Tutorial.html
# https://py-pdf.github.io/fpdf2/fpdf/


class PDF(FPDF):
    def header(self):

        # Rendering logo:
        self.image("shirtificate.png", x=13.5, y=40, w=180)
        # Setting font: helvetica bold 15

        self.set_font("helvetica", "B", 15)
        # # Moving cursor to the right:
        # self.cell(80)
        # Printing title:
        self.cell(80, 10, "CS50 Shirtificate", border=1, align="C", center=True)
        # # Performing a line break:
        # self.ln(20)


# Instantiation of inherited class
name = input("Name: ")
pdf = PDF()
pdf.add_page()
# pdf.cell(800)
# pdf.set_font("Times", "B", 15)
pdf.set_y(100)
pdf.set_text_color(r=255, g=255, b=255)
pdf.cell(w=None, h= None, text = f"{name} took CS50", align="C", center=True)
pdf.output("shirtificate.pdf")

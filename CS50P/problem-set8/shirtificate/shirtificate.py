from fpdf import FPDF
from PIL import Image

"""
File: shirtificate.py
Description:
    Generating a personalized CS50 Shirtificate in PDF format.

"""


def main():

    pdf = FPDF()
    pdf.set_margins(left=10, top=10, right=10)
    pdf.add_page(orientation='P', format='A4')

    # Set title
    pdf.set_font('Times', 'B', 40)
    pdf.cell(0, 20, 'CS50 Shirtificate', ln=True, align='C')

    # Add some space
    pdf.ln(20)

    # Add the shirt image
    shirt = Image.open("shirtificate.png")
    width, height = shirt.size
    pdf.image("shirtificate.png", x=(210 - 190) / 2, w=190, h=(190/width)*height)

    name = input("Enter your name: ")

    # Set font and text color to white for name on shirt
    pdf.set_font('Times', 'B', 26)
    pdf.set_text_color(255, 255, 255)

    txt = name + " took CS50"

    # Position the name on top of the shirt
    pdf.text(x=55, y=110, txt=txt)

    # Output the PDF
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()

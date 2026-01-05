from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        #title on top
        self.set_font("Helvetica", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

def main():
    #get user name
    name = input("Name: ").strip()

    pdf = Shirtificate(orientation="P", format="A4")
    pdf.add_page()

    #settings for the shirt
    shirt_width = 190  # mm
    page_width = pdf.w
    pos_x = (page_width - shirt_width) / 2

    #A Centered shirt image
    pdf.image("shirtificate.png", x=pos_x, y=60, w=shirt_width)

    #here the code inscribes name on the shrt
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(255, 255, 255)  #white colour
    pdf.set_xy(0, 140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")

    # resulting pdf as required
    pdf.output("shirtificate.pdf")

# conventional pattern 😉
if __name__ == "__main__":
    main()

from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(False, 0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Times", "B", 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0,24,row["Topic"],0,1,"L")
    # A4 size paper have width of total 210mm
    pdf.line(10, 27, 200, 27)

    #A4 size has a height of total 298mm
    pdf.ln(250)
    pdf.set_font("Times", "I", 8)
    pdf.set_text_color(180,180,180)
    pdf.cell(0, 10, row["Topic"], align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()
        pdf.ln(274)
        pdf.cell(0, 10, row["Topic"], align="R")

pdf.output("output.pdf")
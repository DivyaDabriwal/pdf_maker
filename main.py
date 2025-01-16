from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

pdf.set_auto_page_break(False, 0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Times', 'B', 24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 12, row['Topic'], 0, 1, align='L')
    # A4 size paper have width of total 210mm
    # pdf.line(10, 27, 200, 27)

    #A4 size has a height of total 298mm
    for i in range(20, 298, 10):
        pdf.line(10, i, 200, i)
    pdf.ln(267)
    pdf.set_text_color(180, 180, 180)
    pdf.set_font('Times', 'I', 8)
    pdf.cell(0, 10, row['Topic'], 0, align='R')

    for item in range(row["Pages"]-1):
        pdf.add_page()
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)
        pdf.ln(279)
        pdf.cell(0, 10, row['Topic'], 0, align='R')

pdf.output("output.pdf")
from fpdf import FPDF
import pandas as pd

df = pd.read_csv('topics.csv')

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.set_font("Times", "B", 24)
pdf.set_text_color(100, 100, 100)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.cell(0,24,row["Topic"],0,1,"L")
    # A4 size paper have width of total 210mm
    pdf.line(10, 27, 200, 27)

pdf.output("output.pdf")

# print(df)

# pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, txt="Hello", align="L", ln=1, border='B')
#
#
# # pdf.set_y(-25)
# # pdf.set_font(family="Times", style="B", size=12)
# # pdf.cell(0, 12, 'Hi', 0,0,'C')
# pdf.output("output.pdf")
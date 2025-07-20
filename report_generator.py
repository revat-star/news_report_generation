from fpdf import FPDF
import datetime
import os
import imghdr

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "News Report", ln=True, align="C")
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

def create_pdf_report(articles, sentiment_summary):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Date: {datetime.datetime.now().date()}", ln=True)
    pdf.ln(5)

    pie_path = "charts/sentiment_pie.png"
    if os.path.exists(pie_path) and imghdr.what(pie_path) == 'png':
        pdf.image(pie_path, x=10, w=90)
    else:
        pdf.cell(0, 10, "No valid sentiment chart available.", ln=True)

    timeline_path = "charts/timeline.png"
    if os.path.exists(timeline_path) and imghdr.what(timeline_path) == 'png':
        pdf.image(timeline_path, x=110, w=90)
    else:
        pdf.cell(0, 10, "No valid timeline chart available.", ln=True)

    pdf.ln(65)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sentiment Summary:", ln=True)
    for k, v in sentiment_summary.items():
        pdf.cell(0, 10, f"{k.capitalize()}: {v}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Top Headlines:", ln=True)
    pdf.set_font("Arial", size=11)
    for article in articles[:10]:
        pdf.multi_cell(0, 8, f"[{article['date']}] {article['title']} ({article['sentiment']})")
        pdf.ln(1)

    path = os.path.join(REPORT_DIR, "news_report.pdf")
    pdf.output(path)
    return path
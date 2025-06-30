import pandas as pd
import streamlit as st
from jinja2 import Environment, FileSystemLoader
import pdfkit

def save_user_input(input_df, prediction):
    if "history" not in st.session_state:
        st.session_state["history"] = []
    st.session_state["history"].append((input_df.to_dict(), prediction))

def load_user_history():
    return st.session_state.get("history", [])

def generate_pdf_report(data):
    env = Environment(loader=FileSystemLoader("reports"))
    template = env.get_template("report_template.html")
    html_out = template.render(data=data)
    pdfkit.from_string(html_out, "reports/credit_report.pdf")

import pdfkit
import os

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"  # adjust if installed elsewhere
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

import os
from jinja2 import Environment, FileSystemLoader

def generate_html_report(data, filename="credit_report.html"):
    env = Environment(loader=FileSystemLoader("reports"))
    template = env.get_template("report_template.html")
    html_out = template.render(data=data)

    report_path = os.path.join("reports", filename)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html_out)
    return report_path

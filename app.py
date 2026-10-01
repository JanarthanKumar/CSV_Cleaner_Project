import io
import csv
from datetime import datetime
import streamlit as st

def parse_date(date_str):
    formats = [
        "%d-%m-%Y",
        "%d-%m-%y",
        "%Y/%m/%d",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d/%m/%y",
        "%d %b %Y",
        "%d %B %Y"
    ]
    cleaned_str = date_str.strip()
    for fmt in formats:
        try:
            return datetime.strptime(cleaned_str, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return cleaned_str

def clean_and_transpose(raw_lines):
    reader = csv.reader(raw_lines)
    rows = list(reader)
    if not rows:
        return []

    header = rows[0]
    expected_cols = len(header)
    cleaned_rows = [header]

    for row in rows[1:]:
        if len(row) != expected_cols:
            continue
        if any(cell.strip() == "" for cell in row):
            continue

        cleaned_row = list(row)
        cleaned_row[0] = parse_date(cleaned_row[0])
        cleaned_rows.append(cleaned_row)

    transposed = list(zip(*cleaned_rows))
    return [list(col) for col in transposed]

st.set_page_config(page_title="CSV Matrix Cleaner", layout="wide")

st.title("CSV Matrix Transposer & Cleaner")

uploaded_file = st.file_uploader("Upload Messy CSV File", type=["csv"])

if uploaded_file is not None:
    file_contents = uploaded_file.getvalue().decode("utf-8", errors="ignore").splitlines()
    
    st.subheader("Raw Uploaded Content")
    raw_reader = list(csv.reader(file_contents))
    st.write(raw_reader)
    
    processed_matrix = clean_and_transpose(file_contents)
    
    if processed_matrix:
        st.subheader("Cleaned & Transposed Output Matrix")
        st.write(processed_matrix)
        
        output_buffer = io.StringIO()
        writer = csv.writer(output_buffer)
        writer.writerows(processed_matrix)
        
        st.download_button(
            label="Download Cleaned CSV",
            data=output_buffer.getvalue(),
            file_name="cleaned_transposed.csv",
            mime="text/csv"
        )
    else:
        st.error("No valid complete rows found in the uploaded file.")
        
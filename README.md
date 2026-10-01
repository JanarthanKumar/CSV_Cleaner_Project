# CSV Matrix Transposer & Cleaner 🧹📊

A lightweight, local web application that acts as an automated ETL (Extract, Transform, Load) pipeline for messy spreadsheet data. 

In data science and analytics, we often reach straight for heavy libraries like Pandas to handle our data. I built this project to prove I can handle dirty, real-world data using foundational Python data structures and pure algorithmic logic first. 

## 🚀 What It Does
This tool ingests messy bank statements or generic CSV exports and outputs a perfectly formatted matrix ready for SQL databases or Power BI dashboards. 

* **Broken Row Filtering:** Automatically detects and drops rows with missing critical data (e.g., a transaction missing an amount or a dropped status code).
* **Dynamic Date Parsing:** Captures inconsistent date strings (like `12-04-26`, ` 10 December 2026 `, or `2026/04/13`) and standardizes them into a clean `YYYY-MM-DD` format.
* **Matrix Transposition:** Flips rows into columns using list comprehensions to restructure the dataset for specific analytical models.
* **Zero-Friction UI:** Provides a clean drag-and-drop web interface using Streamlit to visualize the "Before" and "After" transformations in real-time.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Data Processing:** Pure Python (`csv`, `datetime`, string slicing, list comprehensions)
* **Frontend:** Streamlit

## 💻 How to Run It Locally

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/yourusername/csv-matrix-cleaner.git](https://github.com/yourusername/csv-matrix-cleaner.git)

Navigate into the project directory:cd csv-matrix-cleaner

Install the required web framework:pip install -r requirements.txt

Launch the application:python -m streamlit run app.py

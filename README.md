# Brand Funnel Visualizer

This Streamlit app lets you upload an Excel file with brand funnel metrics by quarter and visualize the funnel as a chart.

## 📁 Required Excel Format

| Brand    | Metric             | Q1'23 | Q2'23 | Q3'23 | Q4'23 | Q1'24 |
|----------|--------------------|-------|-------|-------|-------|-------|
| Al Hilal | Total Awar Score   | 58%   | 60%   | 62%   | 65%   | 68%   |
| Al Hilal | Brand Con Score    | 45%   | 47%   | 50%   | 52%   | 55%   |
| Liv      | Total Awar Score   | 50%   | 53%   | 55%   | 56%   | 58%   |

## 🚀 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌐 How to Deploy on Streamlit Cloud
1. Push the files to a public GitHub repo
2. Go to https://streamlit.io/cloud and click "New App"
3. Select your repo and set `app.py` as the main file
4. Click "Deploy"

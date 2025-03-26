# multi-source-mlb-stats
# 🏀 Multi-Source MLB Stats Pipeline

This project pulls MLB player statistics from **two different sources** (RotoWire and ESPN), cleans and normalizes the data, merges it into a unified dataset, and pushes the final result to **Google Sheets**. It's designed to demonstrate skills in data engineering, web scraping, data cleaning, and pipeline automation.

---

## 🔗 Data Sources

| Source     | Method         | Description                              |
|------------|----------------|------------------------------------------|
| RotoWire   | API (JSON)     | Full player stats for ~750 players       |
| ESPN       | Web Scraping   | Top 50 player stats scraped from table   |

---

## 💡 Technologies Used
- Python 3.12+
- Pandas
- BeautifulSoup
- Requests
- gspread + Google Sheets API
- Virtual Environment (`venv`)

---

## 🚀 Pipeline Overview

1. **`fetch_rotowire.py`**
   - Pulls structured JSON from RotoWire
   - Cleans and normalizes column names

2. **`fetch_espn.py`**
   - Scrapes HTML table from ESPN
   - Cleans, extracts, and normalizes stats

3. **`merge_stats.py`**
   - Matches columns across both datasets
   - Flags ESPN "Top 50" players in RotoWire
   - Saves merged dataset to CSV

4. **`push_to_sheets.py`**
   - Authenticates with Google Sheets
   - Clears and uploads the final dataset

5. **`scrape_all.py`**
   - Orchestrates the entire flow
   - Can be run as a daily job

---

## 🔄 Sample Usage
```bash
# Run entire pipeline
python3 scripts/scrape_all.py
```

---

## 🔧 Setup Instructions

### 1. Clone the Repo and Create a Virtual Environment
```bash
git clone https://github.com/your-username/multi-source-mlb-stats.git
cd multi-source-mlb-stats
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Google Sheets Credentials
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a project
- Enable Sheets + Drive APIs
- Create a **service account**
- Generate and download the `credentials.json` file
- Share your Google Sheet with the **service account email** (Editor access)

> ⚡ Note: This file should NOT be committed to your repo. Make sure `credentials.json` is in your `.gitignore`.

---

## 📊 Sample Output
A Google Sheet containing ~750 player stats from RotoWire, with ESPN top players flagged.

---

## 🔗 Future Improvements
- Add support for additional sources (e.g. Baseball-Reference)
- Automate via CRON or GitHub Actions
- Build a Streamlit dashboard
- Integrate with a database (e.g. PostgreSQL)

---

## 👍 Why It Matters
This project simulates a real-world multi-source data pipeline, showing how to:
- Extract data from APIs and web pages
- Clean and normalize disparate schemas
- Merge intelligently and track source lineage
- Deliver clean, usable data to stakeholders

Great for data engineering, sports analytics, or just showing you know how to ship a working pipeline.

---

**Built by Tony Persaud ✨**


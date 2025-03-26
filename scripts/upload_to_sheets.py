import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe

def push_to_google():
    # Auth
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    # Open sheet
    sheet = client.open("Multi-Source MLB Tracker").sheet1

    # Load DataFrame
    df = pd.read_csv("data/clean/rotowire_with_flags.csv")

    # Clear old content and upload
    sheet.clear()
    set_with_dataframe(sheet, df)

    

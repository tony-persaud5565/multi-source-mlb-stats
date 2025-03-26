# scripts/scrape_all.py

from scripts.fetch_rotowire import fetch_rotowire
from scripts.fetch_espn import fetch_mlb_stats
from scripts.merge_stats import merge_stats
from scripts.upload_to_sheets import push_to_google

def main():
    print("Fetching RotoWire data...")
    df_roto = fetch_rotowire()
    
    print("Fetching ESPN data...")
    df_espn = fetch_mlb_stats()

    print("Merging and saving...")
    df_merged = merge_stats()

    print("Pushing to Google Sheets...")
    push_to_google()

    print("✅ All done.")

if __name__ == "__main__":
    main()

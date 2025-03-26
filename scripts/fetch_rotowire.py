import pandas as pd
import requests
from bs4 import BeautifulSoup
def fetch_rotowire():
    #API Endpoint from RotoWire
    url = 'https://www.rotowire.com/baseball/tables/player-basic-stats.php?pos=B&league=3&season=2024&filter=0'
    response = requests.get(url)

    #Parse JSON
    data = response.json()

    #convert to dataframe and get rid of not needed columns in df
    df=pd.DataFrame(data)
    df=df.iloc[:,4:]
    df.drop(columns=df.columns[2],inplace=True)
    df.drop(columns=df.columns[3],inplace=True)
    df.drop(columns=df.columns[14],inplace=True)
    df.drop(columns=df.columns[14],inplace=True)
    df.drop(columns=df.columns[14],inplace=True)
    df.drop(columns=df.columns[14],inplace=True)

#adjusting column names
    df = df.rename(columns=
   {'player':'name',
    'team':'team',
    'position':'position',
    'games':'games_played',
    'ab':'at_bats',
    'runs':'runs',
    'hits':'hits',
    'doubles':'doubles',
    'triples':'triples',
    'hr':'home_runs',
    'rbi':'runs_batted_in',
    'walks':'walks',
    'strikes':'strikes',
    'steals':'steals',
    'avg':'avg',
    'obp':'on_base_percentage',
    'slg':'slugging_percentage',
    'ops':'on_base_plus_slugging',
  })
    print("Current columns:", df.columns.tolist())  
#adjusting column order
    desired_order = ['name','team','position','games_played','at_bats','runs','hits','doubles','triples','home_runs','runs_batted_in','walks','strikes','steals','avg','on_base_percentage','slugging_percentage','on_base_plus_slugging']
    df = df[desired_order]

#getting rid of Jr. in name field
    df["name"] = df["name"].str.replace(r"\s+Jr\.?", "", regex=True)

#Save to CSV
    csv_filename='data/clean/rotowire_stats.csv'
    df.to_csv(csv_filename, index=False)

    return df
if __name__ == "__main__":
    print(fetch_rotowire().head())


import pandas as pd 
from bs4 import BeautifulSoup
import requests

def fetch_mlb_stats():
    url = "https://www.espn.com/mlb/stats/player/_/season/2024/seasontype/2"
    headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.90 Safari/537.36"
}
    response = requests.get(url,headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to load page:{response.status_code}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    table_names =soup.find_all('table')[0]
    table_stats = soup.find_all('table')[1]

    if table_names == None:
        raise Exception("Failed to find table")
    if table_stats == None:
        raise Exception("Failed to find table")
    
    headers_name =[th.text.strip() for th in table_names.find('thead').find_all('th')]
    headers_stats =[th.text.strip() for th in table_stats.find('thead').find_all('th')]

    name_rows=[]
    for tr in table_names.find('tbody').find_all('tr'):
        cells = [td.text.strip() for td in tr.find_all("td")]
        if len(cells) == len(headers_name):
            name_rows.append(cells)

    stat_rows=[]
    for tr in table_stats.find('tbody').find_all('tr'):
        cells = [td.text.strip() for td in tr.find_all("td")]
        if len(cells) == len(headers_stats):
            stat_rows.append(cells)

    
    df_names = pd.DataFrame(name_rows, columns=headers_name)
    df_stats = pd.DataFrame(stat_rows, columns=headers_stats)
    df_names["Team"] = df_names["Name"].str.extract(r"([A-Z]{2,3})$")
    df_names["Name"] = df_names["Name"].str.replace(r"([A-Z]{2,3})$", "", regex=True).str.strip()
    df= pd.concat([df_names,df_stats], axis=1)
    df.drop(columns=df.columns[0],inplace=True)
    df.drop(columns=df.columns[12],inplace=True)
    df.drop(columns=df.columns[18],inplace=True)

    df = df.rename(columns=
   {'Name':'name',
    'Team':'team',
    'POS':'position',
    'GP':'games_played',
    'AB':'at_bats',
    'R':'runs',
    'H':'hits',
    '2B':'doubles',
    '3B':'triples',
    'HR':'home_runs',
    'RBI':'runs_batted_in',
    'BB':'walks',
    'K':'strikes',
    'SB':'steals',
    'AVG':'avg',
    'OBP':'on_base_percentage',
    'SLG':'slugging_percentage',
    'OPS':'on_base_plus_slugging',
  })
    
    desired_order = ['name','team','position','games_played','at_bats','runs','hits','doubles','triples','home_runs','runs_batted_in','walks','strikes','steals','avg','on_base_percentage','slugging_percentage','on_base_plus_slugging']
    df = df[desired_order]
   

 
    csv_filename = 'data/clean/espn_stats.csv'
    df.to_csv(csv_filename, index=False)

    return df

if __name__ == "__main__":
    print(fetch_mlb_stats().head())

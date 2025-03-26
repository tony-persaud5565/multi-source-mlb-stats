import pandas as pd 

def merge_stats():
    # Load the data
    df_roto = pd.read_csv("data/clean/rotowire_stats.csv")
    df_espn = pd.read_csv("data/clean/espn_stats.csv")

    #Flag fata with filtering
    df_roto["In_ESPN_Top_50"] = df_roto["name"].isin(df_espn["name"])
    df_roto.to_csv("data/clean/rotowire_with_flags.csv", index=False)

    return df_roto
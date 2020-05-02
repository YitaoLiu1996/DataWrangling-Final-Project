import requests
import pandas as pd


def getStat(season):
    url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=200' + str(season) + "-0" + str((season+1)) + '&SeasonType=Regular+Season&StatCategory=PTS'
    r = requests.get(url).json()

    df = pd.DataFrame(r['resultSet']['rowSet'], columns=r['resultSet']['headers'])
    print(df)
    filename = 'stats-0' + str(season) +"0" + str((season)+1)
    #df.to_csv(filename, index=False)
    
    


df1617 = getStat(2)



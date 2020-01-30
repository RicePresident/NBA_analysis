import pandas as pd
import numpy as np

df1 = pd.read_csv('15-16_NBA_player_stats.csv')
df2 = pd.read_csv('16-17_NBA player_stats.csv')
df3 = pd.read_csv('17-18_NBA_player_stats.csv')
df4 = pd.read_csv('18-19_NBA_player_stats.csv')



stats = pd.DataFrame(df2, columns = ['Rk','Player','Pos','Age','Tm','G','GS','MP','FG','FGA','FG%','3P','3PA',
                                    '3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST',
                                    'STL','BLK','TOV','PF','PTS','MP','PER','TS%','3PAr','FTr','ORB%','DRB%',
                                    'TRB%','AST%','STL%','BLK%','TOV%','USG%','OWS','DWS','WS','WS/48','OBPM',
                                    'DBPM','BPM','VORP'])

stats

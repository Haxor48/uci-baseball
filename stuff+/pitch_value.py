import numpy as np
import pybaseball as pb
import pandas as pd
import requests

def get_mlb_game_data(start, end):
    all_games = []
    for i in range(start, end+1):
        response = requests.get(f'https://statsapi.mlb.com/api/v1/schedule?sportId=1&startDate={i}-01-01&endDate={i}-12-31&gameType=R&fields=dates,date,games,gamePk')
        json = response.json()
        for date in json['dates']:
            for game in date['games']:
                all_games.append(game['gamePk'])
    
    for code in all_games:
        

if __name__ == '__main__':
    print(list(pb.statcast_single_game(529429).columns))
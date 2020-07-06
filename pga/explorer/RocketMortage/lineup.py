
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import minimize
import pulp
from pydfs_lineup_optimizer import get_optimizer, Site, Sport


class Lineups():
    def __init__(self):

        self.data = pd.read_csv('all_strokes_gained.csv')
        self.salaries = pd.read_csv('DKSalaries_RM.csv')
        self.topdogs = pd.read_csv('topdogs.csv')
        self.darkhorse = pd.read_csv('darkhorses.csv')

        self.sg_putting = self.data['SG: Putting-AVERAGE']
        self.sg_around = self.data['SG: Around-the-Green-AVERAGE']
        self.sg_approach = self.data['SG: Approach the Green-AVERAGE']
        self.sg_ttg = self.data['SG: Tee-to-Green-AVERAGE']
        self.sg_ott = self.data['SG: Off-the-Tee-AVERAGE']
    
    def score_player(self, Wputting, Waround, Wapproach, Wttg, Wott, version=''):

        #self.salaries['Avg Points Per Game'] = 

        self.salaries['AvgPointsPerGame'] = (self.sg_putting * Wputting) + (self.sg_around * Waround) + (self.sg_approach * Wapproach) + (self.sg_ttg * Wttg) + (self.sg_ott * Wott)

        self.salaries.fillna(0, inplace=True)

        #print(self.salaries)

        print(f'SG: Putting-AVERAGE {Wputting}% || SG: Approach the Green-AVERAGE {Waround}% || SG: Tee-to-Green-AVERAGE {Wapproach}% || SG: Off-the-Tee-AVERAGE {Wttg}% || SG: Around-the-Green-AVERAGE{Wott}%')

        self.file = self.salaries.to_csv(f'draftkings_{version}.csv')

        self.file_name = self.file


    def top_dogs(self, Wputting, Waround, Wapproach, Wttg, Wott, version=''):

        self.topdogs['AvgPointsPerGame'] = (self.sg_putting * Wputting) + (self.sg_around * Waround) + (self.sg_approach * Wapproach) + (self.sg_ttg * Wttg) + (self.sg_ott * Wott)

        self.topdogs.fillna(0, inplace=True)

        #print(self.salaries)

        print(f'SG: Putting-AVERAGE {Wputting}% || SG: Approach the Green-AVERAGE {Waround}% || SG: Tee-to-Green-AVERAGE {Wapproach}% || SG: Off-the-Tee-AVERAGE {Wttg}% || SG: Around-the-Green-AVERAGE{Wott}%')

        self.csv_file = self.topdogs.to_csv(f'topdog_{version}.csv')

    

    def dark_horse(self, Wputting, Waround, Wapproach, Wttg, Wott, version=''):

        self.darkhorse['AvgPointsPerGame'] = (self.sg_putting * Wputting) + (self.sg_around * Waround) + (self.sg_approach * Wapproach) + (self.sg_ttg * Wttg) + (self.sg_ott * Wott)

        self.darkhorse.fillna(0, inplace=True)

        #print(self.salaries)

        print(f'SG: Putting-AVERAGE {Wputting}% || SG: Approach the Green-AVERAGE {Waround}% || SG: Tee-to-Green-AVERAGE {Wapproach}% || SG: Off-the-Tee-AVERAGE {Wttg}% || SG: Around-the-Green-AVERAGE{Wott}%')

        self.csv_file = self.darkhorse.to_csv(f'darkhorse_{version}.csv')





    def optimize(self):
        optimizer = get_optimizer(Site.DRAFTKINGS, Sport.GOLF)
        optimizer.load_players_from_csv(f'{self.file_name}')
        for lineup in optimizer.optimize(n=1):
            print(lineup)
            print(lineup.players) # list of players
            print(lineup.fantasy_points_projection)
            print(lineup.salary_costs)

from Ranking import Ranking
from Tournament import Tournament
import random
import math

class SimulatedAnnealing:
    tournament = None
    initial_ranking = None
    initial_temp = None
    temp_length = None
    cooling_ratio = None
    num_non_improve = None

    def __init__(self, tournament=None, initial_ranking=None, initial_temp=None, temp_length=None, cooling_ratio=None, num_non_improve=None):
        self.tournament = tournament
        self.initial_ranking = initial_ranking
        self.initial_temp = initial_temp
        self.temp_length = temp_length
        self.cooling_ratio = cooling_ratio
        self.num_non_improve = num_non_improve

    def search(self):
        stagnant_iterations = 0
        current_ranking = self.initial_ranking
        best_ranking = self.initial_ranking
        current_temp = self.initial_temp
        while stagnant_iterations < self.num_non_improve:
            for i in range(1, self.temp_length):
                new_ranking = Ranking(neighbour=current_ranking, swap_index=random.randint(0, len(current_ranking)-2))
                print("Examining:" + str(new_ranking))
                delta_score = new_ranking.get_kemeny_score()-current_ranking.get_kemeny_score()
                if new_ranking.get_kemeny_score() < best_ranking.get_kemeny_score():
                    best_ranking = new_ranking
                    stagnant_iterations = -1
                
                if delta_score <= 0:
                    current_ranking = new_ranking
                elif random.uniform(0,1) < math.e**((-delta_score)/current_temp):
                    current_ranking = new_ranking
                stagnant_iterations += 1
            current_temp *= cooling_ratio
        return best_ranking
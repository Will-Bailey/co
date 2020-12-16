from Ranking import Ranking
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
                random_index_1 = random.randint(0, len(current_ranking)-1)
                random_index_2 = random.randint(0, len(current_ranking)-1)
                while random_index_1 == random_index_2:
                    random_index_2 = random.randint(0, len(current_ranking)-1)

                new_ranking = Ranking(neighbour=current_ranking, swap_index_1=min([random_index_1, random_index_2]), swap_index_2=max([random_index_1, random_index_2]))
                delta_score = new_ranking.get_kemeny_score()-current_ranking.get_kemeny_score()
                
                if new_ranking.get_kemeny_score() < best_ranking.get_kemeny_score():
                    best_ranking = new_ranking
                    stagnant_iterations = -1
                
                if delta_score <= 0:
                    current_ranking = new_ranking
                    print("Making downhill move")
                elif random.uniform(0,1) < math.e**((-delta_score)/current_temp):
                    print("Making uphill move")
                    current_ranking = new_ranking
                stagnant_iterations += 1
            current_temp *= self.cooling_ratio
        return best_ranking
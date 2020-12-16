from ranking import Ranking
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
        # Initialise the variables of the search
        stagnant_iterations = 0
        current_ranking = self.initial_ranking
        best_ranking = self.initial_ranking
        current_temp = self.initial_temp

        # Outer loop to iterate over varying temperatures until the stoping criterion is met
        while stagnant_iterations < self.num_non_improve:
            # Inner loop to iterate over random neighbouring solutions of the current solution for the temperature length
            for i in range(1, self.temp_length):
                #Pick 2 random indices to switch to genereate a neighbouring solution
                new_ranking = Ranking(neighbour=current_ranking, swap_index=random.randint(1, len(current_ranking)-1))

                # Calculate the difference in Kemeny Score between the 2 solutions being comapred
                delta_score = new_ranking.get_kemeny_score()-current_ranking.get_kemeny_score()
                
                # If the new ranking is better than the best ranking found so far:
                if new_ranking.get_kemeny_score() < best_ranking.get_kemeny_score():
                    best_ranking = new_ranking
                    #Reset the number of stagnant iterations to -1 (will be 0 by the end of this iteration of the inner loop)
                    stagnant_iterations = -1
                
                # If the new ranking is better than the current ranking, accept the new ranking
                if delta_score <= 0:
                    current_ranking = new_ranking
                    print("Making downhill move")
                # Else if the new ranking is worse than the current ranking, accept the new ranking on a probabilty based on the current temperature
                elif random.uniform(0,1) < math.e**((-delta_score)/current_temp):
                    print("Making uphill move")
                    current_ranking = new_ranking
                
                # Increase the number of solutions that have been looked at since the last improvement to the best solution
                stagnant_iterations += 1
                print(best_ranking.get_kemeny_score(), best_ranking.calc_kemeny_score())
            # Alter the current temperature
            current_temp *= self.cooling_ratio
        return best_ranking
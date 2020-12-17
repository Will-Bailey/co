from tournament import Tournament
from ranking import Ranking
from simulatedAnnealing import SimulatedAnnealing
import time
import sys
import csv

def main():
    assert len(sys.argv)==2, "Please pass the file containing the tournament data as an argument."  
    
    tournament = Tournament(definition_file=sys.argv[1])
    initial_ranking = Ranking(order=list(range(0, len(tournament.participants))), tournament=tournament)
    
    start = time.perf_counter()
    final_ranking = tournament.get_best_ranking(initial_ranking=initial_ranking, initial_temp=41, temp_length=32, cooling_ratio=0.999, num_non_improve=50000)
    end = time.perf_counter()

    print("The following ranking has a Kemeny Score of " + str(final_ranking.get_kemeny_score()) + ". This solution was reached in " + str((end-start) * 1000) + "ms.")
    print(final_ranking.get_table())

def tuning_trials():
    assert len(sys.argv)==2, "Please pass the file containing the tournament data as an argument."  
    
    tournament = Tournament(definition_file=sys.argv[1])
    initial_ranking = Ranking(order=list(range(0, len(tournament.participants))), tournament=tournament)

    base_initial_temp = 40
    base_temp_length = 45
    base_cooling_ratio = 0.99
    base_num_non_improve = 50000

    best_rating = sys.maxsize


    with open("trials.csv", "w", newline="") as out_file:
        writer = csv.writer(out_file)
        writer.writerow(["Initial Temperature", "Temperature Length", "Cooling Ratio", "num_non_improve", "Runtime", "Kemeny Score", "Rating"])
        while True:
            
            range_initial_temp = []
            range_temp_length = []
            range_cooling_ratio = []
            range_num_non_improve = []

            bases = [base_initial_temp, base_temp_length, base_cooling_ratio, base_num_non_improve]
            ranges = [range_initial_temp, range_temp_length, range_cooling_ratio, range_num_non_improve]

            for pair in zip(bases, ranges):
                for percentage in [0.9, 1, 1.1]:
                    pair[1].append(pair[0]*percentage)

            temp = []
            for value in range_temp_length:
                temp.append(round(value))
            range_temp_length = temp

            for initial_temp in range_initial_temp:
                for temp_length in range_temp_length:
                    for cooling_ratio in range_cooling_ratio:
                        for num_non_improve in range_num_non_improve:
                            start = time.perf_counter()
                            final_ranking = tournament.get_best_ranking(initial_ranking=initial_ranking, initial_temp=initial_temp, temp_length=temp_length, cooling_ratio=cooling_ratio, num_non_improve=num_non_improve)
                            end = time.perf_counter()

                            rating = (end-start)*final_ranking.get_kemeny_score()

                            if best_rating > rating:
                                best_rating = rating
                                base_initial_temp = initial_temp
                                base_temp_length = temp_length
                                base_cooling_ratio = cooling_ratio
                                base_num_non_improve = num_non_improve
                                print("Best Variables: ", base_initial_temp, base_temp_length, base_cooling_ratio, base_num_non_improve)

                            writer.writerow([initial_temp, temp_length, cooling_ratio, num_non_improve, end-start, final_ranking.get_kemeny_score(), rating])




if __name__ == "__main__":
    main()

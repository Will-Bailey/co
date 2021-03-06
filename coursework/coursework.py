from Tournament import Tournament
from Ranking import Ranking
from SimulatedAnnealing import SimulatedAnnealing 

tournament = Tournament(definition_file="1994_Formula_One.wmg")

initial_ranking = Ranking(order=list(range(0, len(tournament.participants))), tournament=tournament)

final_ranking = tournament.get_best_ranking(initial_ranking=initial_ranking, initial_temp=300, temp_length=45, cooling_ratio=0.999, num_non_improve=100000)

print(final_ranking.get_kemeny_score(), final_ranking.get_participants())

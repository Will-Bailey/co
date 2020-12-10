from Tournament import Tournament
from Ranking import Ranking
from SimulatedAnnealing import SimulatedAnnealing 

tournament = Tournament(definition_file="1994_Formula_One.wmg")

initial_ranking = Ranking(order=list(range(0, len(tournament.participants))), tournament=tournament)

search = SimulatedAnnealing(tournament=tournament, initial_ranking=initial_ranking, initial_temp=100, temp_length=200, cooling_ratio=0.999, num_non_improve=10000)

final_ranking = search.search()

print(final_ranking.get_kemeny_score(), final_ranking.get_participants())

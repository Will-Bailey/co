from Tournament import Tournament
from Ranking import Ranking
from SimulatedAnnealing import SimulatedAnnealing 

tournament = Tournament(definition_file="1994_Formula_One.wmg")

initial_ranking = Ranking(order=list(range(0, len(tournament.participants))), tournament=tournament)
#print(initial_ranking.get_participants())

search = SimulatedAnnealing(tournament=tournament, initial_ranking=initial_ranking, initial_temp=7, temp_length=45, cooling_ratio=0.99, num_non_improve=30)

final_ranking = search.search()

print(final_ranking.get_participants())
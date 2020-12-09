import Ranking
import Tournament
import SimulatedAnnealing 

tournament = Tournament(definition_file="1994_Formula_One.wmg")
initial_ranking = Ranking(tournament=tournament, order=range(0, len(tournament.participants)))

search = SimulatedAnnealing(tournament=tournament, initial_ranking=initial_ranking, initial_temp=7, temp_length=45, cooling_ratio=0.99, num_non_improve=30)

final_ranking = search.search

print(final_ranking.print_participants())
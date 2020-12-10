import copy

class Ranking(list):
    kemeny_score = None
    tournament = None

    def __init__(self, order=None, tournament=None, neighbour=None, swap_index=None):
        if (order!=None) & (tournament!=None):
            self.build_from_order(order, tournament)
        elif (neighbour!=None) & (swap_index!=None):
            self.build_from_neighbour(neighbour, swap_index)
        else:
            assert False, "Invalid configuration of build variables"
        
    def build_from_order(self, order, tournament):
        super().__init__(order)
        self.tournament = tournament
        self.kemeny_score = self.calc_kemeny_score()

    def build_from_neighbour(self, neighbour, swap_index):
        
        self.build_from_order(list(neighbour), neighbour.tournament)

        self[swap_index], self[swap_index+1] = self[swap_index+1], self[swap_index]

        delta_score = 0
        for edge in self.tournament.edges:
            # If the new higher ranked participant won, decrease the kemeny score by the weight of this edge
            if edge[1]==self[swap_index] & (edge[2]==self[swap_index + 1]):
                delta_score -= edge[0]
            # Else if the new higher ranked participant lost, increase the kemeny score by the weight of this edge
            elif edge[1]==self[swap_index] & (edge[2]==self[swap_index + 1]):
                delta_score += edge[0]
        self.kemeny_score += delta_score

    def __str__(self):
        #return str(self.get_participants())
        return str(self.get_indices())

    def calc_kemeny_score(self):
        tournament = self.tournament
        ranking = self
        assert len(tournament.participants)==len(ranking)

        score = 0

        for edge in tournament.edges:
            winner = edge[1]
            loser = edge[2]

            if ranking.index(winner) > ranking.index(loser):
                score += edge[0]

        return score

    def get_kemeny_score(self):
        return self.kemeny_score

    def get_participants(self):
        participant_ranking = []
        for i in self:
            participant_ranking.append(self.tournament.participants[i])
        return participant_ranking

    def get_indices(self):
        return list(self)


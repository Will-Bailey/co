import copy

class Ranking(list):
    kemeny_score = None
    tournament = None

    def __init__(self, order=None, tournament=None, neighbour=None, swap_index_1=None, swap_index_2=None):
        if (order!=None) & (tournament!=None):
            self.build_from_order(order, tournament)
        elif (neighbour!=None) & (swap_index_1!=None) & (swap_index_2!=None):
            self.build_from_neighbour(neighbour, swap_index_1, swap_index_2)
        else:
            assert False, "Invalid configuration of build variables"
        
    def build_from_order(self, order, tournament):
        super().__init__(order)
        self.tournament = tournament
        self.kemeny_score = self.calc_kemeny_score()

    def build_from_neighbour(self, neighbour, swap_index_1, swap_index_2):
        assert swap_index_1 < swap_index_2
        
        self.build_from_order(list(neighbour), neighbour.tournament)

        self[swap_index_1], self[swap_index_2] = self[swap_index_2], self[swap_index_1]

        delta_score = 0
        for edge in self.tournament.edges:
            if swap_index_1 == edge[1] & edge[2] in self[swap_index_1:(swap_index_2 + 1)]:
                self.kemeny_score += edge[0]
            elif swap_index_2 == edge[1] & edge[2] in self[swap_index_1:swap_index_2 + 1]:
                self.kemeny_score -= edge[0]
            elif swap_index_1 ==edge[2] & edge[1] in self[swap_index_1:swap_index_2 + 1]:
                self.kemeny_score -= edge[0]
            elif swap_index_2 ==edge[2] & edge[1] in self[swap_index_1:swap_index_2 + 1]:
                self.kemeny_score += edge[0]

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


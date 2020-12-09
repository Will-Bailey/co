class Ranking(List):
    kemeny_score = None
    tournament = None

    def __init__(order=None, tournament=None, neighbour=None, swap_index=None):
        if (order!=None) && (tournament!=None):
            self.build_from_order(order, tournament)
        elif (ranking!=None) && (swap_index!=None):
            self.build_from_neighbour(neighbour, swap_index)
        else:
            assert False, "Invalid configuration of build variables"
        

    def build_from_order(self, order, tournament):
        self = order
        self.tournament = tournament
        self.kemeny_score = get_kemeny_score(self)

    def build_from_neighbour(self, neighbour, swap_index):
        self = neighbour[swap_index], neighbour[swap_index + 1] = neighbour[swap_index + 1], neighbour[swap_index]
        self.tournament = neighbour.tournament
        self.kemeny_score = neighbour.kemeny_score 

        for edge in self.tournament:
            # If the new higher ranked participant won, decrease the kemeny score by the weight of this edge
            if edge[1]==self[swap_index] && (edge[2]==self[swap_index + 1]):
                self.kemeny_score -= edge[0]
            # Else if the new higher ranked participant lost, increase the kemeny score by the weight of this edge
            elif edge[1]==self[swap_index] && (edge[2]==self[swap_index + 1]):
                self.kemeny_score += edge[0]

    def get_kemeny_score(self):
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




    def get_neighbours():
        pass
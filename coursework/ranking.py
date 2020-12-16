import copy

# A ranking is an ordering of the particpants of a tournament
class Ranking(list):
    kemeny_score = None
    tournament = None

    # Constructor to determine how the ranking will be created, either from scratch or as a neighbour of an existing ranking
    def __init__(self, order=None, tournament=None, neighbour=None, swap_index=None):
        if (order!=None) & (tournament!=None):
            self.build_from_order(order, tournament)
        elif (neighbour!=None) & (swap_index!=None):
            self.build_from_neighbour(neighbour, swap_index)
        else:
            assert False, "Invalid configuration of build variables"
        
    # The build method for constructing a ranking from scratch using a tournament and an ordering
    def build_from_order(self, order, tournament):
        super().__init__(order)
        self.tournament = tournament
        self.kemeny_score = self.calc_kemeny_score()

    # The build method for constructing the neighbour of an existing ranking.
    def build_from_neighbour(self, neighbour, swap_index):
        # Copy the neighbour and swap the desired elemtents to create a new ranking
        self.build_from_order(list(neighbour), neighbour.tournament)
        self.insert(0, self.pop(swap_index))

        # Calculate the difference in kemeny score
        for edge in self.tournament.edges:
            if edge[1] == self[0] & self.index(edge[2]) <= swap_index:
                self.kemeny_score -= edge[0]
            elif edge[2] == self[0]:
                self.kemeny_score += edge[0]
    
    #String method fro printing the ranking
    def __str__(self):
        return str(self.get_indices())

    #The method used to calculate the kemeny score of a ranking from scratch 
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


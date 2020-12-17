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
        assert swap_index >= 1

        # Copy the neighbour and swap the desired elemtents to create a new ranking
        #self.build_from_order(list(neighbour), neighbour.tournament)
        super().__init__(list(neighbour))
        self.tournament = neighbour.tournament
        self.kemeny_score = neighbour.get_kemeny_score()
        self.insert(0, self.pop(swap_index))

        # Calculate the difference in kemeny score
        for i in range(1, swap_index+1):
            winning_edge = self.tournament.edges[self[0]][self[i]]
            loosing_edge = self.tournament.edges[self[i]][self[0]]
            if winning_edge>=0:
                self.kemeny_score -= winning_edge
            elif loosing_edge>=0:
                self.kemeny_score += loosing_edge

    #String method for printing the ranking
    def __str__(self):
        return str(self.get_indices())

    #The method used to calculate the kemeny score of a ranking from scratch 
    def calc_kemeny_score(self):
        assert len(self.tournament.participants)==len(self)

        score = 0

        for winner in range(0, len(self.tournament.participants)):
            for looser in range(0, len(self.tournament.participants)):
                if (self.tournament.edges[winner][looser]>=0) & (self.index(winner) > self.index(looser)):
                    score += self.tournament.edges[winner][looser]

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


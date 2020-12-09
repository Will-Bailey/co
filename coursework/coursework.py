class Tournament:
    participants = []
    edges = []
    meta = ""

    def __init__(definition_file=None, definition_string=None):
        if definition_file!=None:
            self.build_from_file(definition_file)
        elif definition_string!=None:
            self.build_from_string(definition_string)
        assert False, "No arguments have been given to build from"


    def build_from_string(self, string):
        #deconstruct the string in to lines and elements within those lines
        lines = string.splitlines()
        for line in lines:
            line = line.split(",")

        num_participants = lines.pop(0)
        self.meta = lines.pop(num_participants+2)

        for line in lines:
            if int(line[0]) <= num_participants:
                self.participants.append = line[1]
            else:
                sanitised_line = (int(line[0]), int(line[1])-1, int(line[2])-1)
                self.edeges.append(sanitised_line)

    def build_from_file(self, file):
        with open(file, "r") as input_file:
            self.build_from_string(input_file.read())

    def __str__(self):
        string = ""
        string += str(len(participants))
        string += "\n"

        for participant in participants:
            string += str(index(participant)+1)
            string += ","
            string += participant
            string += "\n"

        string += meta
        string+= "\n"
        
        for edge in edges:
            string += str(edge[0])
            string += str(edge[1]+1)
            string += str(edge[2]+1)
            string += "\n"

    return string

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
            winner = tournament.participants.get(edge[1])
            loser = tournament.participants.get(edge[2])

            if ranking.index(winner) > ranking.index(loser):
                score += edge[0]

        return score




    def get_neighbours():
        pass



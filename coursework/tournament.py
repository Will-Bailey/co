from SimulatedAnnealing import SimulatedAnnealing

# A tournament is a set of participants and a set of weighted edges between these participants
class Tournament:
    participants = []
    edges = []
    meta = ""

    # The constructor for the tournament class which can be built either from a file or from a string
    def __init__(self, definition_file=None, definition_string=None):
        if definition_file!=None:
            self.build_from_file(definition_file)
        elif definition_string!=None:
            self.build_from_string(definition_string)
        else:
            assert False, "No arguments have been given to build from"

    # The build method for constructing a tournament from a string
    def build_from_string(self, string):
        lines = string.splitlines()

        # Remove the 2 lines that conatin metadata not necessary to encode within the tournament
        num_participants = int(lines.pop(0))
        self.meta = lines.pop(num_participants)

        # Iterate through the lines and parse them into the relevant attributes of the tournament
        for line in lines:
            full_line = line
            line = line.split(",")
            if lines.index(full_line) < num_participants:
                self.participants.append(line[1])
            else:
                sanitised_line = (int(line[0]), int(line[1])-1, int(line[2])-1)
                self.edges.append(sanitised_line)

    # The build method for constructing a tournament from a file by extracting the string from that file
    def build_from_file(self, file):
        with open(file, "r") as input_file:
            self.build_from_string(input_file.read())

    # Overwrite the string method of this class to return a string equivalent to the string used to construct the tournament.
    def __str__(self):
        string = ""
        string += str(len(self.participants))
        string += "\n"

        for participant in self.participants:
            string += str(self.participants.index(participant)+1)
            string += ","
            string += participant
            string += "\n"

        string += self.meta
        string+= "\n"
        
        for edge in self.edges:
            string += str(edge[0])+","
            string += str(edge[1]+1)+","
            string += str(edge[2]+1)
            string += "\n"

        return string

    # Conduct a simulated annealing search to find the ranking of this tournament with the lowest Kemeny score
    def get_best_ranking(self, initial_ranking, initial_temp, temp_length, cooling_ratio, num_non_improve):
        
        search = SimulatedAnnealing(tournament=self, initial_ranking=initial_ranking, initial_temp=initial_temp, temp_length=temp_length, cooling_ratio=cooling_ratio, num_non_improve=num_non_improve)

        return search.search()
class Tournament:
    participants = []
    edges = []
    meta = ""

    #The constructor for the tournament class which can be built either from a file or from a string
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

    #Overwrite the string method of this class to return a string equivalent to the string used to construct the tournament.
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
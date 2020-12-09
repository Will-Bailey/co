class SimulatedAnnealing:
    tournament = None
    initial_solution = None
    initial_temperature
    temperature_length
    cooling_ratio = 0.5
    num_non_improve = 10

    def __init__(tournament):

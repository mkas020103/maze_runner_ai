class Blue:
    def __init__(self, manhattan, power_up):
        self.power_up = power_up
        self.pos = (self.power_up[1][0], self.power_up[1][1])

        # Distance of each point to the goal
        self.manhattan = manhattan

    def move_closer(self, explorable):
        # Get the paths that are explorable only
        current_paths = [x for x in explorable if x in self.manhattan]

        # Return the explorable point with the smallest manhattan value
        best_path = min(current_paths, key=lambda x: self.manhattan[x])
        print('best path: ', best_path)
        return best_path

# Example usage
manhattan = {(160, 516): 250, (110, 566): 150, (160, 566): 200, (210, 566): 250, (110, 616): 100, 
             (210, 616): 200, (110, 666): 50, (210, 666): 150, (160, 716): 50}

power_up = [(100, 500), (160, 566)]  # Example power_up list
explorable = [(1024, 30), (1024, 80), (974, 80), (1074, 80)]

blue = Blue(manhattan, power_up)
best_path = blue.move_closer(explorable)
print("Best path to move closer:", best_path)

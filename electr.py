import math

class Electr:
    def __init__(self):
        self.distance = float('0.0')
        self.heights = []

    def read_data(self, name_in_file):
        with open(name_in_file, 'r') as dijkstra_in_file:
            self.distance = int(dijkstra_in_file.readline())

            self.heights = list(map(int, dijkstra_in_file.readline().split(" ")))

    def counting_length_of_lines(self):
        length_of_lines = 0

        for i in range(len(self.heights)):
            if i%2 == 1:
                self.heights[i] = 1

        for i in range(len(self.heights) - 1):            
            length_of_line = (self.distance**2 + (self.heights[i] - self.heights[i+1])**2)**(1/2)
            length_of_lines += length_of_line

        return round(length_of_lines, 2)

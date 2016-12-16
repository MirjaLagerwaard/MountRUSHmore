import csv
import cProfile
import re
from board import *
from vehicle import *
from algorithm import *

vehicles = {}

# fp = "test.csv"

# Breadth 33 zetten
# fp = "vehicles_6x6_1.csv"

# Breadth 15 zetten
# fp = "vehicles_6x6_2.csv"

# Breadth 21 zetten
# fp = "vehicles_6x6_3.csv"

# Card 9 zetten -> Breadth 9 zetten -> Depth 13
# fp = "vehicles_6x6_game1.csv"

# Card 16 zetten -> Breadth 16 zetten -> Depth 49
# fp = "vehicles_6x6_game2.csv"

# Card 16 zetten -> Breadth 16 -> Depth 485
fp = "vehicles_6x6_game3.csv"

# Card 15 zetten -> Breadth 15 zetten -> Depth 160
# fp = "vehicles_6x6_game4.csv"

# Breadth 27 moves -> Depth ...
# fp = "vehicles_9x9_1.csv"

# Breadth ... -> Depth ...
# fp = "vehicles_9x9_2.csv"

# Breadth ... -> Depth ...
# fp = "vehicles_9x9_3.csv"

# Random's best: 175 zetten
# fp = "vehicles_12x12.csv"

def main():
    with open(fp, "rb") as fileRushhour:
        reader_vehicles = csv.reader(fileRushhour, delimiter=',')
        for vehicle in reader_vehicles:
            vehicles[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

    Board1 = Board(6, 6, 2, vehicles)
    max_depth = 20
    solution_list = []
    while max_depth != -1:
        print "Current max_depth: ", max_depth
        max_depth, solution_list = DepthFirstSearch(Board1, max_depth, solution_list)
        Board1 = Board(6, 6, 2, vehicles)

    # iterate backwards over de parent boards in solution list
    for i, boards in enumerate(solution_list[::-1]):
        # print the number of moves
        print "s: ", i
        # print the board
        boards.printBoard()

if __name__ == "__main__":
    main()

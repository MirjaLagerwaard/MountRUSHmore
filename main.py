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

# Card 9 zetten -> Breadth 9 zetten -> Depth ...
# fp = "vehicles_6x6_game1.csv"

# Card 16 zetten -> Breadth 16 zetten -> Depth ...
# fp = "vehicles_6x6_game2.csv"

# Card 16 zetten -> Breadth 16 -> Depth ...
# fp = "vehicles_6x6_game3.csv"

# Card 15 zetten -> Breadth 15 zetten -> Depth ...
# fp = "vehicles_6x6_game4.csv"

# Breadth ... -> Depth ...
# fp = "vehicles_9x9_1.csv"

# Breadth ... -> Depth ...
# fp = "vehicles_9x9_2.csv"

# Breadth ... -> Depth ...
# fp = "vehicles_9x9_3.csv"

# Random's best: 175 zetten
fp = "vehicles_12x12.csv"

def main():
    with open(fp, "rb") as fileRushhour:
        reader_vehicles = csv.reader(fileRushhour, delimiter=',')
        for vehicle in reader_vehicles:
            vehicles[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

    Board1 = Board(12, 12, 5, vehicles)
    Random(Board1)

if __name__ == "__main__":
    main()

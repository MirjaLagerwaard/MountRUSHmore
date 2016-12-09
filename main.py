import csv
import cProfile
import re
from board import *
from vehicle import *
from algorithm import *

#9x9_2 Barbara haar pc: 24 moves, 5.5 miljoen staten
#9x9 Mirja haar pc: 551965 staten, memory error
#6x6_1 Mirja haar pc: 15 sec runtime (waarvan 9 sec bezig in deepcopy)

vehicles = {}
#
# fp = "test.csv"
# fp = "vehicles_6x6_1.csv"
# fp = "vehicles_6x6_3.csv"

# 9 zetten -> Breadth 10 zetten
# fp = "vehicles_6x6_game1.csv"

# 16 zetten -> Breadth 16 zetten
# fp = "vehicles_6x6_game2.csv"

# 16 zetten
fp = "vehicles_6x6_game3.csv"

# fp = "vehicles_9x9_1.csv"
# fp = "vehicles_9x9_2.csv"
# fp = "vehicles_9x9_3.csv"


def main():
    with open(fp, "rb") as fileRushhour:
        reader_vehicles = csv.reader(fileRushhour, delimiter=',')
        for vehicle in reader_vehicles:
            vehicles[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

    Board1 = Board(6, 6, 1, vehicles)
    BreadthFirstSearch(Board1)

if __name__ == "__main__":
    main()

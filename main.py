import csv
from board import *
from vehicle import *

hor_auto = {}
ver_auto = {}

# fp = "test.csv"
fp = "vehicles_6x6.csv"

with open(fp, "rb") as fileRushhour:
    reader_vehicles = csv.reader(fileRushhour, delimiter=',')
    for vehicle in reader_vehicles:
        if vehicle[0] == "H":
            hor_auto[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))
        if vehicle[0] == "V":
            ver_auto[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

Board1 = Board(6, 6, 2, hor_auto, ver_auto)
initBoard1 = Board1.makeBoard()
#move1 = Board1.updateBoard(vehicle[1], 1, 2)
Board1.BreadthFirstSearch()

import csv
from board import *

hor_auto = {}
ver_auto = {}

with open("test.csv", "rb") as fileVehicle:
    reader_vehicles = csv.reader(fileVehicle, delimiter=',')
    for vehicle in reader_vehicles:
        if vehicle[0] == "H":
            hor_auto[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))
        if vehicle[0] == "V":
            ver_auto[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

Board1 = Board(4, 6, 1)
initBoard1 = Board1.makeBoard(hor_auto, ver_auto)
# move1 = Board1.updateBoard(hor_auto, ver_auto, vehicle[1], 1, 2)
print Board1.possibleMoves(hor_auto, ver_auto)
Board1.isSolution(hor_auto)

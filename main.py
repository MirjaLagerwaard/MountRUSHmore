import csv
from board import *

hor_auto = []
ver_auto = []

with open("1_vehicle_test.csv", "rb") as fileVehicle:
    reader_vehicles = csv.reader(fileVehicle, delimiter=',')
    for vehicle in reader_vehicles:
        if vehicle[0] == "H":
            hor_auto.append(Vehicle(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4]))
        if vehicle[0] == "V":
            ver_auto.append(Vehicle(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4]))

Board1 = Board(3, 3, 1)
initBoard1 = Board1.makeBoard(hor_auto, ver_auto)
move1 = Board1.updateBoard(hor_auto, ver_auto, vehicle[1], 2, 0)

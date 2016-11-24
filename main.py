import csv
from board import *

hor_auto = []
ver_auto = []

with open("vehicles_12x12.csv", "rb") as fileVehicle:
    reader_vehicles = csv.reader(fileVehicle, delimiter=',')
    for vehicle in reader_vehicles:
        if vehicle[0] == "H":
            hor_auto.append(Vehicle(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4]))
        if vehicle[0] == "V":
            ver_auto.append(Vehicle(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4]))

Board1 = Board(12, 12, 5)
initBoard1 = Board1.makeBoard(hor_auto, ver_auto)

#
# print hor_auto[0].x
# print ver_auto[0].y
# print initBoard1

import csv
# import cProfile
# import re
from board import *
from vehicle import *

#9x9 Barbara haar pc: 3491677

def BreadthFirstSearch(board):
    """
    Breadth-first search (BFS) is an algorithm for traversing or searching
    tree or graph data structures. It starts at the tree root (or some
    arbitrary node of a graph, sometimes referred to as a 'search key'[1])
    and explores the neighbor nodes first, before moving to the next level
    neighbors.
    """
    # make the archive (as a dict) and the queue (as a list)
    archive = {toString(board.vehicles): 0} # hash van startbord (board1)
    queue = Queue.Queue()

    queue.put(board.vehicles) # stopt alleen nog maar de auto's in de queue

    # while there are items in the queue
    while queue:
        # pop the first item of the queue (FIFO: first in, first out)
        parent_vehicles = queue.get() # pak de eerste lijst van auto's die in de queue staat

        print "Layer: ", archive[toString(parent_vehicles)], " Archive_len:", len(archive)

        board.makeBoard(parent_vehicles) # reset het bord voor we possibleMoves gaan doen

        # get all the possible moves of this parent state, i.e. the children
        moves = board.possibleMoves()

        # iterate over each possible move
        for ID, move_list in moves.iteritems():
            # iterate over each x- and y-coordinate
            for (x, y) in move_list:
                # make a copy of the child state
                child_vehicles = copy.deepcopy(parent_vehicles)

                # update array
                child_vehicles = updateArray(child_vehicles, ID, x, y)

                # print len(archive)

                # if the child is in the archive, break out of loop
                if toString(child_vehicles) in archive:
                    break

                board.updateBoard(ID, x, y, parent_vehicles)


                # if the child is the solution, print party and how many moves were needed, and return
                if board.isSolution():
                    board.printBoard()
                    print "Firework, Champagne, Confetti!"
                    print str(archive[toString(parent_vehicles)] + 2) + " moves were needed."
                    return

                # add the child state to archive and report the depth of the graph
                archive[toString(child_vehicles)] = archive[toString(parent_vehicles)] + 1

                # add the children of the parent state to the queue
                queue.put(child_vehicles)

                old_x = parent_vehicles[ID].x
                old_y = parent_vehicles[ID].y
                board.updateBoard(ID, old_x, old_y, child_vehicles)

def toString(vehicles):
    """
    Makes a string of the state of the board.
    """

    s = ""

    for _, vehicle in vehicles.iteritems():
        if vehicle.dir == 'H':
            s += str(vehicle.x)
        if vehicle.dir == 'V':
            s += str(vehicle.y)

    return s

def updateArray (vehicles, ID, x, y):
    if vehicles[ID].dir == 'H':
        vehicles[ID].x = x
    elif vehicles[ID].dir == 'V':
        vehicles[ID].y = y

    return vehicles

vehicles = {}

#fp = "test.csv"
fp = "vehicles_6x6.csv"
# fp = "vehicles_9x9_1.csv"
# fp = "vehicles_9x9_2.csv"
fp = "vehicles_9x9_3.csv"

# 551965
# def main():

with open(fp, "rb") as fileRushhour:
    reader_vehicles = csv.reader(fileRushhour, delimiter=',')
    for vehicle in reader_vehicles:
        vehicles[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

Board1 = Board(9, 9, 4, vehicles)
BreadthFirstSearch(Board1)

# if __name__ == "__main__":
#     cProfile.run('main()')

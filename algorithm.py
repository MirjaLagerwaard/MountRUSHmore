import copy
import Queue
import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def toString(vehicles):
    """
    Makes a string of the state of the board.
    """

    # make string
    s = ""

    # iterate over each vehicle in the array with vehicles
    for _, vehicle in vehicles.iteritems():
        # store the x-coordinate when
        if vehicle.dir == 'H':
            s += str(vehicle.x)

        if vehicle.dir == 'V':
            s += str(vehicle.y)

    return s

def updateArray (ID, x, y, vehicles):
    """
    Updates the array of vehicles.
    """

    if vehicles[ID].dir == 'H':
        vehicles[ID].x = x
    elif vehicles[ID].dir == 'V':
        vehicles[ID].y = y

    return vehicles

def Random(board):
    """
    TODO
    """

    plot_moves = []
    original_board = copy.deepcopy(board)

    for i in range(10):

        print "Iteration: ", i
        total_moves = 1
        new_list = []
        archive_list = []
        archive_length = 1
        counter_archive = 0
        board = copy.deepcopy(original_board)

        while not board.isSolution() and total_moves < 175:

            moves = board.possibleMoves()

            for i in range (0, len(moves)):
                for j in range (0, len(moves.values()[i])):
                    new_list.append((moves.values()[i][j], moves.keys()[i]))

            #Total random:
            random_move, ID = random.choice(new_list)
            x, y = random_move

            # Pseudorandom:
            # ID = random.choice(moves.keys())
            # x, y = random.choice(moves[ID])

            board.updateBoard(ID, x, y, board.vehicles)
            board.vehicles = updateArray(ID, x, y, board.vehicles)

            total_moves += 1

            new_list = []

        if board.isSolution():
            print str(total_moves) + " moves were needed."
            plot_moves.append(total_moves)

    plot_moves.sort()
    print plot_moves

    n, bins, patches = plt.hist(plot_moves, 15, normed=1, facecolor='grey', alpha=0.75)
    plt.show()


def DepthFirstSearch(board):
    """
    Depth-first search (DFS) is an algorithm for traversing or
    searching tree or graph data structures. One starts at the
    root (selecting some arbitrary node as the root in the case
    of a graph) and explores as far as possible along each branch
    before backtracking.
    """

    stack = []
    archive = {toString(board.vehicles): 0}
    bound = 175

    stack.append(board.vehicles)

    while stack > 0 and bound < 175:

        parent_vehicles = stack.pop()
        board.makeBoard(parent_vehicles)
        moves = board.possibleMoves()

        # iterate over each possible move
        for ID, move_list in moves.iteritems():
            # iterate over each x- and y-coordinate
            for (x, y) in move_list:
                # make a copy of the child state
                child_vehicles = copy.deepcopy(parent_vehicles)

                # update array
                child_vehicles = updateArray(ID, x, y, child_vehicles)

                if toString(child_vehicles) in archive:
                    continue

                board.updateBoard(ID, x, y, parent_vehicles)

                if board.isSolution():
                    # hoeveel stappen heeft het gekost = in welke diepte zit je om bij deze oplossing te komen?
                    # stel dit in als nieuwe bound (bound = nieuw getal)
                    # ga verder

                    # print "Firework, Champagne, Confetti!"
                    #
                    # solution_list = []
                    #
                    # solution_list.append(copy.deepcopy(board))
                    #
                    # crawler = archive[toString(child_vehicles)]
                    # while archive[toString(crawler)] != 0:
                    #     board.makeBoard(crawler)
                    #     solution_list.append(copy.deepcopy(board))
                    #     crawler = archive[toString(crawler)]
                    #
                    # for i, boards in enumerate(solution_list[::-1]):
                    #     print "Moves: ", i
                    #     boards.printBoard()
                    #
                    # print "Total moves: ", i + 2
                    # return

                # add the child state to archive
                archive[toString(child_vehicles)] = archive[toString(parent_vehicles)] + 1

                # add the children of the parent state to the queue
                stack.append(child_vehicles)

                old_x = parent_vehicles[ID].x
                old_y = parent_vehicles[ID].y
                board.updateBoard(ID, old_x, old_y, child_vehicles)

    print "No solution found."


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
    while queue.qsize():
        # pop the first item of the queue (FIFO: first in, first out)
        parent_vehicles = queue.get() # pak de eerste lijst van auto's die in de queue staat

        # print "Layer: ", archive[toString(parent_vehicles)], " Archive_len:", len(archive)

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
                child_vehicles = updateArray(ID, x, y, child_vehicles)

                # print len(archive)

                # if the child is in the archive, break out of loop
                if toString(child_vehicles) in archive:
                    continue

                archive[toString(child_vehicles)] = parent_vehicles

                board.updateBoard(ID, x, y, parent_vehicles)
                # if the child is the solution, print party and how many moves were needed, and return
                if board.isSolution():
                    print "Firework, Champagne, Confetti!"

                    solution_list = []

                    solution_list.append(copy.deepcopy(board))

                    crawler = archive[toString(child_vehicles)]
                    while archive[toString(crawler)] != 0:
                        board.makeBoard(crawler)
                        solution_list.append(copy.deepcopy(board))
                        crawler = archive[toString(crawler)]

                    for i, boards in enumerate(solution_list[::-1]):
                        print "Moves: ", i
                        boards.printBoard()

                    print "Total moves: ", i + 2
                    return

                # add the children of the parent state to the queue
                queue.put(child_vehicles)

                old_x = parent_vehicles[ID].x
                old_y = parent_vehicles[ID].y
                board.updateBoard(ID, old_x, old_y, child_vehicles)

    print "No solution found."

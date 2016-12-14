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

    s = ""

    for _, vehicle in vehicles.iteritems():
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

    for i in range(1000):

        print "Iteration: ", i
        total_moves = 1
        new_list = []
        archive_list = []
        archive_length = 1
        counter_archive = 0
        board = copy.deepcopy(original_board)

        while not board.isSolution() and total_moves < 527:

            moves = board.possibleMoves()

            for i in range (0, len(moves)):
                for j in range (0, len(moves.values()[i])):
                    new_list.append((moves.values()[i][j], moves.keys()[i]))

            #Total random:
            random_move, ID = random.choice(new_list)
            x, y = random_move

            # Pseudo random:
            # ID = random.choice(moves.keys())
            # x, y = random.choice(moves[ID])

            # Archive:
            # while [x, y, ID] in archive_list:
            #     random_move, ID = random.choice(new_list)
            #     x, y = random_move
            # archive_list.append([x, y, ID])
            # counter_archive += 1
            #
            # if counter_archive == archive_length:
            #     counter_archive = 0
            #     archive_list = []

            board.updateBoard(ID, x, y, board.vehicles)
            board.vehicles = updateArray(ID, x, y, board.vehicles)

            total_moves += 1

            new_list = []

        if board.isSolution():
            print str(total_moves) + " moves were needed."
            plot_moves.append(total_moves)

    plot_moves.sort()
    print plot_moves

    n, bins, patches = plt.hist(plot_moves, 15, normed=1, facecolor='green', alpha=0.75)
    plt.show()


def DepthFirstSearch(board):
    """
    Depth-first search (DFS) is an algorithm for traversing or
    searching tree or graph data structures. One starts at the
    root (selecting some arbitrary node as the root in the case
    of a graph) and explores as far as possible along each branch
    before backtracking.
    """

    # make a stack
    stack = []
    archive = {toString(board.vehicles): 0} # hash van startbord (board1)

    stack.append(board.vehicles)

    while stack:
        parent_vehicles = stack.pop()

        print "Archive_len:", len(archive)

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
                child_vehicles = updateArray(ID, x, y, child_vehicles)

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

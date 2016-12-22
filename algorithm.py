import csv
import copy
import Queue
import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from board import *
from vehicle import *

def PrepareFile(fp, shape):
    """
    Prepares the CSV file to load the Rush Hour board.
    """

    vehicles = {}
    with open(fp, "rb") as fileRushhour:
        reader_vehicles = csv.reader(fileRushhour, delimiter=',')
        # iterate over each vehicle in the CSV
        for vehicle in reader_vehicles:
            vehicles[vehicle[1]] = Vehicle(vehicle[0], vehicle[1], int(vehicle[2]), int(vehicle[3]), int(vehicle[4]))

    return Board(shape, shape, round((shape / 2.) - 1), vehicles)

def toString(vehicles):
    """
    Makes a string of the array of vehicles.
    """

    s = ""

    # iterate over each vehicle in the array with vehicles
    for _, vehicle in vehicles.iteritems():
        # store the x-coordinate as a string when direction of vehicle is horizontal
        if vehicle.dir == 'H':
            s += str(vehicle.x)
        # store the y-coordinate as a string when direction of the vehicle is vertical
        if vehicle.dir == 'V':
            s += str(vehicle.y)

    return s

def updateArray (ID, x, y, vehicles):
    """
    Updates the array of vehicles.
    """

    # update the x-coordinate of the vehicle when direction is horizontal
    if vehicles[ID].dir == 'H':
        vehicles[ID].x = x
    # update the y-coordinate of the vehicle when direction is vertical
    elif vehicles[ID].dir == 'V':
        vehicles[ID].y = y

    return vehicles

def BreadthFirstSearch(board):
    """
    Breadth-first search (BFS) is an algorithm for traversing or searching tree
    or graph data structures. It starts at the tree root (or some arbitrary node
    of a graph, sometimes referred to as a 'search key'[1]) and explores the
    neighbor nodes first, before moving to the next level neighbors.

    This algorithm also prints the path to the solution.
    """

    # create archive and hash the beginstate array of vehicles
    archive = {toString(board.vehicles): 0}
    # create queue and and store the beginstate array of vehicles
    queue = Queue.Queue()
    queue.put(board.vehicles)

    # loop untill queue is empty
    while queue.qsize():
        # get the first board of the queue (i.e. parent)
        parent_vehicles = queue.get()
        board.makeBoard(parent_vehicles)
        moves = board.possibleMoves()

        # iterate over each possible move
        for ID, move_list in moves.iteritems():
            # iterate over each x- and y-coordinate of possible move
            for (x, y) in move_list:
                child_vehicles = copy.deepcopy(parent_vehicles)
                child_vehicles = updateArray(ID, x, y, child_vehicles)

                if toString(child_vehicles) in archive:
                    continue

                # hash the parent state with as key the child state
                archive[toString(child_vehicles)] = parent_vehicles
                board.updateBoard(ID, x, y, parent_vehicles)

                if board.isSolution():
                    print "Firework, Champagne, Confetti!"
                    solution_list = []
                    solution_list.append(copy.deepcopy(board))

                    # create crawler as hash of child vehicles
                    crawler = archive[toString(child_vehicles)]

                    # iterate over archive untill the beginstate in the archive
                    # is reached and append the parents of the solution in the
                    # solution list to print the path to the solution
                    while archive[toString(crawler)] != 0:
                        board.makeBoard(crawler)
                        solution_list.append(copy.deepcopy(board))
                        crawler = archive[toString(crawler)]

                    # iterate backwards over de parent boards in solution
                    # list and print the path to the solution
                    for i, boards in enumerate(solution_list[::-1]):
                        print "Move: ", i
                        boards.printBoard()

                    # total moves = i + 2, because the beginstate and moving the
                    # red car to the EXIT are also moves
                    print "Total moves: ", i + 2
                    return

                # add the children of the parent state to the queue
                queue.put(child_vehicles)

                # update the vehicle array and board
                old_x = parent_vehicles[ID].x
                old_y = parent_vehicles[ID].y
                board.updateBoard(ID, old_x, old_y, child_vehicles)

    print "No solution found."

def Random(board):
    """
    Picks a random possible move untill solution is found. When the solution is
    found, this algorithm will search for duplicate boards in the solution list
    and deletes the boards between these duplicates and one of the duplicates
    itself.
    """

    plot_moves = []
    original_board = copy.deepcopy(board)
    iterations = 1

    # loop iterations times
    for i in range(iterations):

        print "Iteration: ", i + 1

        # reset board to original board
        board = copy.deepcopy(original_board)

        total_moves = 0
        total_moves_print = 0
        converted_list = []
        solution_list = [original_board]

        # loop untill the solution of the board is found
        while not board.isSolution():
            moves = board.possibleMoves()

            # convert the dictionary of possible moves to hash the ID of the car at every move
            for ID in range (0, len(moves)):
                for move in range (0, len(moves.values()[ID])):
                    converted_list.append((moves.values()[ID][move], moves.keys()[ID]))

            # pick a random possible move
            random_move, ID = random.choice(converted_list)
            x, y = random_move
            total_moves += 1

            # update board and array after the random move
            board.updateBoard(ID, x, y, board.vehicles)
            board.vehicles = updateArray(ID, x, y, board.vehicles)
            solution_list.append(copy.deepcopy(board))
            converted_list = []

            if board.isSolution():

                # search for duplicates in the solution list and delete every
                # board between duplicates and a duplicate itself
                found = True
                range_i = 0
                while found:
                    found = False
                    for i in range(range_i, len(solution_list)):
                        state1 = toString(solution_list[i].vehicles)
                        range_i = i
                        for j in range(len(solution_list) - 1, range_i, -1):
                            state2 = toString(solution_list[j].vehicles)
                            if state1 == state2:
                                solution_listA = solution_list[:i]
                                solution_listB = solution_list[j:]
                                solution_list = solution_listA + solution_listB
                                found = True
                                break
                        if found:
                            break

                # iterate backwards over de parent boards in solution list
                # to print the path to the solution
                for i, boards in enumerate(solution_list):
                    print "Move: ", i
                    boards.printBoard()
                    total_moves_print += 1
                print total_moves_print, " moves were needed."

                # store the sample of the amount of moves in list plot moves for plotting the histogram
                plot_moves.append(total_moves_print)

    # sort list of moves, so the less amount of moves is plotted first
    plot_moves.sort()
    print plot_moves

    # make a histogram of the random sample
    n, bins, patches = plt.hist(plot_moves, 15, normed=1, facecolor='grey', alpha=0.75)
    plt.show()

def Run_ReversedIterativeDeepeningDepthFirstSearch(board):
    """
    Prepares the variables for running the Iterative Deepening Depth-First
    Search algorithm.
    """

    max_depth = 1000
    solution_list = []
    original = copy.deepcopy(board)

    # loop until the max_depth of -1 is (this is when the beginstate is reached)
    while max_depth != -1:
        max_depth, solution_list = ReversedIterativeDeepeningDepthFirstSearch(board, max_depth, solution_list)
        board = copy.deepcopy(original)

    # print the path of the last found solution by iterating
    # backwards over the boards in the solution list
    board.printBoard()
    i = 0
    for i, boards in enumerate(solution_list[::-1]):
        boards.printBoard()
    # i + 2 moves, because the first move and moving the red car to the exit are also moves
    print i + 2, "moves were needed."

def ReversedIterativeDeepeningDepthFirstSearch(board, max_depth, solution_list):
    """
    Depth-first search (DFS) is an algorithm for traversing or searching tree or
    graph data structures. One starts at the root (selecting some arbitrary node
    as the root in the case of a graph) and explores as far as possible along
    each branch before backtracking.

    Random's Best will be used to set a maximum depth to the Depth-First Search
    algorithm. When the Depth-First Search finds a better solution, the maximum
    depth will be adjust to this solution.
    """

    # create a list as stack and store the beginstate array of vehicles and the depth as tuple
    stack = [(board.vehicles, 0)]
    # create archive and hash the beginstate array of vehicles
    archive = {(toString(board.vehicles),0): 0}

    # loop untill stack is empty
    while len(stack) > 0:

        parent_vehicles, depth = stack.pop()

        if depth >= max_depth:
            continue

        board.makeBoard(parent_vehicles)
        moves = board.possibleMoves()

        # iterate over each possible move
        for ID, move_list in moves.iteritems():
            # iterate over each x- and y-coordinate of possible move
            for (x, y) in move_list:

                child_vehicles = copy.deepcopy(parent_vehicles)
                child_vehicles = updateArray(ID, x, y, child_vehicles)

                if (toString(child_vehicles), depth + 1) in archive:
                    continue

                print "Depth: ", depth, "Stack: ", len(stack), "Archive: ", len(archive), "Max depth: ", max_depth

                # hash the parent state with as key the child state
                archive[(toString(child_vehicles), depth + 1)] = parent_vehicles
                board.updateBoard(ID, x, y, parent_vehicles)

                if board.isSolution():
                    print "Firework, Champagne, Confetti!"
                    solution_list = []
                    solution_list.append(copy.deepcopy(board))

                    # create crawler as hash of child vehicles
                    crawler = archive[(toString(child_vehicles), depth + 1)]

                    # iterate over archive untill the beginstate in the archive
                    # is reached and append the parents of the solution in the
                    # solution list to print the path to the solution
                    while archive[(toString(crawler), depth)] != 0:
                        board.makeBoard(crawler)
                        solution_list.append(copy.deepcopy(board))
                        crawler = archive[(toString(crawler), depth)]
                        depth -= 1

                    return len(solution_list) - 1, solution_list

                # add the children of the parent state to the queue
                stack.append((child_vehicles, depth + 1))

                # update the vehicle array and board
                old_x = parent_vehicles[ID].x
                old_y = parent_vehicles[ID].y
                board.updateBoard(ID, old_x, old_y, child_vehicles)

    print "No solution found."
    return -1, solution_list

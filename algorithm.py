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


def Random(board):
    """
    Picks a random possible move untill solution is found.
    """

    plot_moves = []
    original_board = copy.deepcopy(board)
    iterations = 10

    # loop iterations times
    for i in range(iterations):

        print "Iteration: ", i
        # reset board to original board
        board = copy.deepcopy(original_board)
        # set counter for the amount of moves to 1, because moving the red car to the EXIT is also a move
        total_moves = 1
        converted_list = []
        archive_list = []

        # loop untill the solution of the board is found
        while not board.isSolution():

            moves = board.possibleMoves()

            # loop over every vehicle which can move (using the ID of the vehicle)
            for ID in range (0, len(moves)):
                # loop over every move one vehicle can make
                for move in range (0, len(moves.values()[ID])):
                    # store every single move of the vehicle as tuple in converted list
                    converted_list.append((moves.values()[ID][move], moves.keys()[ID]))

            # pick a random possible move
            random_move, ID = random.choice(converted_list)
            x, y = random_move

            # update board and array after the random move
            board.updateBoard(ID, x, y, board.vehicles)
            board.vehicles = updateArray(ID, x, y, board.vehicles)

            total_moves += 1
            converted_list = []

        if board.isSolution():
            print str(total_moves) + " moves were needed."
            # store the sample of the amount of moves in list plot moves
            plot_moves.append(total_moves)

    # sort list of moves, so the less amount of moves is plotted first
    plot_moves.sort()
    print plot_moves

    # make a histogram of the random sample
    n, bins, patches = plt.hist(plot_moves, 15, normed=1, facecolor='grey', alpha=0.75)
    plt.show()


def DepthFirstSearch(board, max_depth, solution_list):
    """
    Depth-first search (DFS) is an algorithm for traversing or searching tree or
    graph data structures. One starts at the root (selecting some arbitrary node
    as the root in the case of a graph) and explores as far as possible along
    each branch before backtracking.
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

        # reset board with board from the stack
        board.makeBoard(parent_vehicles)
        # get all the possible moves of this board (i.e. all the children)
        moves = board.possibleMoves()

        # iterate over each possible move
        for ID, move_list in moves.iteritems():
            # iterate over each x- and y-coordinate of possible move
            for (x, y) in move_list:
                # make a copy of the parent
                child_vehicles = copy.deepcopy(parent_vehicles)
                # update array after move
                child_vehicles = updateArray(ID, x, y, child_vehicles)

                if (toString(child_vehicles), depth + 1) in archive:
                    continue

                print "Depth: ", depth, "Stack: ", len(stack), "Archive: ", len(archive), "Max depth: ", max_depth

                # hash the parent state with as key the child state
                archive[(toString(child_vehicles), depth + 1)] = parent_vehicles
                # update board after move
                board.updateBoard(ID, x, y, parent_vehicles)

                if board.isSolution():
                    print "Firework, Champagne, Confetti!"

                    # create a list for all the moves to the solution list
                    solution_list = []
                    # append copy of the solution board
                    solution_list.append(copy.deepcopy(board))
                    # create crawler as hash of child vehicles
                    crawler = archive[(toString(child_vehicles), depth + 1)]

                    # iterate over archive untill beginstate is reached
                    while archive[(toString(crawler), depth)] != 0:
                        # make a board of the parent state
                        board.makeBoard(crawler)
                        # store the parent state in the solution list
                        solution_list.append(copy.deepcopy(board))
                        # update crawler
                        crawler = archive[(toString(crawler), depth)]
                        depth -= 1

                    # total moves = i + 2, because the beginstate and moving the red car to the EXIT are also moves
                    return len(solution_list) - 1, solution_list

                # add the children of the parent state to the queue
                stack.append((child_vehicles, depth + 1))

                # update the old x-coordinate
                old_x = parent_vehicles[ID].x
                # update the old y-coordinate
                old_y = parent_vehicles[ID].y
                # update board
                board.updateBoard(ID, old_x, old_y, child_vehicles)

    print "No solution found."
    return -1, solution_list


def BreadthFirstSearch(board):
    """
    Breadth-first search (BFS) is an algorithm for traversing or searching tree
    or graph data structures. It starts at the tree root (or some arbitrary node
    of a graph, sometimes referred to as a 'search key'[1]) and explores the
    neighbor nodes first, before moving to the next level neighbors.
    """

    # create archive and hash the beginstate array of vehicles
    archive = {toString(board.vehicles): 0}
    # create queue and and store the beginstate array of vehicles
    queue = Queue.Queue(board.vehicles)

    # loop untill queue is empty
    while queue.qsize():

        # get the first board of the queue (i.e. parent)
        parent_vehicles = queue.get()
        # reset board with board from the queue
        board.makeBoard(parent_vehicles)
        # get all the possible moves of this board (i.e. all the children)
        moves = board.possibleMoves()

        # iterate over each possible move
        for ID, move_list in moves.iteritems():
            # iterate over each x- and y-coordinate of possible move
            for (x, y) in move_list:
                # make a copy of the parent
                child_vehicles = copy.deepcopy(parent_vehicles)
                # update array after move
                child_vehicles = updateArray(ID, x, y, child_vehicles)

                if toString(child_vehicles) in archive:
                    continue

                # hash the parent state with as key the child state
                archive[toString(child_vehicles)] = parent_vehicles
                # update board after move
                board.updateBoard(ID, x, y, parent_vehicles)

                if board.isSolution():
                    print "Firework, Champagne, Confetti!"

                    # create a list for all the moves to the solution list
                    solution_list = []
                    # append copy of the solution board
                    solution_list.append(copy.deepcopy(board))
                    # create crawler as hash of child vehicles
                    crawler = archive[toString(child_vehicles)]

                    # iterate over archive untill beginstate is reached
                    while archive[toString(crawler)] != 0:
                        # make a board of the parent state
                        board.makeBoard(crawler)
                        # store the parent state in the solution list
                        solution_list.append(copy.deepcopy(board))
                        # update crawler
                        crawler = archive[toString(crawler)]

                    # iterate backwards over de parent boards in solution list
                    for i, boards in enumerate(solution_list[::-1]):
                        # print the number of moves
                        print "s: ", i
                        # print the board
                        boards.printBoard()

                    # total moves = i + 2, because the beginstate and moving the red car to the EXIT are also moves
                    print "Total moves: ", i + 2
                    return

                # add the children of the parent state to the queue
                queue.put(child_vehicles)

                # update the old x-coordinate
                old_x = parent_vehicles[ID].x
                # update the old y-coordinate
                old_y = parent_vehicles[ID].y
                # update board
                board.updateBoard(ID, old_x, old_y, child_vehicles)

    print "No solution found."

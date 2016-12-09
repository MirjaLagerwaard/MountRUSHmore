import copy
import Queue
import random

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

        print "Layer: ", archive[toString(parent_vehicles)], " Archive_len:", len(archive), "Queue_len:", len(queue)

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

def RandomMoves(board):
    """

    """

    total_moves = 1
    new_dict = {}
    archive_list = []
    archive_length = 5
    counter_archive = 0

    while not board.isSolution():

        moves = board.possibleMoves()
        #print moves

        for i in range (0, len(moves)):
            for j in range (0, len(moves.values()[i])):
                new_dict[moves.values()[i][j]] = moves.keys()[i]

        random_move = random.choice(new_dict.keys())
        x, y = random_move
        ID = new_dict[random_move]

        #print random_move

        while [x, y, ID] in archive_list:
            random_move = random.choice(new_dict.keys())
            x, y = random_move
            ID = new_dict[random_move]

        #print new_dict

        archive_list.append([x, y, ID])
        counter_archive += 1

        #print archive_list
        board.updateBoard(ID, x, y, board.vehicles)
        board.vehicles = updateArray(ID, x, y, board.vehicles)
        #board.printBoard()

        total_moves += 1
        print total_moves

        new_dict = {}

        if counter_archive == 5:
            counter_archive = 0
            archive_list = []

    print "Firework, Champagne, Confetti!"
    print total_moves

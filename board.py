from vehicle import *
import copy

class Board(object):
    """
    Rush Hour board.
    """

    def __init__(self, width, height, y_exit, hor_auto, ver_auto):
        """
        Initialize board.
        """

        self.width = width
        self.height = height
        self.y_exit = y_exit
        self.board = [['_'] * self.height for _ in range(self.width)]
        self.hor_auto = hor_auto
        self.ver_auto = ver_auto


    def printBoard(self):
        """
        Prints the board.
        """

        # transpose board to print x and y correctly
        board = [[j[i] for j in self.board] for i in range(len(self.board[0]))]

        # print board
        for element in board:
            print " ".join(element)
        print "\n"

    def toString(self):
        """
        Makes a string of the state of the board.
        """

        s = ""
        for element in board:
            s += "".join(element)
        return s

    def makeBoard(self):
        """
        Makes the beginstate of the board.
        """

        # iterate over each verhicle in list 'hor_auto'
        for ID, vehicle in self.hor_auto.iteritems():
            # set vehicle ID on each position of the vehicle
            for i in range(0, vehicle.size):
                self.board[vehicle.x - i][ vehicle.y] = ID

        # iterate over each verhicle in list 'ver_auto'
        for ID, vehicle in self.ver_auto.iteritems():
            # set vehicle ID on each position of the vehicle
            for i in range(0, vehicle.size):
                self.board[vehicle.x][vehicle.y - i] = ID

        # prints the beginstate of the board
        print "Beginstate"
        self.printBoard()


    def updateBoard(self, ID, x, y):
        """
        Update the board and the hor_auto or ver_auto dict.
        """

        # iterate over each x- and y-coordinate of the board
        for x_board in range(self.width):
            for y_board in range(self.height):
                # remove the vehicle from the old position on the board
                if self.board[x_board][y_board] == ID:
                    self.board[x_board][y_board] = '_'

        # update x-coordinate for horizontal car
        if ID in self.hor_auto:
            self.hor_auto[ID].x = x

            for i in range(self.hor_auto[ID].size):
                self.board[x - i][y] = ID

        # update y-coordinate for vertical car
        elif ID in self.ver_auto:
            self.ver_auto[ID].y = y

            for i in range(self.ver_auto[ID].size):
                self.board[x][y - i] = ID

        # # prints the board with the vehicle on his new position
        # self.printBoard()


    def possibleMoves(self):
        """
        Returns all possible moves of a specific state of the board as a dict.
        """

        children = {}

        # MOVEMENT OF HORIZONTAL CARS
        # iterate over each vehicle in list 'hor_auto'
        for ID, vehicle in self.hor_auto.iteritems():
            # iterate over each possible x-position untill RIGHT wall is reached
            for i in range(vehicle.x + 1, self.width):
                # check if position in front of vehicle is empty
                if self.board[i][vehicle.y] == "_":
                    # store the coordinates as a tuple
                    coordinate = (i, vehicle.y)
                    # hash the possible child to the dict 'children'
                    if ID in children:
                        children[ID].append(coordinate)
                    else:
                        children[ID] = [coordinate]
                # vehicle is not alowed to move, a car or truck is in his way
                else:
                    break

            # iterate over each possible x-position untill LEFT wall is reached
            for i in range(vehicle.x - 1, vehicle.size - 2, -1):
                # check if position in front of vehicle is empty
                if self.board[i - (vehicle.size - 1)][vehicle.y] == "_":
                    # store the coordinates as a tuple
                    coordinate = (i, vehicle.y)
                    # hash the possible child to the dict 'children'
                    if ID in children:
                        children[ID].append(coordinate)
                    else:
                        children[ID] = [coordinate]
                # vehicle is not alowed to move, a car or truck is in his way
                else:
                    break

        # MOVEMENT OF VERTICAL CARS
        # iterate over each vehicle in list 'ver_auto'
        for ID, vehicle in self.ver_auto.iteritems():
            # iterate over each possible y-position untill LOWER wall is reached
            for i in range(vehicle.y + 1, self.height):
                # check if position in front of vehicle is empty
                if self.board[vehicle.x][i] == "_":
                    # store the coordinates as a tuple
                    coordinate = (vehicle.x, i)
                    # hash the possible child to the dict 'children'
                    if ID in children:
                        children[ID].append(coordinate)
                    else:
                        children[ID] = [coordinate]
                # vehicle is not alowed to move, a car or truck is in his way
                else:
                    break

            # iterate over each possible y-position untill UPPER wall is reached
            for i in range(vehicle.y - 1, vehicle.size - 2, -1):
                # check if position in front of vehicle is empty
                if self.board[vehicle.x][i - (vehicle.size - 1)] == "_":
                    # store the coordinates as a tuple
                    coordinate = (vehicle.x , i)
                    # hash the possible child to the dict 'children'
                    if ID in children:
                        children[ID].append(coordinate)
                    else:
                        children[ID] = [coordinate]
                # vehicle is not alowed to move, a car or truck is in his way
                else:
                    break

        # return the dict 'children' with all the possible moves of each vehicle
        return children

    def isSolution(self):
        """
        Returns true when red car can drive through the EXIT.
        """

        # iterate over each vehicle in list 'hor_auto'
        for _, vehicle in self.hor_auto.iteritems():
            # if the y-coordinate of the vehicle is equal to the y-coordinate of the EXIT
            if self.y_exit == vehicle.y:
                # iterate over each x-coordinate
                for i in range(vehicle.x + 1, self.width):
                    # check if the way to the EXIT is free
                    if self.board[i][vehicle.y] != "_":
                        return False
                return True


    def BreadthFirstSearch(self):
        """
        Breadth-first search (BFS) is an algorithm for traversing or searching
        tree or graph data structures. It starts at the tree root (or some
        arbitrary node of a graph, sometimes referred to as a 'search key'[1])
        and explores the neighbor nodes first, before moving to the next level
        neighbors.
        """
        # make the archive (as a dict) and the queue (as a list)
        archive = {self.toString(): 0}
        queue = [self]

        # while there are items in the queue
        while queue:
            # pop the first item of the queue (FIFO: first in, first out)
            parent_state = queue.pop(0)

            # get all the possible moves of this parent state, i.e. the children
            moves = parent_state.possibleMoves()

            # iterate over each possible move
            for ID, move_list in moves.iteritems():
                # iterate over each x- and y-coordinate
                for (x, y) in move_list:
                    # make a copy of the child state
                    child_state = copy.deepcopy(parent_state)

                    # update board
                    child_state.updateBoard(ID, x, y)
                    print len(archive)

                    # if the child is in the archive, break out of loop
                    if child_state.toString() in archive:
                        break
                    # if the child is the solution, print party and how many moves were needed, and return
                    elif child_state.isSolution():
                        print "Firework, Champagne, Confetti!"
                        print str(archive[parent_state.toString()] + 2) + " moves were needed."
                        return

                    # add the child state to archive and report the depth of the graph
                    archive[child_state.toString()] = archive[parent_state.toString()] + 1

                    # add the children of the parent state to the queue
                    queue.append(child_state)

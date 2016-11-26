import pprint
import numpy as np

class Board(object):
    """
    TODO
    """
    def __init__(self, width, height, y_exit):
        """
        Initialize board.
        """

        self.width = width
        self.height = height
        self.y_exit = y_exit
        self.board = [['_'] * self.height for _ in range(self.width)]

    def printBoard(self):
        """
        Prints the board.
        """

        # transpose board to print x and y correctly
        board = [[j[i] for j in self.board] for i in range(len(self.board[0]))]

        # print board
        for element in board:
            print " ".join(element)

    def makeBoard(self, hor_auto, ver_auto):
        """
        Makes the beginstate of the board.
        """

        # iterate over each verhicle in list 'hor_auto'
        for ID, vehicle in hor_auto.iteritems():
            # set vehicle ID on each position of the vehicle
            for i in range(0, vehicle.size):
                self.board[vehicle.x - i][ vehicle.y] = ID

        # iterate over each verhicle in list 'ver_auto'
        for ID, vehicle in ver_auto.iteritems():
            # set vehicle ID on each position of the vehicle
            for i in range(0, vehicle.size):
                self.board[vehicle.x][vehicle.y - i] = ID

        # prints the beginstate of the board
        self.printBoard()

    def updateBoard(self, hor_auto, ver_auto, ID, x, y):
        """
        Update the board and the hor_auto or ver_auto dict.
        """

        # iterate over each x- and y-coordinate of the board
        for x_board in range(self.width - 1):
            for y_board in range(self.height - 1):
                # remove the vehicle from the old position on the board
                if self.board[x_board][y_board] == ID:
                    self.board[x_board][y_board] = '_'

        # update x-coordinate for horizontal car
        if ID in hor_auto:
            hor_auto[ID].x = x

            self.board[x][y] = ID
            self.board[x - 1][y] = ID

        # update y-coordinate for vertical car
        elif ID in ver_auto:
            ver_auto[ID].y = y

            self.board[x][y] = ID
            self.board[x][y - 1] = ID

        # prints the board with the vehicle on his new position
        self.printBoard()

    def possibleMoves(self, hor_auto, ver_auto):
        """
        Returns all possible moves of a specific state of the board as a dict.
        """

        children = {}

        # MOVEMENT OF HORIZONTAL CARS
        # iterate over each vehicle in list 'hor_auto'
        for ID, vehicle in hor_auto.iteritems():
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
            for i in range (vehicle.x - 1, vehicle.size - 2, -1):
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
        for ID, vehicle in ver_auto.iteritems():
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
            for i in range (vehicle.y - 1, vehicle.size - 2, -1):
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

    def isSolution(self, hor_auto):
        """
        Returns true when red car is at the EXIT
        """
        # iterate over each vehicle in list 'hor_auto'
        for _, vehicle in hor_auto.iteritems():
            # if the y-coordinate of the vehicle is the y-coordinate of the EXIT
            if self.y_exit == vehicle.y:
                # and if the x-coordinate of the vehicle is at the EXIT
                if vehicle.x == self.width - 1:
                    # we found the solution, return true
                    return True


    def BreadthFirstSearch(board):
        """
        TODO
        """

        #1 voeg de array childs toe aan de queue
        #2 als de array leeg is
            # return geen oplossing
        #3 anders pak eerste item van de queue
            #4 is het item de oplossing (call functie isSolution)?
                #JA:
                    # stop en return
                #NEE:
                    #5 is het item aanwezig in het archief?
                        #JA:
                            # ga naar 2
                        #NEE:
                            # maak alle kinderen van het item (call functie moves)
                            # ga naar 1

class Vehicle(object):
    """
    TODO
    """
    def __init__(self, direction, ID, x, y, size):
        self.dir = direction
        self.x = x
        self.y = y
        self.size = size
        self.ID = ID

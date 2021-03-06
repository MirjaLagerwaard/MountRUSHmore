from vehicle import *

class Board(object):
    """
    Rush Hour board.
    """

    def __init__(self, width, height, y_exit, vehicles):
        """
        Initialize board.
        """

        self.width = width
        self.height = height
        self.y_exit = y_exit
        self.makeBoard(vehicles)

    def printBoard(self):
        """
        Print board.
        """
        # transpose board to print x and y correctly
        board = [[j[i] for j in self.board] for i in range(len(self.board[0]))]

        # print board
        for element in board:
            print " ".join(element)
        print "\n"

    def makeBoard(self, new_vehicles):
        """
        Makes the beginstate of the board.
        """
        self.vehicles = new_vehicles
        self.board = [['_'] * self.height for _ in range(self.width)]

        # iterate over each verhicle in list 'hor_auto'
        for ID, vehicle in new_vehicles.iteritems():
            if vehicle.dir == 'H':
                # set vehicle ID on each position of the vehicle
                for i in range(0, vehicle.size):
                    self.board[vehicle.x - i][vehicle.y] = ID
            if vehicle.dir == 'V':
            # set vehicle ID on each position of the vehicle
                for i in range(0, vehicle.size):
                    self.board[vehicle.x][vehicle.y - i] = ID

    def updateBoard(self, ID, x, y, old_vehicles):
        """
        Update the board and the vehicles array.
        """

        # update the x-coordinate for the horizontal cars
        if old_vehicles[ID].dir == 'H':
            for i in range(old_vehicles[ID].size):
                self.board[old_vehicles[ID].x - i][old_vehicles[ID].y] = '_'
            for i in range(old_vehicles[ID].size):
                self.board[x - i][y] = ID

        #update the y-coordinate for the vertical cars
        if old_vehicles[ID].dir == 'V':
            for i in range(old_vehicles[ID].size):
                self.board[old_vehicles[ID].x][old_vehicles[ID].y - i] = '_'
            for i in range(old_vehicles[ID].size):
                self.board[x][y - i] = ID

    def possibleMoves(self):
        """
        Returns all possible moves of a specific state of the board as a dict.
        """

        children = {}


        # iterate over each vehicle in array with vehicles
        for ID, vehicle in self.vehicles.iteritems():

            # movement of horizontal cars
            if vehicle.dir == 'H':
                # iterate over each possible x-position untill RIGHT wall is reached
                for i in range(vehicle.x + 1, self.width):
                    if self.board[i][vehicle.y] == "_":
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
                for i in range(vehicle.x - vehicle.size, -1, -1):
                    if self.board[i][vehicle.y] == "_":
                        coordinate = (i + vehicle.size - 1, vehicle.y)
                        # hash the possible child to the dict 'children'
                        if ID in children:
                            children[ID].append(coordinate)
                        else:
                            children[ID] = [coordinate]
                    # vehicle is not alowed to move, a car or truck is in his way
                    else:
                        break

            # movement of vertical cars
            elif vehicle.dir == 'V':
                # iterate over each possible y-position untill LOWER wall is reached
                for i in range(vehicle.y + 1, self.height):
                    if self.board[vehicle.x][i] == "_":
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
                for i in range(vehicle.y - vehicle.size, -1, -1):
                    if self.board[vehicle.x][i] == "_":
                        coordinate = (vehicle.x , i + vehicle.size - 1)
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
        for i in range(self.vehicles['#'].x + 1, self.width):
            # check if the way to the EXIT is free
            if self.board[i][self.vehicles['#'].y] != "_":
                return False
        return True

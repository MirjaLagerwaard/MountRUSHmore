import pprint

class Board(object):
    """
    TODO
    """
    def __init__(self, width, height, y_exit):
        """
        TODO
        """
        self.width = width
        self.height = height
        self.y_exit = y_exit

    def makeBoard(self, hor_auto, ver_auto):
        """
        TODO
        """

        board = [['_' for j in range(self.height)] for i in range(self.width)]

        for vehicle in hor_auto:
            for i in range(0, int(vehicle.size)):
                board[int(vehicle.y)][int(vehicle.x) - i] = vehicle.ID
        for vehicle in ver_auto:
            for i in range(0, int(vehicle.size)):
                board[int(vehicle.y) - i][int(vehicle.x)] = vehicle.ID

        for element in board:
            print (" ".join(element))

    def moves(self, width, height, position):
        """
        TODO
        """

        childs = []

        """
        Movement of horizontal cars TO RIGHT
        """

        # iterate over each x-position on board until wall is reached
        for x_pos in hor_auto(Vehicle.getX(), (self.width - 1), 1):
            # check if position in front of vehicle is empty
            if board[Vehicle.getX() + 1, Vehicle.getY()] == "_":
                childs.append(board)
            # vehicle is nou aloud to move, a car or truck is in his way
            else:
                break

        """
        Movement of horizontal vehicles TO LEFT
        """

        # iterate over each x-position on board until wall is reached
        for x_pos in hor_auto(Vehicle.getX(), (self.size - 1), -1):
            # check backwards moving if vehicle is a car
            if self.size == '2':
                if board[Vehicle.getX() - 2, Vehicle.getY()] == "_":
                    childs.append(board)
                # vehicle is nou aloud to move, a car or truck is in his way
                else:
                    break
            # check backwards moving if vehicle is a truck
            elif self.size == '3':
                if board[Vehicle.getX() - 3, Vehicle.getY()] == "_":
                    childs.append(board)
                # vehicle is not alowed to move, a car or truck is in his way
                else:
                    break

        """
        Movement of vertical vehicles DOWNWARDS
        """

        # iterate over each y-position on board until wall is reached
        for y_pos in ver_auto(Vehicle.getY(), (self.height - 1), 1):
            # check if position in front of vehicle is empty
            if (board[Vehicle.getX(), Vehicle.getY() + 1] == "_"):
                childs.append(board)
            # vehicle is now alowed to move, a car or truck is in his way
            else:
                break

        """
        Movement of vertical vehicles UPWARDS
        """

        # iterate over each y-position on board until wall is reached
        for y_pos in ver_auto(Vehicle.getY(), (self.size - 1), -1):
            # check backwards moving if vehicle is a car
            if self.size == '2':
                if board[Vehicle.getX() - 2, Vehicle.getY()] == "_":
                    childs.append(board)
                # vehicle is now alowed to move, a car or truck is in his way
                else:
                    break
            # check backwards moving if vehicle is a truck
            elif self.size == '3':
                if board[Vehicle.getX() - 3, Vehicle.getY()] == "_":
                    childs.append(board)
                # vehicle is nou alowed to move, a car or truck is in his way
                else:
                    break

        return childs

    def isSolution(self):
        """
        Returns true when red car is at the EXIT
        """
        for verhicles in hor_auto:
            if self.y_exit == Vehicle.getY():
                if Vehicle.getX() == self.width - 1:
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

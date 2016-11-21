import pprint
from vehicle import *

class Board(object):
    """
    TODO
    """
    def __init__(self, width, height):
        """
        TODO
        """
        self.width = width
        self.height = height

    def isPositiononBoard(self, pos):
        """
        TODO
        """
        return 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height)

    def moves(self, width, height, position):
        """
        TODO
        """

        """"
        Movement of horizontal cars TO RIGHT
        """"

        # iterate over each x-position on board until wall is reached
        for x_pos in hor_auto(Vehicle.getX(), (self.width - 1), 1):
            # check if position in front of vehicle is empty
            if (board[Vehicle.getX() + 1, Vehicle.getY()] == "."):
                return child
            # vehicle is nou aloud to move, a car or truck is in his way
            else:
                break

        """"
        Movement of horizontal vehicles TO LEFT
        """"

        # iterate over each x-position on board until wall is reached
        for x_pos in hor_auto(Vehicle.getX(), (self.size - 1), -1):
            # check backwards moving if vehicle is a car
            if (self.size == '2'):
                if (board[Vehicle.getX() - 2, Vehicle.getY()] == "."):
                    return child
                # vehicle is nou aloud to move, a car or truck is in his way
                else:
                    break
            # check backwards moving if vehicle is a truck
            elif (self.size == '3'):
                if (board[Vehicle.getX() - 3, Vehicle.getY()] == "."):
                    return child
                # vehicle is nou aloud to move, a car or truck is in his way
                else:
                    break

        """"
        Movement of vertical vehicles DOWNWARDS
        """"

        for y_pos in ver_auto(Vehicle.getY(), (self.height - 1), 1):
            # check if position in front of vehicle is empty
            if (board[Vehicle.getX(), Vehicle.getY() + 1] == "."):
                return child
            # vehicle is nou aloud to move, a car or truck is in his way
            else:
                break

        """"
        Movement of vertical vehicles UPWARDS
        """"

        # iterate over each x-position on board until wall is reached
        for y_pos in ver_auto(Vehicle.getY(), (self.size - 1), -1):
            # check backwards moving if vehicle is a car
            if (self.size == '2'):
                if (board[Vehicle.getX() - 2, Vehicle.getY()] == "."):
                    return child
                # vehicle is nou aloud to move, a car or truck is in his way
                else:
                    break
            # check backwards moving if vehicle is a truck
            elif (self.size == '3'):
                if (board[Vehicle.getX() - 3, Vehicle.getY()] == "."):
                    return child
                # vehicle is nou aloud to move, a car or truck is in his way
                else:
                    break

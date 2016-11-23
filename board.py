import pprint
from vehicle import *

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
        self.board = [self.width][self.height]

    def updateBoard(self, vehicles):
        """
        TODO
        """




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
            if (board[Vehicle.getX() + 1, Vehicle.getY()] == "."):
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
            if (self.size == '2'):
                if (board[Vehicle.getX() - 2, Vehicle.getY()] == "."):
                    childs.append(board)
                # vehicle is nou aloud to move, a car or truck is in his way
                else:
                    break
            # check backwards moving if vehicle is a truck
            elif (self.size == '3'):
                if (board[Vehicle.getX() - 3, Vehicle.getY()] == "."):
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
            if (board[Vehicle.getX(), Vehicle.getY() + 1] == "."):
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
            if (self.size == '2'):
                if (board[Vehicle.getX() - 2, Vehicle.getY()] == "."):
                    childs.append(board)
                # vehicle is now alowed to move, a car or truck is in his way
                else:
                    break
            # check backwards moving if vehicle is a truck
            elif (self.size == '3'):
                if (board[Vehicle.getX() - 3, Vehicle.getY()] == "."):
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

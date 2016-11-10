import pprint

board = []
#
for row in range(9):
    board.append([])
    for column in range(9):
        board[row].append('.')

for element in board:
    print (" ".join(element))


class Board(object):
    """
    Comments
    """
    def __init__(self, width, height):
        """
        Comments
        """
        self.width = width
        self.height = height

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.
        returns: True if pos is in the room, False otherwise.
        """
        if (0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height):
            return True
        return False

    def collisionCar(self, pos):
        """
        Returns True if there is a collision with a car.
        """
        if (position + 1 || position - 2 !== empty)
            return True
        return False


class horizontalAuto(object):
    """
    Comments
    """
    def __init__(self):
        self.position = (x,y) van neus auto
        self.direction = horizontal (vast y-coordinaat)
        self.size = 2

class verticalAuto(object):
    """
    Comments
    """
    def __init__(self):
        self.position = (x,y) van neus auto
        self.direction = vertical (vaste x-coordinaat)
        self.size = 2

class horizontalTruck(object):
    """
    Comments
    """
    def __init__(self):
        self.position = (x,y) van neus truck
        self.direction = horizontal (vast y-coordinaat)
        self.size = 3

class verticalTruck(object):
    """
    Comments
    """
    def __init__(self)
        self.position = (x,y) van neus truck
        self.direction = vertical (vaste x-coordinaat)
        self.size = 3

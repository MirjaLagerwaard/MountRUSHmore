class Vehicle(object):
    """
    Vehicles for on Rush hour board.
    """

    def __init__(self, direction, ID, x, y, size):
        """
        Initialize vehicles.
        """
        self.dir = direction
        self.x = x
        self.y = y
        self.size = size
        self.ID = ID

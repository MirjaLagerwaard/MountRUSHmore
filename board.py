import pprint

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

    def Moves(self, width, height, position):
        """
        TODO
        """

        # movement of horizontal cars FORWARD
        for pos in hor_auto(Vehicle.getX(), (self.width - 1)):
            if (Vehicle.get(X) + 1 == ".")
                if (isPositiononBoard(Vehicle.get(X) + 1) == True)



            # Kan mijn auto hier staan?
            # Ja:
            #     Dit is een child! voeg toe aan de queue
            # Nee:
            #     Dit is geen child EN stop met checken achteruit gaan (break)


        # movement of horizontal cars BACKWARDS
        for pos in hor_auto(Vehicle.getX(), (self.size - 1), -1):
            # Kan mijn auto hier staan?
            # Ja:
            #     Dit is een child! voeg toe aan de queue
            # Nee:
            #     Dit is geen child EN stop met checken achteruit gaan (break)

        # movement of vertical cars FORWARD
            # Kan mijn auto hier staan?
            # Ja:
            #     Dit is een child! voeg toe aan de queue
            # Nee:
            #     Dit is geen child EN stop met checken achteruit gaan (break)


        # movement of vertical cars BACKWARDS
            # Kan mijn auto hier staan?
            # Ja:
            #     Dit is een child! voeg toe aan de queue
            # Nee:
            #     Dit is geen child EN stop met checken achteruit gaan (break)

        return queue


            for (i = 0; i < min x-coordinaat; i++)
                if (size == 2)
                    if (x.coordinaat auto - 2 == ".")
                        if (position x-2 binnen het board valt)
                            remove auto van board
                            set auto op x-2
                if (size == 3)
                    if (x.coordinaat auto - 3 == ".")
                        if (position x-3 binnen het board valt)
                            remove auto van board
                            set auto op x-3

            Voor alle horizontale autos:
                Voor alle posities vooruit: (geteld vanaf de auto)
                    Kan mijn auto hier staan?
                    Ja:
                        Dit is een child! voeg toe aan de queue
                    Nee:
                        Dit is geen child EN stop met checken vooruit gaan (break)

                Voor alle posities achteruit: (geteld vanaf de auto)
                    Kan mijn auto hier staan?
                    Ja:
                        Dit is een child! voeg toe aan de queue
                    Nee:
                        Dit is geen child EN stop met checken achteruit gaan (break)

            return queue


class Vehicle(object):
    """
    TODO
    """
    def __init__(self, room, position, direction, size):
        self.room = room
        self.dir = direction
        self.pos = position
        self.size = size

# board = []
# #
# for row in range(9):
#     board.append([])
#     for column in range(9):
#         board[row].append('.')
#
# for element in board:
#     print (" ".join(element))

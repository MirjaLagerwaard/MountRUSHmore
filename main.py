from board import *
from vehicle import *

def BreadthFirstSearch(self):
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

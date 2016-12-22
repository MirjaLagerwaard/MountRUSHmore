import sys
from algorithm import *

if __name__ == "__main__":

    # Error when the user did not give the right amount of arguments
    if len(sys.argv) <= 1 or len(sys.argv) > 3:
        print "Usage: python main.py <6_1/6_2/6_3/9_1/9_2/9_3/12> <breadth/depth/random>"
        exit()

    # update fp to the CSV file the user asked for
    if sys.argv[1] == "6_1":
        fp = "vehicles_6x6_1.csv"
        shape = 6
    elif sys.argv[1] == "6_2":
        fp = "vehicles_6x6_2.csv"
        shape = 6
    elif sys.argv[1] == "6_3":
        fp = "vehicles_6x6_3.csv"
        shape = 6
    elif sys.argv[1] == "9_1":
        fp = "vehicles_9x9_1.csv"
        shape = 9
    elif sys.argv[1] == "9_2":
        fp = "vehicles_9x9_2.csv"
        shape = 9
    elif sys.argv[1] == "9_3":
        fp = "vehicles_6x6_3.csv"
        shape = 9
    elif sys.argv[1] == "12":
        fp = "vehicles_12x12.csv"
        shape = 12
    else:
        print "Usage: python main.py <6_1/6_2/6_3/9_1/9_2/9_3/12> <breadth/depth/random>"
        exit()

    # prepare the CSV file before running an algorithm
    board = PrepareFile(fp, shape)

    # run the algorithm the user asked for
    if sys.argv[2] == "breadth":
        BreadthFirstSearch(board)
    elif sys.argv[2] == "depth":
        Run_ReversedIterativeDeepeningDepthFirstSearch(board)
    elif sys.argv[2] == "random":
        Random(board)
    else:
        print "Usage: python main.py <6_1/6_2/6_3/9_1/9_2/9_3/12> <breadth/depth/random>"
        exit()

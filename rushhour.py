# class Board(object):
#     """
#     Comment
#     """
#     def __init__(self, x, y):
#         """
#         Comment
#         """
import pprint

board = []
#
for row in range(9):
    board.append([])
    for column in range(9):
        board[row].append('.')

for element in board:
    print (" ".join(element))




# print board
# for row in board:
#     # Loop over columns.
#     for column in row:
#         print(column, end="")
#     print(end="\n")

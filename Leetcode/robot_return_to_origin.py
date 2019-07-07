from functools import reduce

def rate_move(move: str):
    if(move == 'L'):
        return (-1,0)
    elif(move == 'R'):
        return (1,0)
    elif(move == 'U'):
        return (0,-1)
    else:
        return (0,1)

def add_coords(coord1, coord2):
    return (coord1[0] + coord2[0], coord1[1] + coord2[1])

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        rated_moves = [rate_move(move) for move in moves]
        final_coords = reduce(add_coords, rated_moves)
        if final_coords == (0,0):
            return True
        else:
            return False

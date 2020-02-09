from unification import var
from kanren import run
from kanren.core import everyg
from kanren.goals import permuteq
from numpy import array

DIGITS = tuple(range(1, 10))

def get_rows(sb):
    rows = tuple(tuple(sb[i]) for i in range(0, 9))
    return rows

def get_cols(sb):
    cols = tuple(tuple(sb[:,i]) for i in range(0, 9))
    return cols

def get_squares(sb):
    sq = tuple(tuple(sb[r:r+3,c:c+3].flatten()) for r in range(0, 9, 3) for c in range(0, 9, 3))
    return sq

def test(set):
    return permuteq(set, DIGITS)

def validate(sb):
    rows = get_rows(sb)
    cols = get_cols(sb)
    squares = get_squares(sb)
    x = var('x')
    return run(0, x, everyg(test, rows), everyg(test, cols), everyg(test, squares))

board = array([[4,3,5,2,6,9,7,8,1],
               [6,8,2,5,7,1,4,9,3],
               [1,9,7,8,3,4,5,6,2],
               [8,2,6,1,9,9,3,4,7],
               [3,7,4,6,8,2,9,1,5],
               [9,5,1,7,4,3,6,2,8],
               [5,1,9,3,2,6,8,7,4],
               [2,4,8,9,5,7,1,3,6],
               [7,6,3,4,1,8,2,5,9]]);

result = validate(board)
valid = "Board is correct"
invalid = "Board is not correct"
if len(result) == 0:
    print(valid)
else:
    print(invalid)

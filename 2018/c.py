import sys

def build_square(centre):
    results = set()
    while (len(results) < 9):
        result = dig(2,centre)
        if result == (0, 0):
            return True #true
        elif result == (-1, -1):
            sys.exit(0) #somehow we made a mistake
        else:
            results.add(result)
    return False #not finished yet

def build_single_col(centre):
    results = set()
    while(len(results) < 3):
        result = dig(2, centre)
        if result == (0, 0):
            return True
        elif result == (-1, -1):
            sys.exit(0)
        elif result[1] > centre:
            results.add(result)
    return False

def build_double_col(centre):
    results = set()
    while(len(results) < 6):
        result = dig(2, centre)
        if result == (0, 0):
            return True
        elif result == (-1, -1):
            sys.exit(0)
        elif result[1] >= centre:
            results.add(result)
    return False


def dig(row, col):
    print(row, col)
    sys.stdout.flush()
    return tuple(map(int,input().split()))

def solve_case(c, a):
    h = 3
    w = a // h + 1
    squares, extras = divmod(w, h)
    if squares < 0:
        squares, extras = 1, 0

    for s in range(squares):
        if build_square(2 + (s*3)):
            break
    else:
        if extras == 1:
            build_single_col(w-1)
        elif extras == 2:
            build_double_col(w-1)

if __name__ == "__main__":
    t = int(input())
    for c in range(t):
        a = int(input())
        solve_case(c, a)

import numpy as np
import random

input = [val for val in open('day9.txt').read().strip('\n').split()]

cols = len(input[0])
rows = len(input)

A = np.zeros((rows,cols))

for idx,line in enumerate(input):
    A[idx] = [num for num in line]

def get_basin_size(row,col):
    rp = row
    cp = col
    A[rp,cp] = -1

    # the blind mouse algorithm
    # todo: read up on BFS
    size = 1
    for _ in range(10000):
        dir = random.randint(0,3)
        if dir == 0 and not check_right(rp,cp):
            cp += 1
            if A[rp,cp] != -1:
                size += 1
                A[rp,cp] = -1
        elif dir == 1 and not check_left(rp,cp):
            cp -= 1
            if A[rp,cp] != -1:
                size += 1
                A[rp,cp] = -1        
        elif dir == 2 and not check_down(rp,cp):
            rp += 1
            if A[rp,cp] != -1:
                size += 1
                A[rp,cp] = -1
        elif dir == 3 and not check_up(rp,cp):
            rp -= 1
            if A[rp,cp] != -1:
                size += 1
                A[rp,cp] = -1

    return size
    
risk = 0

def check_right(row,col):
    isWall = True
    if col < cols-1: # check right
        isWall = A[row][col+1] == 9
    return isWall

def check_left(row,col):
    isWall = True
    if col > 0: # check left
        isWall = A[row][col-1] == 9
    return isWall

def check_up(row,col):
    isWall = True
    if row > 0: # check above
        isWall = A[row-1][col] == 9
    return isWall

def check_down(row,col):
    isWall = True
    if row < rows-1: # check below
        isWall = A[row+1][col] == 9
    return isWall

sizes = []
for row,line in enumerate(A):
    for col,val in enumerate(line):
        isMin = True
        if row > 0: # check above
            isMin = A[row-1][col] > val
        if col > 0 and isMin: # check left
            isMin = A[row][col-1] > val
        if row < rows-1 and isMin: # check below
            isMin = A[row+1][col] > val
        if col < cols-1 and isMin: # check right
            isMin = A[row][col+1] > val
        if isMin:
            risk += 1+val
            size = get_basin_size(row,col)
            sizes.append(size)

sorted_sizes = sorted(sizes,reverse = True)
p2 = 1
for val in sorted_sizes[:3]:
    p2 *= val

print(f"p1: {int(risk)} p2: {p2}")


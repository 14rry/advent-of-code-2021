from collections import Counter

with open('day5.txt') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]
points = []

def populate_points(p,all_points):

    x1 = p[0]
    x2 = p[2]
    y1 = p[1]
    y2 = p[3]
    
    if x1 > x2:
        xdir = -1
    else:
        xdir = 1

    if y1 > y2:
        ydir = -1
    else:
        ydir = 1

    # uncomment to get part 1 answer
    # if not ((x1 == x2) or (y1 == y2)):
    #    return all_points # return without doing anything, ignore diagonals for part 1

    x_list = [_ for _ in range(x1,x2+xdir,xdir)]
    y_list = [_ for _ in range(y1,y2+ydir,ydir)]

    if len(x_list) == 1:
        x_list = [x_list[0]] * len(y_list)
    elif len(y_list) == 1:
        y_list = [y_list[0]] * len(x_list)

    for i,val in enumerate(x_list):
        all_points.append((val,y_list[i]))

    return all_points    

# parse input
for line in lines:
    line = line.replace(' -> ',',')
    temp = line.split(',')
    temp = [int(val) for val in temp]
    points = populate_points(temp,points)

cpoints = Counter(points)
answer = 0
for c in cpoints.values():
    if c >= 2:
        answer += 1

print(answer)

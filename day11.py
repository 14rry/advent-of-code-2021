lines = [[int(val) for val in line] for line in open('day11.txt').read().strip().split()]
# for idx,line in enumerate(lines):
#     new_line = []
#     for c in line:
#         new_line.append(int(c))
#     lines[idx] = new_line

total_flashes = 0
R = len(lines)
C = len(lines[0])

# directions to check all neighbors, including diagonals
DR = [-1,-1,-1,0,1,1,1,0]
DC = [-1,0,1,1,1,0,-1,-1]

step = 0
all_flashed = False
while (not all_flashed) or step < 100:
    # step 1, everyone increases by 1
    for r,line in enumerate(lines):
        for c,val in enumerate(line):
            lines[r][c] += 1

    # step 2, > 9 flashes
    did_flash = True
    flash = [[0] * R for _ in range(C)]
    while did_flash:
        did_flash = False
        for r,line in enumerate(lines):
            for c,val in enumerate(line):
                if val > 9 and flash[r][c] == 0: #flash
                    did_flash = True
                    total_flashes += 1
                    flash[r][c] = 1
                    for rr,cc in zip(DR,DC):
                        rr = rr + r
                        cc = cc + c
                        if 0<=rr<R and 0<=cc<C:
                            lines[rr][cc] += 1

    # step 3, all flashes go to 0
    all_flashed = True
    for r,line in enumerate(flash):
        for c,val in enumerate(line):
            if val == 1:
                lines[r][c] = 0
            else:
                all_flashed = False

    if all_flashed:
        p2 = step+1 # part 2 answer

    step += 1
    if step == 100:
        p1 = total_flashes # part 1 answer

print(f"p1: {p1} p2: {p2}")

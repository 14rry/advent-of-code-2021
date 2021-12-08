
fishs = [3,4,3,1,2]

with open('day6.txt') as f:
    fishs = f.readlines()
    fishs = [fish.strip('\n') for fish in fishs]
    fishs = fishs[0].split(',')
    fishs = [int(fish) for fish in fishs]

for day in range(80):
    for idx,fish in enumerate(fishs):
        if fish == 0:
            fishs.append(9)
            fishs[idx] = 6
        else:
            fishs[idx] = fish-1

print(len(fishs))
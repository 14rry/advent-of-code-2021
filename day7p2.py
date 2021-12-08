import statistics

crabs = [16,1,2,0,4,2,7,1,2,14]

crabs = [int(val) for val in open('day7.txt').read().strip().split(',')]

round_mean = round(statistics.mean(crabs))

guesses = range(round_mean-1,round_mean+1) # try +/- 1 because rounding isn't perfect solution
all_fuels = []

for round_mean in guesses:

    fuel = 0
    for crab in crabs:
        delta = crab-round_mean
        cost = 0
        for i in range(abs(delta)+1):
            fuel += cost
            cost += 1

    all_fuels.append(fuel)

print(min(all_fuels)) # the answer
index_min = min(range(len(all_fuels)), key=all_fuels.__getitem__)
print(guesses[index_min]) # the delta that provided the min fuel


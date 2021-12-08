import statistics

crabs = [16,1,2,0,4,2,7,1,2,14]

crabs = [int(val) for val in open('day7.txt').read().strip().split(',')]

med = statistics.median(crabs)
print(med)

fuel = 0
for crab in crabs:
    fuel += abs(crab-med)

print(fuel)
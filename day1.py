with open('day1.txt') as f:
	lines = f.readlines()

vals = [int(line) for line in lines]
p1 = sum( a < b for (a,b) in zip(vals,vals[1:]))
p2 = sum( a < b for (a,b) in zip(vals,vals[3:]))

print(f"p1: {p1} p2: {p2}")

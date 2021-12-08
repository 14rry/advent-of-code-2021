with open('day2.txt') as f:
	lines = f.readlines()

horizontal_pos = 0
depth = 0
depth_p2 = 0

for line in lines:
	dir,val = line.strip('\n').split(' ')
	val = int(val)
	if dir == 'forward':
		horizontal_pos += val
		depth_p2 += depth * val
	elif dir == 'down':
		depth += val
	elif dir == 'up':
		depth -= val

p1 = horizontal_pos*depth
p2 = horizontal_pos*depth_p2

print(f"p1: {p1} p2: {p2}")

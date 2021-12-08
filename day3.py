with open('day3.txt') as f:
	lines = f.readlines()

lines = [line.strip('\n') for line in lines]

def get_most_common(my_list,position):
	count = sum(int(val[position]) for val in my_list)

	if count >= len(my_list)/2:
		return 1
	else:
		return 0

def keep_most_common(my_list,position,flip):
	if len(my_list) == 1:
		return my_list

	new_list = []
	common = get_most_common(my_list,position)
	if flip:
		common = (common-1)*-1
	for bin_num in my_list:
			if int(bin_num[position]) == common:
				new_list.append(bin_num)

	return new_list

gamma = 0
epsilon = 0
oxy_list = lines
co2_list = lines

# iterate over each bit position
for bit_position in range(len(lines[0])):
	val = get_most_common(lines,bit_position)
	gamma = (2*gamma) + val
	epsilon = (2*epsilon) + (val-1)*-1

	oxy_list = keep_most_common(oxy_list,bit_position,False)
	co2_list = keep_most_common(co2_list,bit_position,True)

p1 = gamma*epsilon

oxy_val = int(oxy_list[0],2)
co2_val = int(co2_list[0],2)
p2 = oxy_val*co2_val

print(f"p1: {p1} p2: {p2}")


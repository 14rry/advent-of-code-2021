
fishs = [3,4,3,1,2] # example input

mask = [0]*9
fishs = [int(x) for x in open('day6.txt').read().strip().split(',')]

for fish in fishs:
    mask[fish] += 1

# change range to 80 for part 1
for day in range(256):
    new_mask = [0]*9
    for idx,val in enumerate(mask):
        if idx == 0:
            new_mask[8] += val
            new_mask[6] += val
        else:
            new_mask[idx-1] += val
    mask = new_mask
    
print(sum(mask))
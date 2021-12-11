input = open('day8.txt').readlines()

inputs = []
outputs = []
for line in input:
    temp = line.split('|')
    outputs.append(temp[1].split())
    inputs.append(temp[0].split())

output_vals = []

# analyze input to determine other digits:
# inputs = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split()

def parse_input_set(inputs):
    digit_strs = ['']*10
    for segs in inputs:
        if len(segs) == 2:
            digit_strs[1] = segs
        elif len(segs) == 3:
            digit_strs[7] = segs
        elif len(segs) == 4:
            digit_strs[4] = segs
        elif len(segs) == 7:
            digit_strs[8] = segs
    # 6 is the only digit with 6 segments and only one of the right most segments
    for segs in inputs:
        if len(segs) == 6: # could be 0,6,9
            # if it's missing any of the '1' segments, it's 6
            isZero = True
            if digit_strs[6] == '':
                for c in digit_strs[1]:
                    if segs.find(c) == -1:
                        digit_strs[6] = segs
                        isZero = False
            # if it has all of the '4' segments, it's 9
            if digit_strs[9] == '' and isZero:
                test = True
                for c in digit_strs[4]:
                    if segs.find(c) == -1:
                        test = False
                if test:
                    digit_strs[9] = segs
                    isZero = False
            if isZero:
                digit_strs[0] = segs
    for segs in inputs:
        if len(segs) == 5: # could be 2,3,5
            # if it has both '1' segments, it's 3
            if digit_strs[3] == '':
                test = True
                for c in digit_strs[1]:
                    if segs.find(c) == -1:
                        test = False
                if test:
                    digit_strs[3] = segs
            # if every segment is in '6', it's '5'
            if digit_strs[5] == '':
                test = True
                for c in segs:
                    if digit_strs[6].find(c) == -1:
                        test = False
                if test:
                    digit_strs[5] = segs
    for segs in inputs:
        if segs not in digit_strs:
            digit_strs[2] = segs

    return digit_strs

def find_equivalent(digits,segs):
    for idx,val in enumerate(digits):
        if len(val) == len(segs):
            test = True
            for c in segs:
                if val.find(c) == -1:
                    test = False
            if test:
                return idx
    print('error!',segs,digits)
    return -1 #error

p2 = 0
p1 = 0
for idx,ins in enumerate(inputs):
    output_val = 0
    digits = parse_input_set(ins)
    for val in outputs[idx]:
        real_digit = find_equivalent(digits,val)
        if real_digit in [1,4,7,8]:
            p1 += 1
        output_val = output_val*10 + find_equivalent(digits,val)
    output_vals.append(output_val)
    p2 += output_val

print(f"p1: {p1} p2: {p2}")

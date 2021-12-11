import statistics

input = "{([(<{}[<>[]}>{[]{[(<()>"
input = open('day10.txt').readlines()
temp = []
openings = ['{','(','<','[']
score = 0
complete_scores = []
for line in input:
    stack = []
    for idx,c in enumerate(line):
        if c in openings:
            stack.append(c)
        else:
            now = stack.pop()
            valid = False
            if c == '}':
                if now == '{':
                    valid = True
                else:
                    score += 1197
            elif c == ')':
                if now == '(':
                    valid = True
                else:
                    score += 3
            elif c == ']':
                if now == '[':
                    valid = True
                else:
                    score += 57
            elif c == '>':
                if now == '<':
                    valid = True
                else:
                    score += 25137
            if not valid:
                stack.append(now)
                break
    if idx == len(line)-1: # valid but incomplete
        # calc completion score
        cs = 0
        for val in stack[::-1]:
            if val == '(':
                cs = cs*5 + 1
            elif val == '[':
                cs = cs*5 + 2
            elif val == '{':
                cs = cs*5 + 3
            elif val == '<':
                cs = cs*5 + 4
        complete_scores.append(cs)
        
p1 = score
p2 = statistics.median(complete_scores)

print(f"p1: {p1} p2: {p2}")

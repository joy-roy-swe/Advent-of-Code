import sys
from collections import defaultdict, Counter
infile = sys.argv[1] if len(sys.argv)>=2 else 'day-1-input.in'
D = open(infile).read().strip()

lines = D.split('\n')
LEFT = []
RIGHT = []
RC = Counter()

for line in lines:
    l,r = line.split()
    l,r = int(l),int(r)
    LEFT.append(l)
    RIGHT.append(r)
    RC[r] += 1

LEFT.sort()
RIGHT.sort()
answer = 0

for l,r in zip(LEFT,RIGHT):
    answer += abs(l-r)
print(answer)

answer = 0
for l in LEFT:
    answer += l * RC.get(l,0)
print(answer)


import sys
infile = sys.argv[1] if len(sys.argv)>=2 else 'day-1-input.in'
D = open(infile).read().strip()

lines = D.split('\n')

LL = []
RR = []

for line in lines:
    L,R = line.split()
    L,R = int(L),int(R)
    LL.append(L)
    RR.append(R)
LL.sort()
RR.sort()
answer = 0

for l,r in zip(LL,RR):
    answer += abs(l-r)
print(answer)


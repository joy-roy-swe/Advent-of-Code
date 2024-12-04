import sys
import re
infile = sys.argv[1] if len(sys.argv)>=2 else 'day-3-input.in'
D = open(infile).read().strip()

def valid_mul_calculation(str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, str)
    result = sum(int(a) * int(b) for a, b in matches)
    return result

lines = D.split('\n')
answer = 0

for line in lines:
    answer += valid_mul_calculation(line)

print(answer)

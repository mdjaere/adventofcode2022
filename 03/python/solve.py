import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [line.strip() for line in open(infile)]


def getPriority(c):
    o = ord(c) - ord("a") + 1
    if o < 0:
        o = ord(c) - ord("A") + 27
    return o


score = 0
for sack in lines:
    half = int(len(sack) / 2)
    comp_a, comp_b = sack[0:half], sack[half:]
    same = list(set(comp_a).intersection(set(comp_b)))[0]
    score += getPriority(same)
print(score)

score_2 = 0
i = 0
while i < len(lines):
    same = list(set(lines[i]).intersection(
        set(lines[i+1])).intersection(set(lines[i+2])))[0]
    score_2 += getPriority(same)
    i = i + 3
print(score_2)

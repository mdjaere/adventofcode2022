import sys
import re

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'

def get_score(a, b):
  if a == "rock":
    if b == "rock":
      return 1, 3
    if b == "paper":
      return 1, 0
    if b == "scissors":
      return 1, 6
  if a == "paper":
    if b == "rock":
      return 2, 6
    if b == "paper":
      return 2, 3
    if b == "scissors":
      return 2, 0
  if a == "scissors":
    if b == "rock":
      return 3, 0
    if b == "paper":
      return 3, 6
    if b == "scissors":
      return 3, 3
  raise Exception()


def get_score_2(a, b):
  if a == "A":
    if b == "X":
      return 3, 0
    if b == "Y":
      return 1, 3
    if b == "Z":
      return 2, 6
  if a == "B":
    if b == "X":
      return 1, 0
    if b == "Y":
      return 2, 3
    if b == "Z":
      return 3, 6
  if a == "C":
    if b == "X":
      return 2, 0
    if b == "Y":
      return 3, 3
    if b == "Z":
      return 1, 6
  raise Exception()


scores = []
scores_2 = []
for line in open(infile):
  line_raw = line.strip()

  # Part 1
  line = line_raw
  replacements = [("A|X", "rock"), ("B|Y", "paper"), ("C|Z", "scissors")]
  for pat, new in replacements:
    line = re.sub(pat, new, line)
  elf, me = line.split(" ")
  score = get_score(me, elf)
  scores.append(score)

  # part 2
  elf, outcome = line_raw.split(" ")
  score_2 = get_score_2(elf, outcome)
  scores_2.append(score_2)

ans = sum([sum(s) for s in scores])
assert (ans == 17189)
print(ans)

ans_2 = sum([sum(s) for s in scores_2])
assert (ans_2 == 13490)
print(ans_2)

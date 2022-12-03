import sys

infile = sys.argv[1] if len(sys.argv) > 1 else 'input'
lines = [lines.strip() for line in open(infile)]
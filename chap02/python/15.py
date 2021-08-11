import sys

with open('./popular-names.txt', mode="r") as f:
    n = int(sys.argv[1])
    lines = [line.rstrip() for line in f]
    for i in range(n, 0, -1):
        print(lines[-i])
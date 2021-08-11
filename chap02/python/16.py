import sys
import math

with open('./popular-names.txt', mode="r") as f:
    n = int(sys.argv[1])
    lines = [line.rstrip() for line in f]
    n_split = math.ceil(len(lines) / float(n))
    fs = [open(f"f_{i}.txt", mode="w") for i in range(n)]
    i = 0
    cnt = 0
    for line in lines:
        fs[i].write(line + "\n")
        cnt += 1
        if cnt == n_split:
            i += 1
            cnt = 0
    for i in range(n):
        fs[i].close()
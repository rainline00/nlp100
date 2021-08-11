import sys

with open('./popular-names.txt', mode="r") as f:
    n = int(sys.argv[1])
    cnt = 0
    for line in f:
        print(line.rstrip())
        cnt += 1
        if cnt == n: break
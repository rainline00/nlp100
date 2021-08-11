with open('./popular-names.txt', mode="r") as f:
    lines = [line.rstrip().split() for line in f]
    lines.sort(key=lambda x: int(x[2]), reverse=True)
    for line in lines:
        print("\t".join(line))

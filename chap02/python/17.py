with open('./popular-names.txt', mode="r") as f:
    names = sorted(set([line.split()[0] for line in f]))
    for name in names:
        print(name)
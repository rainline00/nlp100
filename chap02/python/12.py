with open('./popular-names.txt', mode="r") as f:
    f1 = open("col1.txt", mode="w")
    f2 = open("col2.txt", mode="w")
    for line in f:
        c1, c2, _, _ = line.rstrip().split()
        f1.write(c1 + "\n")
        f2.write(c2 + "\n")
    f1.close()
    f2.close()
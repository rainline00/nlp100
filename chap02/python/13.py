with open("col1.txt") as f1:
    with open("col2.txt") as f2:
        f = open("merged.txt", mode="w")
        for c1, c2 in zip(f1, f2):
            f.write(c1.rstrip() + "\t" + c2.rstrip() + "\n")
        f.close()

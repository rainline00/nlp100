with open("../output/england.txt", mode="r") as f:
    for line in f:
        if line.startswith("[[Category:"):
            print(line.rstrip())
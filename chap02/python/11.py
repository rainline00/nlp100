with open('./popular-names.txt', mode="r") as f:
    for line in f:
        print(line.replace("\t", " "), end="")
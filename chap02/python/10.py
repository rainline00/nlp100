with open('./popular-names.txt', mode="r") as f:
    print(len([_ for _ in f]))
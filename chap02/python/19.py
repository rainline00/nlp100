from collections import Counter

with open('./popular-names.txt', mode="r") as f:
    names = [line.split()[0] for line in f]
    counter = Counter(names)
    for k, v in counter.most_common():
        print(v, k)
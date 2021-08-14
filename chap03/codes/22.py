import re

p = re.compile("^\[\[Category:(.*?)(?:\|.*)?\]\]$")

with open("../output/england.txt", mode="r") as f:
    for line in f:
        m = p.match(line.rstrip())
        if m:
            print(m.groups()[0])

import re

p = re.compile(r"^(\={2,})\s*(.+?)\s*(\={2,})$")

with open("../output/england.txt", mode="r") as f:
    for line in f:
        m = p.match(line.rstrip())
        if m:
            level = len(m.groups()[0]) - 1
            name = m.groups()[1]
            print(f"{level}: {name}")

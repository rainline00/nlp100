import re
# +? -> 最短一致
# +  -> 最長一致
p = re.compile(r"\[\[ファイル:(.+?)\|")

with open("../output/england.txt", mode="r") as f:
    text = "".join([line for line in f])
    m = p.findall(text, re.MULTILINE)
    print("\n".join(m))

import re

with open("../output/england.txt", mode="r") as f:
    text = f.read()
    
target = re.findall(r"^\{\{基礎情報.*?$([\s\S]*?)^\}\}$", text, re.MULTILINE)[0]
target = re.sub(r"\'{2,5}", "", target)
target = re.sub(r"\[\[([^\|]*?\|)??([^\|]*?)\]\]", r"\2", target)
# ?? は 0回一致か1回一致か選べる状況ならば0回一致を選ぶ（最短一致）

result = re.findall(r"^\|\s*(.*?)\s*\=\s*?(.*?)$", target, re.MULTILINE)
dic = dict(result)
for k, v in dic.items():
    print(k, v)

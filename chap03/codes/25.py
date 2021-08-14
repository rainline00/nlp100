import re

with open("../output/england.txt", mode="r") as f:
    text = f.read()
    
target = re.findall(r"^\{\{基礎情報.*?$([\s\S]*?)^\}\}$", text, re.MULTILINE)[0]
target = re.sub(r"\'{2,5}", "", target)

result = re.findall(r"^\|\s*(.*?)\s*\=\s*?(.*?)$", target, re.MULTILINE)
dic = dict(result)
for k, v in dic.items():
    print(k, v)
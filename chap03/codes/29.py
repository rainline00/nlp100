import requests
import re
import json

with open("../output/england.txt", mode="r") as f:
    text = f.read()
    
target = re.findall(r"^\{\{基礎情報.*?$([\s\S]*?)^\}\}$", text, re.MULTILINE)[0]
target = re.sub(r"\'{2,5}", "", target)
target = re.sub(r"\[\[([^\|]*?\|)??([^\|]*?)\]\]", r"\2", target)
# ?? は 0回一致か1回一致か選べる状況ならば0回一致を選ぶ（最短一致）
target = re.sub(r"<.+?>", r"", target)
target = re.sub(r"\{\{(?:lang\|.+?|仮リンク)\|([^\|\}]+)[^\}]*\}\}", r"\1", target)

result = re.findall(r"^\|\s*(.*?)\s*\=\s*?(.*?)$", target, re.MULTILINE)
dic = dict(result)

url_file = dic["国旗画像"].replace(" ", "_")
url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
data = requests.get(url)
print(re.search(r"\"url\":\s*\"([^\"]+)\"", data.text).groups()[0])
#df = json.loads(data.text)
#print(df["query"]["pages"]["347935"]["imageinfo"][0]["url"])
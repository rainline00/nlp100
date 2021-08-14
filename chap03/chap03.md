# chap03
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．

1行に1記事の情報がJSON形式で格納される
各行には記事名が”title”キーに，記事本文が”text”キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
ファイル全体はgzipで圧縮される
以下の処理を行うプログラムを作成せよ．

# 20. JSONデータの読み込み 
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
```python
import json

with open("../input/jawiki-country.json", mode="r") as f:
    fw = open("../output/england.txt", mode="w")
    for line in f:
        df = json.loads(line)
        if df["title"] == "イギリス":
            fw.write(df["text"])
    fw.close()
```

# 21. カテゴリ名を含む行を抽出 
記事中でカテゴリ名を宣言している行を抽出せよ．
```python
with open("../output/england.txt", mode="r") as f:
    for line in f:
        if line.startswith("[[Category:"):
            print(line.rstrip())
```

# 22. カテゴリ名の抽出 
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
```python
import re

p = re.compile("^\[\[Category:(.*?)(?:\|.*)?\]\]$")

with open("../output/england.txt", mode="r") as f:
    for line in f:
        m = p.match(line.rstrip())
        if m:
            print(m.groups()[0])
```

# 23. セクション構造 
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．

```python
import re

p = re.compile(r"^(\={2,})\s*(.+?)\s*(\={2,})$")

with open("../output/england.txt", mode="r") as f:
    for line in f:
        m = p.match(line.rstrip())
        if m:
            level = len(m.groups()[0]) - 1
            name = m.groups()[1]
            print(f"{level}: {name}")
```

# 24. ファイル参照の抽出 
記事から参照されているメディアファイルをすべて抜き出せ．

```python
import re
# +? -> 最短一致
# +  -> 最長一致
p = re.compile(r"\[\[ファイル:(.+?)\|")

with open("../output/england.txt", mode="r") as f:
    text = "".join([line for line in f])
    m = p.findall(text, re.MULTILINE)
    print("\n".join(m))
```

# 25. テンプレートの抽出 
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
```python
import re

with open("../output/england.txt", mode="r") as f:
    text = f.read()
    
target = re.findall(r"^\{\{基礎情報.*?$([\s\S]*?)^\}\}$", text, re.MULTILINE)

result = re.findall(r"^\|\s*(.*?)\s*\=\s*?(.*?)$", target[0], re.MULTILINE)
dic = dict(result)
for k, v in dic.items():
    print(k, v)import re

with open("../output/england.txt", mode="r") as f:
    text = f.read()
    
target = re.findall(r"^\{\{基礎情報.*?$([\s\S]*?)^\}\}$", text, re.MULTILINE)

result = re.findall(r"^\|\s*(.*?)\s*\=\s*?(.*?)$", target[0], re.MULTILINE)
dic = dict(result)
for k, v in dic.items():
    print(k, v)
```

# 26. 強調マークアップの除去 
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
```python
import re

with open("../output/england.txt", mode="r") as f:
    text = f.read()
    
target = re.findall(r"^\{\{基礎情報.*?$([\s\S]*?)^\}\}$", text, re.MULTILINE)[0]
target = re.sub(r"\'{2,5}", "", target)

result = re.findall(r"^\|\s*(.*?)\s*\=\s*?(.*?)$", target, re.MULTILINE)
dic = dict(result)
for k, v in dic.items():
    print(k, v)

````

# 27. 内部リンクの除去 
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
```python
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
```

# 28. MediaWikiマークアップの除去 
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
```python
import re

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
for k, v in dic.items():
    print(k, v)

```


# 29. 国旗画像のURLを取得する 
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
```python
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
```
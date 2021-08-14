import json

with open("../input/jawiki-country.json", mode="r") as f:
    fw = open("../output/england.txt", mode="w")
    for line in f:
        df = json.loads(line)
        if df["title"] == "イギリス":
            fw.write(df["text"])
    fw.close()
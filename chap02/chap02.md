# 10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ
```
wc -l popular-names.txt
```

# 11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ
```
sed -e 's/\t/ /g' popular-names.txt > 11sed.txt
cat popular-names.txt | tr '\t' ' ' > 11tr.txt
expand -t1 popular-names.txt > 11expand.txt
```

# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
```
cut -f 1 popular-names.txt > col1.txt
cut -f 2 popular-names.txt > col2.txt
```

# 13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

```
paste col1.txt col2.txt > merged.txt
```

# 14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

```
chap02 $ head -n5 popular-names.txt
Mary	F	7065	1880
Anna	F	2604	1880
Emma	F	2003	1880
Elizabeth	F	1939	1880
Minnie	F	1746	1880
```

# 15. 末尾のN行を出力 
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

```
chap02 $ tail -n5 popular-names.txt
Benjamin	M	13381	2018
Elijah	M	12886	2018
Lucas	M	12585	2018
Mason	M	12435	2018
Logan	M	12352	2018
```

# 16. ファイルをN分割する 
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

```
split -n popular-names.txt
```

# 17. １列目の文字列の異なり 
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはcut, sort, uniqコマンドを用いよ．
```
cut -f 1 popular-names.txt| sort | uniq > set_name.txt
```

# 18. 各行を3コラム目の数値の降順にソート 
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
```
sort -n -r -k3 popular-names.txt > sorted_3col.txt
```
# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる 
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
```
cut -f 1 popular-names.txt | sort | uniq -c > num_names.txt
```
# analysis_of_hitrecords

## 本レポジトリについて
このレポジトリは東京大学システム創成学科Cコースの「社会システム工学応用」という授業で与えられた課題を実装したものである。
楽曲のデータを集計し、それをヒストグラムにまとめ、正規分布(=ガウス分布)でフィッティングした。その後、事後確率の中央値を数値的に求め、アンケート結果と照合した。
詳しくはhttps://github.com/miyamotononno/analysis_of_hitrecords/issues/1 のスライドを参照すること。

## setup
楽曲の集計にあたり、Spotify Web API(特に、python版のspotipy)を用いている。  

使用するにあたり、クライアントID,クライアントSecret, ユーザーネームが必要である。それらを生成次第、以下のように新たにconfig.pyというファイルを作成すること。
```
CLIENT_ID = '-----------'
CLIENT_SECRET = '-----------'
USER_NAME = '-----------'

```

## 結果

楽曲の集計結果はhitrecord.pngファイルに、ベイズ推定の結果はprediction.pngファイルにある。

## 参考

本調査の概要: https://github.com/miyamotononno/analysis_of_hitrecords/issues/1

論文 *Optimal Prediction in Every Congnition*: https://web.mit.edu/cocosci/Papers/Griffiths-Tenenbaum-PsychSci06.pdf

Spotify Web API: https://developer.spotify.com/documentation/web-api/  

spotipy: https://spotipy.readthedocs.io/en/latest/

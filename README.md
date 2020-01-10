# analysis_of_hitrecords

## 本レポジトリについて
このレポジトリは東京大学システム創成学科Cコースの「社会システム工学応用」という授業で与えられた課題を実装したものである。
楽曲のデータを集計し、それをヒストグラムにまとめ、正規分布(=ガウス分布)でフィッティングした。その後、事後確率の中央値を数値的に求め、アンケート結果と照合した。

## setup
楽曲の集計にあたり、Spotify Web API(特に、python版のspotipy)を用いている。  

使用するにあたり、クライアントID,クライアントSecret, ユーザーネームが必要である。それらを生成次第、以下のように新たにconfig.pyというファイルを作成すること。
```
CLIENT_ID = '-----------'
CLIENT_SECRET = '-----------'
USER_NAME = '-----------'

```

## ベイズ推定について

![スクリーンショット 2020-01-10 23 32 55](https://user-images.githubusercontent.com/32972443/72161997-7b37f600-3404-11ea-8f85-ed375e5d4022.png)


## 結果

楽曲の集計結果はhitrecord.pngファイルに、ベイズ推定の結果はprediction.pngファイルにある。

## 参考

論文 *Optimal Prediction in Every Congnition*: https://web.mit.edu/cocosci/Papers/Griffiths-Tenenbaum-PsychSci06.pdf

Spotify Web API: https://developer.spotify.com/documentation/web-api/  

spotipy: https://spotipy.readthedocs.io/en/latest/

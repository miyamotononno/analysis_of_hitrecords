# analysis_of_hitrecords

## 本レポジトリについて
このレポジトリは東京大学システム創成学科Cコースの「社会システム工学応用」という授業で与えられた課題を実装したものである。
楽曲のデータを集計し、それをヒストグラムにまとめ、ガウス分布でフィッティングした。

## setup
楽曲の集計にあたり、Spotify Web API(特に、python版のspotipy)を用いている。
使用するにあたり、クライアントID,クライアントSecret, ユーザーネームが必要である。
それらを生成次第、以下のように新たにconfig.pyというファイルを作成すること。
```
CLIENT_ID = '-----------'
CLIENT_SECRET = '-----------'
USER_NAME = '-----------'

```

## 参考
Spotify Web API: https://developer.spotify.com/documentation/web-api/
spotipy: https://spotipy.readthedocs.io/en/latest/

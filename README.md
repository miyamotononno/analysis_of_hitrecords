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

## ベイズ推定について

ベイズの定理は、事後確率$p(t_{total} | t)$、事前確率$p(t | t_{total})$、尤度$p(t_{total})$を用いて、

$$
    p(t_{total} | t) = \frac{p(t | t_{total})p(t_{total})}{p(t)}
$$

と表される。　　

今回の事例に合わせて用語を整理する。　　　　


事後確率$p(t_{total} | t)$はある楽曲がt分経過したときに、その楽曲の全体の時間が$t_{total}$分である確率である。

尤度$p(t_{total})$は楽曲全体の中で、ある曲が1曲t分である確率である。これはさきほどの正規分布に従う。  
事前確率$p(t | t_{total})$はある楽曲を聞いている中で、その曲が今何秒経過しているかである。これは、一様分布に従っており、$\cfrac{1}{t_{total}}\$である。  

$p(t)$ は聞こえた楽曲が何秒経過しているかである。これは、聞こえてきた楽曲が１曲 $t_{total}$分である確率にt秒経過した確率をかけ、全ての$t_{total}$分の楽曲に対して足し合わせることに等しい。つまり、以下のような形で示される。

$$
    p(t) = \int_{0}^{\infty} p(t | t_{total})p(t_{total}) dt_{total}
$$

今回求めるのは、（論文に従い）事後確率の中央値である。つまり、  

$$
    p(t_{total}>t^* | t)=0.5
$$
 
となる$t^* $である。事前確率が正規分布に従う場合、$p(t)$が解析的に解くことが不可能なので、数値的に解く必要がある。

## 結果

楽曲の集計結果はhitrecord.pngファイルに、ベイズ推定の結果はprediction.pngファイルにある。

## 参考

論文 Optimal Prediction in Every Congnition: https://web.mit.edu/cocosci/Papers/Griffiths-Tenenbaum-PsychSci06.pdf

Spotify Web API: https://developer.spotify.com/documentation/web-api/  

spotipy: https://spotipy.readthedocs.io/en/latest/

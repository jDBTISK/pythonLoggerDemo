# logger demo

## Overview

python logger のデモ

## Description

自分で logger の設定することって他の言語だとあまりなかったりする(?)ので  
さあ python でスクリプト書こう!!と思った時に logger の挙動を理解しておらずめちゃくちゃになることがしばしば。

というわけでよく使う最小限の logger (handler でメール飛ばしたりも出来るけどそういう高度なことは別途調べてください) の設定だけ書きました

短いコードなので内容はコード読んで理解してください。

## Setup

`python 3` 系なら動くと思います。

## Examples

普通に実行すると標準出力にログが出る

```log
python main.py
2021-05-13 22:13:15,951 [INFO] __main__ : begining script.
2021-05-13 22:13:15,951 [DEBUG] __main__ : ↓↓↓ Hoge のインスタンスを生成 (Level >= INFO のログを出力) ↓↓↓
2021-05-13 22:13:15,951 [INFO] hoge : hoge.INFO
2021-05-13 22:13:15,951 [WARNING] hoge : hoge.WARN
2021-05-13 22:13:15,952 [ERROR] hoge : hoge.ERROR
2021-05-13 22:13:15,952 [DEBUG] __main__ : ↓↓↓ Fuga のインスタンスを生成 (Level >= WARN のログを出力) ↓↓↓
2021-05-13 22:13:15,952 [WARNING] fuga : fuga.WARN
2021-05-13 22:13:15,952 [ERROR] fuga : fuga.ERROR
2021-05-13 22:13:15,952 [INFO] __main__ : finished script.
```

`-f` または `--outputLogFile` を指定することで `logs` ディレクトリ直下に作られる log ファイルにログが出る

```log
python main.py -f
```

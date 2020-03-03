# Inno vation Nominated Database とは

総務省が主催の「異能（Inno）vation」事業にて、奇想天外なアイデアを募る「ジェネレーションアワード」というものが、2017年より開催されています。

2018〜2019年度にジェネレーションアワードでノミネートされた人物の一覧に記載されている、下記の情報を json 形式で出力するプログラムです。

- 人物名
- 年度
- ノミネートされたテーマ

処理したデータ (nominated.json) を、カレントディレクトリに出力します

# 必要なもの
- Python 3系 (3.7.6 で動作検証済み)
- BeautifulSoup 4

# 実行方法

```bash
 $ git clone https://github.com/Genbuchan/inno-vation-nominated-database.git
 $ cd inno-vation-nominated-database
 $ python3 main.py
```

# 備考
- キーは人物名、値は年度とテーマを格納した配列
- 上記の設計により、複数回のノミネートに対応
- 1つのテーマが複数人によるノミネートの場合、各人物ごとに独立してテーマを記録
- 企業名の場合、人物名と同じように記録

# ToDo
- 人物の都道府県を記録する

# クレジット
(C) 2020 Genbu, 異能vation

当プログラムにて出力されたコンテンツは、異能vation の利用規約に基づき、CC BY 4.0 (表示 4.0 国際) にて使用することができます

[https://creativecommons.org/licenses/by/4.0/legalcode.ja](https://creativecommons.org/licenses/by/4.0/legalcode.ja)

出典: 異能vation ホームページ (https://www.inno.go.jp)

- 平成30年度「異能ジェネレーションアワード」ノミネート発表[(https://www.inno.go.jp/result/h30/nominate.php)](https://www.inno.go.jp/result/h30/nominate.php)
- 2019年度「ジェネレーションアワード」部門ノミネート発表[(https://www.inno.go.jp/result/2019/generation/nominate/)](https://www.inno.go.jp/result/2019/generation/nominate/)

上記の Web ページの内容を json 形式に整形し出力します。
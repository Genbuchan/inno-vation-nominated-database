#!/usr/bin/env python3
# coding: utf-8

import codecs
import json
import urllib.request
from bs4 import BeautifulSoup

# 初期化

urls = {
  "2018": "https://www.inno.go.jp/result/h30/nominate.php",
  "2019": "https://www.inno.go.jp/result/2019/generation/nominate/"
}

people = dict()

# 人物の情報を記録する関数

def add_human_data(human_name:str) :
  """Add human data to people"""
  if human_name in people:
    people[human_name].append({
      "year": url[0],
      "theme": human.find('div', class_="theme").find('h3').string
    })
  else:
    people[human_name] = list()
    people[human_name].append({
      "year": url[0],
      "theme": human.find('div', class_="theme").find('h3').string
    })

# URL を順次代入し、people 変数に格納
for url in urls.items() :
  html = urllib.request.urlopen(url[1])
  parser = BeautifulSoup(html, "html.parser")

  # ノミネートされた情報・人物を human 変数に格納
  for human in parser.find_all('div', class_="cont cf") :
    names = human.find('span').string
    # 複数人でノミネートされた場合、各人物ごとに独立して格納
    if "・" in names :
      for name in names.split("・") :
        add_human_data(name)

    #単体でノミネートされた場合
    else:
      add_human_data(names)

# nominated.json に person 変数の内容を書き込む
with codecs.open('nominated.json', 'w', 'utf-8') as output :
  json.dump(people, output, indent=2, ensure_ascii=False)

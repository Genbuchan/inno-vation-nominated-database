#!/usr/bin/env python3
# coding: utf-8

import codecs
import json
import urllib.request
from bs4 import BeautifulSoup

urls = {
  "2018": "https://www.inno.go.jp/result/h30/nominate.php",
  "2019": "https://www.inno.go.jp/result/2019/generation/nominate/"
}

people = dict()

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

for url in urls.items() :
  html = urllib.request.urlopen(url[1])
  parser = BeautifulSoup(html, "html.parser")

  for human in parser.find_all('div', class_="cont cf") :
    names = human.find('span').string
    if "・" in names :
      for name in names.split("・") :
        add_human_data(name)

    else:
      add_human_data(names)

with codecs.open('nominated.json', 'w', 'utf-8') as output :
  json.dump(people, output, indent=2, ensure_ascii=False)

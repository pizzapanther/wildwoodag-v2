#!/usr/bin/env python3

import os
import re

def run():
  base = "public"
  html = [
    [r'href="/(.*)/"', r'href="/\1/index.html"'],
    [r"href='/(.*)/'", r"href='/\1/index.html'"],
  ]

  json = [
    [r'"permalink":\s*"/(.*?)/"', r'"permalink":"/\1/index.html"'],
  ]

  path = "public/search/index.json"
  with open(path, 'r') as fh:
    text = fh.read()

  for s in json:
    text = re.sub(s[0], s[1], text, flags=re.I)

  with open(path, 'w') as fh:
    fh.write(text)

  for root, dirs, files in os.walk(base):
    for f in files:
      if f.endswith(".html"):
        path = os.path.join(root, f)
        print("Working:", path)
        with open(path, 'r') as fh:
          text = fh.read()

        for s in html:
          text = re.sub(s[0], s[1], text, flags=re.I)

        with open(path, 'w') as fh:
          fh.write(text)


if __name__ == "__main__":
  run()

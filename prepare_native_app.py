#!/usr/bin/env python3

import os


def run():
  base = "public"
  index_paths = [
    '/about/',
    '/events/',
    '/watch/',
    '/donate/',
    '/contact/'
  ]

  for root, dirs, files in os.walk(base):
    for f in files:
      if f.endswith(".html"):
        path = os.path.join(root, f)
        print("Working:", path)
        with open(path, 'r') as fh:
          text = fh.read()

        for i in index_paths:
          text = text.replace(i, f"{i}index.html")

        with open(path, 'w') as fh:
          fh.write(text)


if __name__ == "__main__":
  run()

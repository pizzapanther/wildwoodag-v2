#!/usr/bin/env python3

import datetime
import json
import os.path
import re
import unicodedata
import urllib.request


TEMPLATE = """---
title: {title}
date: {year}-{month}-{day}
image: {img}
categories:
tags:
---

{content}

"""

def zpad(d):
  return str(d).zfill(2)


def slugify(s, dt):
  slug = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii').lower()
  slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
  slug = re.sub(r'[-]+', '-', slug)
  return f'{dt.year}-{zpad(dt.month)}-{zpad(dt.day)}-{slug}'


def main():
  with open('mv/old-posts.json', 'r') as fh:
    posts = json.load(fh)

  cnt = 0
  for p in posts:
    print('Processing:', p[0], p[2])
    cnt += 1

    dt = datetime.datetime.fromisoformat(p[2])
    slug = slugify(p[0], dt)
    print(slug)
    print(p[3])
    base, ext = os.path.splitext(p[3])
    img_path = f'static/pimg/{slug}{ext}'
    img_url = f'/pimg/{slug}{ext}'
    md_path = f'content/post/{slug}.md'

    if not os.path.exists(img_path):
      with urllib.request.urlopen(p[3]) as fh:
        with open(img_path, 'wb') as wh:
          wh.write(fh.read())

      print('Wrote:', img_path)

    context = {
      'title': p[0],
      'year': dt.year,
      'month': zpad(dt.month),
      'day': zpad(dt.day),
      'img': img_url,
      'content': p[1],
    }
    content = TEMPLATE.format(**context)

    with open(md_path, 'w') as wh:
      wh.write(content)

    print('Wrote:', md_path)

  print('Total:', cnt)


if __name__ == "__main__":
  main()

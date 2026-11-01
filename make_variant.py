#!/usr/bin/env python3
"""Generate the two named pages from index.html:

  shalome-tanmay/index.html   (Shalome & Tanmay, same as the root page)
  tanmay-shalome/index.html   (Tanmay & Shalome)

Edit index.html, then run:  python3 make_variant.py
Only the names, their order, the card artwork and the relative paths differ.
The root index.html is kept as is so links already shared keep working.
"""
import os, re
BASE = 'https://tanmayhc7.github.io/ts_saveTheDate/'
src = open('index.html', encoding='utf-8').read()

def build(folder, swap):
    s = src
    s = s.replace('<meta property="og:url" content="' + BASE + '">', '<meta property="og:url" content="' + BASE + folder + '/">')
    if swap:
        s = s.replace(BASE + 'assets/og-card.jpg', BASE + 'assets/og-card-tanmay-shalome.jpg')
        for a, b in [('Shalome &amp; Tanmay', 'Tanmay &amp; Shalome'), ('Shalome and Tanmay', 'Tanmay and Shalome')]:
            s = s.replace(a, b)
        s = s.replace('url(assets/card.jpg)', 'url(assets/card-tanmay-shalome.jpg)')
    s = re.sub(r'(?<![\w/.])assets/', '../assets/', s)
    os.makedirs(folder, exist_ok=True)
    open(folder + '/index.html', 'w', encoding='utf-8').write(s)
    print('written', folder + '/index.html')

build('shalome-tanmay', swap=False)
build('tanmay-shalome', swap=True)

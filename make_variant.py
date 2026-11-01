#!/usr/bin/env python3
"""Generate the Tanmay & Shalome page (tanmay-shalome/index.html) from index.html.

Edit index.html, then run:  python3 make_variant.py
Only the names, their order, the card artwork and the relative paths differ.
"""
import os, re
BASE = 'https://tanmayhc7.github.io/ts_saveTheDate/'
src = open('index.html', encoding='utf-8').read()
s = src
# absolute URLs first: this page lives one folder deeper and has its own link preview
s = s.replace(BASE + 'assets/og-card.jpg', BASE + 'assets/og-card-tanmay-shalome.jpg')
s = s.replace('<meta property="og:url" content="' + BASE + '">', '<meta property="og:url" content="' + BASE + 'tanmay-shalome/">')
# names, in the new order
for a, b in [('Shalome &amp; Tanmay', 'Tanmay &amp; Shalome'), ('Shalome and Tanmay', 'Tanmay and Shalome')]:
    s = s.replace(a, b)
# card artwork with the names swapped
s = s.replace('url(assets/card.jpg)', 'url(assets/card-tanmay-shalome.jpg)')
# relative paths: one folder deeper
s = re.sub(r'(?<![\w/.])assets/', '../assets/', s)
os.makedirs('tanmay-shalome', exist_ok=True)
open('tanmay-shalome/index.html', 'w', encoding='utf-8').write(s)
left = [m for m in re.findall(r'.{20}Shalome.{20}', s) if 'Tanmay' in m and m.index('Shalome') < m.index('Tanmay')]
print('written tanmay-shalome/index.html; leftover Shalome-first names:', left)

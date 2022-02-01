import re

txt = open('post.md').read()

# Anything that isn't a square closing bracket
name_regex = "[^]]+"
# http:// or https:// followed by anything but a closing paren
url_regex = "http[s]?://[^)]+"

markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

matches = []
for match in re.findall(markup_regex, txt):
    print(match)
    matches.append(match)
template_iframe = """<iframe width="560" height="315" 
src="https://www.youtube.com/embed/{0}?controls=0" 
title="YouTube video player" frameborder="0" allow="accelerometer; 
autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

for match in matches:
    youtube_idx = match[1].split('/')[-1]
    txt = txt.replace('![{}]({})'.format(match[0], match[1]), template_iframe.format(youtube_idx, match[0]))

print(txt)


# ![Ansible - A Beginner's Tutorial, Part 2](https://youtu.be/pRZA9ymZXn0)
# 
# <iframe width="560" height="315" 
# src="https://www.youtube.com/embed/gxBis8EgoAg?controls=0" 
# title="YouTube video player" frameborder="0" allow="accelerometer; 
# autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

 

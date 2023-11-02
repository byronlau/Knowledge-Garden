#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31
# @Author  : byron
# @File    : TxtToMK.py
# @description: 将如下字符串old 中的内容转化为 new 中格式

""" old
01.道可道，非常道。名可名，非常名。无名天地之始。有名万物之母。故常无欲以观其妙。常有欲以观其徼。此两者同出而异名，同谓之玄。玄之又玄，众妙之门。
02.天下皆知美之为美，斯恶矣；皆知善之为善，斯不善已。故有无相生，难易相成，长短相形，高下相倾，音声相和，前後相随。是以圣人处无为之事，行不言之教。万物作焉而不辞。生而不有，为而不恃，功成而弗居。夫唯弗居，是以不去。
"""

""" new
### 第01章
道可道，非常道。名可名，非常名。无名天地之始。有名万物之母。故常无欲以观其妙。常有欲以观其徼。此两者同出而异名，同谓之玄。玄之又玄，众妙之门。
### 第02章
天下皆知美之为美，斯恶矣；皆知善之为善，斯不善已。故有无相生，难易相成，长短相形，高下相倾，音声相和，前後相随。是以圣人处无为之事，行不言之教。万物作焉而不辞。生而不有，为而不恃，功成而弗居。夫唯弗居，是以不去。
"""


with open('old.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

chapters = {}

for i, line in enumerate(lines):
    chapter = line[:2]
    content = line[3:]
    if chapter in chapters:
        chapter_title = chapters[chapter]
        lines[i] = f"## {chapter_title}\n{content}"
    else:
        lines[i] = f"## 第{chapter}章\n{content}"

with open('new.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

---
title: 使用rename命令来实现批量替换当前目录下文件名中的某个字符串
number: 53
url: https://github.com/byronlau/Knowledge-Garden/discussions/53
date: 2023-11-02
createdAt: 2023-11-02T06:12:54Z
lastEditedAt: None
updatedAt: 2023-11-02T06:13:01Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: 使用rename命令来实现批量替换当前目录下文件名中的某个字符串.md
---

在Linux中，你可以使用rename命令来实现批量替换当前目录下文件名中的某个字符串。下面是一些示例命令:

将文件名中的特定字符串替换为空格:
``` bash
rename 's/特定字符串/ /g' *
```
将文件名中的特定字符串替换为其他字符串:
``` bash
rename 's/特定字符串/替换字符串/g' *
```
<!-- more -->
请将特定字符串替换为你想要替换的字符串，将替换字符串替换为你想要替换成的字符串。这些命令会在当前目录下的所有文件名中找到并替换指定的字符串。

**如果执行命令后报如下错误**

**Command 'rename' not found, but can be installed with:**
``` bash 
apt install rename
```
执行  apt install rename 安装工具，即可。


<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="53"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
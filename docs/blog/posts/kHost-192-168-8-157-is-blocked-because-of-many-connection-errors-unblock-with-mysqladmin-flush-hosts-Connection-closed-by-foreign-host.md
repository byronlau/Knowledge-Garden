---
title: kHost '192.168.8.157' is blocked because of many connection errors; unblock with 'mysqladmin flush-hosts'Connection closed by foreign host.
number: 71
url: https://github.com/byronlau/Knowledge-Garden/discussions/71
date: 2023-11-29
createdAt: 2023-11-29T09:40:20Z
lastEditedAt: None
updatedAt: 2023-11-29T09:40:20Z
authors: [byronlau]
categories: 
  - DB
labels: []
filename: kHost-192-168-8-157-is-blocked-because-of-many-connection-errors-unblock-with-mysqladmin-flush-hosts-Connection-closed-by-foreign-host.md
---

程序中的数据库访问被终止，报错
`kHost '192.168.8.157' is blocked because of many connection errors; unblock with 'mysqladmin flush-hosts'Connection closed by foreign host.`  

解决办法
``` shell
mysqladmin -h 127.0.0.1 -u root -p flush-hosts
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="71"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
---
title: Nginx try_files的作用
number: 49
url: https://github.com/byronlau/Knowledge-Garden/discussions/49
date: 2023-11-02
createdAt: 2023-11-02T05:49:32Z
lastEditedAt: None
updatedAt: 2023-11-02T05:49:33Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: Nginx-try-files的作用.md
---

今天遇到了一个问题，部署的应用test.zxj.com， 直接访问域名可以跳转到登录页(test.zxj.com/login)，但是在登录页一点刷新页面，或者直接在地址栏输入test.zxj.com/login，就访问不到。

问题的原因就是nginx的配置中没有配try_files。
``` nginx
location / {  
  root   /opt/atp/dist;  
  index  index.html index.htm;  
  try_files $uri $uri/ /index.html;
}
```
<!-- more -->
（以上配置，root是前端代码存放的路径，前后端分离）


 当用户请求 [http://test.zxj.com/example](https://links.jianshu.com/go?to=http%3A%2F%2Ftest.zxj.com%2Fexample) 时，这里的$uri就是/example。

 try_files 会到硬盘里尝试找这个文件。如果存在名为/$root/example（其中$root是项目代码安装目录）的文件，就直接把这个文件的内容发送给用户。

显然，目录中没有叫 example 的文件。然后就看$uri/，增加了一个 /，也就是看有没有名为/$root/example/的目录。

又找不到，就会 fall back 到 try_files 的最后一个选项 /index.html，发起一个内部 “子请求”，也就是相当于 nginx 发起一个 HTTP 请求到 [http://test.zxj.com/index.html](https://links.jianshu.com/go?to=http%3A%2F%2Ftest.zxj.com%2Findex.html)。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="49"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
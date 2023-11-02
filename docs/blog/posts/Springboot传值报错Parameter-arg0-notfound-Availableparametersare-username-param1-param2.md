---
title: Springboot传值报错Parameter'arg0'notfound.Availableparametersare[username,param1,param2
number: 42
url: https://github.com/byronlau/Knowledge-Garden/discussions/42
date: 2023-11-02
createdAt: 2023-11-02T04:59:47Z
lastEditedAt: None
updatedAt: 2023-11-02T04:59:48Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: Springboot传值报错Parameter-arg0-notfound-Availableparametersare-username-param1-param2.md
---

在对老代码重构过程中发现使用如下方式传参报错 Parameter 'arg0' not found ...

``` java
@Select("SELECT COUNT(*) AS num FROM USER WHERE username=#{arg0} AND PASSWORD=#{arg1}")
public int isUserExists(String username,String password);
```
查阅资料发现如下问题

mybatis从3.4.1开始支持java 8 的反射获取入参名了，所以入参不再是arg0，arg1了，不过仍然可以使用param1，param2的这种形式，在java8 编译时指定 -parameters 选项，可以直接使用#{username} #{password}，而不用改变你的接口入参
<!-- more -->

**参考**
- [mybatis3.4.1更新日志](https://github.com/mybatis/mybatis-3/releases/tag/mybatis-3.4.1)
- [mybatis 传参的七种方式](https://www.yuque.com/liu-yanbo/qyu7gr/fgie8uitbkmc0abq)
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="42"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
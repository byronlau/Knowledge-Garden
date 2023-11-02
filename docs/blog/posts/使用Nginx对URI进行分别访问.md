---
title: 使用Nginx对URI进行分别访问
number: 51
url: https://github.com/byronlau/Knowledge-Garden/discussions/51
date: 2023-11-02
createdAt: 2023-11-02T06:01:17Z
lastEditedAt: None
updatedAt: 2023-11-02T06:01:18Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: 使用Nginx对URI进行分别访问.md
---

## 问题

公司做了两套系统 PC 端和移动端网站，最近做了`Nginx`根据设备标识是否是手机进行 pc 域名 `www` 跳转 移动端域名 m ，配置切换后，导致一些资源丢失，经过排查出现这个问题的原因如下

## 原因

因为手机端适配 PC 页面，有些页面没有开发，移动端内直接使用`www` 进行访问， 在切换设配标识配置后，多次重定向，最终 使用移动端域名访问了没有适配的 URI，因为没有适配，资源访问出现`404`。

## 解决方法

1. `www` 根据设备标识跳转`m` 保留
2. 因为接口数据来源可以使用`www`PC 端，因此`m` 中加入根据`URI` 进行逻辑判断，未做适配的走`www` 的 IP:port 访问，其余的走`m` 的 IP:port 访问，具体实施如下

**ww.conf**

``` nginx
if ($http_user_agent ~* (mobile|nokia|iphone|ipad|android|samsung|htc|blackberry)) {
     rewrite  ^(.*)    http://m.byron.com$1 permanent;
}
```

**m.conf**

``` nginx
location / {  
    if ($uri !~ ^/$|^/a/b\?c=d$|^/e$|^/f/g$|^/h/.+) { 
        proxy_pass http://127.0.0.1:8000;  
        break;  
    }    
    proxy_pass http://http://127.0.0.1:8008;
}
```

临时性的解决方法，最终还是要把工程完善，才对。


<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="51"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
---
title: CDN加速原理，以及上线过程中遇到的一些问题
number: 9
url: https://github.com/byronlau/Knowledge-Garden/discussions/9
date: 2023-11-01
createdAt: 2023-11-01T09:46:21Z
lastEditedAt: 2023-11-02T01:54:22Z
updatedAt: 2023-11-02T01:54:22Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: CDN加速原理-以及上线过程中遇到的一些问题.md
---


## CDN介绍

内容分发网络CDN（Content Delivery Network）是建立并覆盖在承载网之上，由遍布全球的边缘节点服务器群组成的分布式网络。CDN能分担源站压力，避免网络拥塞，确保在不同区域、不同场景下加速网站内容的分发，提高资源访问速度。

由于生产中使用的是阿里云的CDN，详细原理参照阿里云官方文档。

[什么是阿里云CDN](https://help.aliyun.com/zh/cdn/product-overview/what-is-alibaba-cloud-cdn#title_sbn_geq_2ez)

## 加速原理

假设您的加速域名为`www.aliyundoc.com`，接入CDN开始加速服务后，当终端用户在北京发起HTTP请求时，处理流程如下图所示。

![原理](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/0988696361/p352419.png)

1. 当终端用户向`www.aliyundoc.com`下的指定资源发起请求时，首先向Local DNS（本地DNS）发起请求域名`www.aliyundoc.com`对应的IP。
2. Local DNS检查缓存中是否有`www.aliyundoc.com`的IP地址记录。如果有，则直接返回给终端用户；如果没有，则向网站授权DNS请求域名`www.aliyundoc.com`的解析记录。
3. 当网站授权DNS解析`www.aliyundoc.com`后，返回域名的CNAME `www.aliyundoc.com.example.com`。
4. Local DNS向阿里云CDN的DNS调度系统请求域名`www.aliyundoc.com.example.com`的解析记录，阿里云CDN的DNS调度系统将为其分配最佳节点IP地址。
5. Local DNS获取阿里云CDN的DNS调度系统返回的最佳节点IP地址。
6. Local DNS将最佳节点IP地址返回给用户，用户获取到最佳节点IP地址。
7. 用户向最佳节点IP地址发起对该资源的访问请求。
   - 如果该最佳节点已缓存该资源，则会将请求的资源直接返回给用户（步骤8），此时请求结束。
   - 如果该最佳节点未缓存该资源或者缓存的资源已经失效，则节点将会向源站发起对该资源的请求。获取源站资源后结合用户自定义配置的缓存策略，将资源缓存到CDN节点并返回给用户（步骤8），此时请求结束。配置缓存策略的操作方法，请参见[配置缓存过期时间](https://help.aliyun.com/zh/cdn/user-guide/add-a-cache-rule#task-261642)。

> 使用过程中出现的问题

1. 每次上线都需要刷新CDN缓存，否则需要根据配置的策略时间，等缓存自动过期；
2. 也可以提前上线，预热缓存，但对我们来说目前没用处，上线比较频繁，并且测试需要测试；
3. 阿里云CDN，如果开启JS，CSS，HTLM等优化，缓存中的文件，将会给你调整格式并且如果开gzip，代码进行压缩，如果JS 没有使用 `,` 结尾那么代码就可能报错；
4. 就目前使用情况 如果你配置的加速域名是 www.abc.com ,那么只有访问 https://www.abc.com 才会进行加速，如果访问https://abc.com、http://www.abc.com、http://abc.com 则会直接对源站进行访问，如果源站没有配置 abc.com:443/80、www.abc.com:80 那么将会访问无效，因此可以配置相关配置，并且在内部使用访问以上域名端口转发到https://www.abc.com 的加速域名，保证所有流量走CDN。
5.  我在源站配置nginx 配置文件中加入了  一个静态资源访问的location 直接对着源站访问没问题，但是通过CDN，始终无法访问通（404），但是很早之前配置的相同逻辑的location 就可以，由于生产环境，不方便处理，就换了其它方案解决，还没找到具体原因，大概率就是当前目录还未在CDN服务缓存中生效。
6. 使用CDN后使用abc.com 如果不重定向到 www.abc.com  那么有些资源出现跨域的问题，图片没问题，但是视频就跨域了，目前还未找到原因，猜测是浏览器策略的原因。


<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="9"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
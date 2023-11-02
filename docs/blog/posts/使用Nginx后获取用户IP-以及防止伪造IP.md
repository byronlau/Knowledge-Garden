---
title: 使用Nginx后获取用户IP，以及防止伪造IP
number: 50
url: https://github.com/byronlau/Knowledge-Garden/discussions/50
date: 2023-11-02
createdAt: 2023-11-02T05:57:45Z
lastEditedAt: None
updatedAt: 2023-11-02T05:57:46Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: 使用Nginx后获取用户IP-以及防止伪造IP.md
---

## 问题背景

在实际应用中，我们可能需要获取用户的ip地址，比如做异地登陆的判断，或者统计ip访问次数等，通常情况下我们使用request.getRemoteAddr()就可以获取到客户端ip，但是当我们使用了nginx作为反向代理后，使用request.getRemoteAddr()获取到的就一直是nginx服务器的ip的地址，那这时应该怎么办？

<!-- more -->

## 解决方案

我在查阅资料时，有一本名叫《实战nginx》的书，作者张晏，这本书上有这么一段话“经过反向代理后，由于在客户端和web服务器之间增加了中间层，因此web服务器无法直接拿到客户端的ip，通过$remote_addr变量拿到的将是反向代理服务器的ip地址”。这句话的意思是说，当你使用了nginx反向服务器后，在web端使用request.getRemoteAddr()（本质上就是获取$remote_addr），取得的是nginx的地址，即$remote_addr变量中封装的是nginx的地址，当然是没法获得用户的真实ip的，但是，nginx是可以获得用户的真实ip的，也就是说nginx使用$remote_addr变量时获得的是用户的真实ip，如果我们想要在web端获得用户的真实ip，就必须在nginx这里作一个赋值操作，如下：

```nginx
proxy_set_header            X-real-ip $remote_addr;
```

其中这个X-real-ip是一个自定义的变量名，名字可以随意取，这样做完之后，用户的真实ip就被放在X-real-ip这个变量里了，然后，在web端可以这样获取：request.getAttribute("X-real-ip")这样就明白了吧。

## 原理介绍

**参考文章**

- [Nginx指令add_header和proxy_set_header的区别](https://www.yuque.com/liu-yanbo/bcrz/qo8mlfy0dngmkk2y)
- [使用Nginx后如何在web应用中获取用户ip及原理解释](http://www.linuxidc.com/Linux/2012-06/63587.html)

这里我们将nginx里的相关变量解释一下，通常我们会看到有这样一些配置

```nginx
  server {
        listen       88;
        server_name  localhost;

        location /{           
         root   html;            index  
         index.html index.htm;            
         proxy_pass                  http://backend;            
         proxy_redirect              off;
		proxy_set_header            Host $host;            
		proxy_set_header            X-real-ip $remote_addr;           
         proxy_set_header            X-Forwarded-For $proxy_add_x_forwarded_for;
    }
```

我们来一条条的看

**1. proxy_set_header  X-real-ip $remote_addr;**

这句话之前已经解释过，有了这句就可以在web服务器端获得用户的真实ip

但是，实际上要获得用户的真实ip，不是只有这一个方法，下面我们继续看。

**2. proxy_set_header  X-Forwarded-For $proxy_add_x_forwarded_for;**

我们先看看这里有个X-Forwarded-For变量，这是一个squid开发的，用于识别通过HTTP代理或负载平衡器原始IP地址的非rfc标准，如果有做X-Forwarded-For设置的话,每次经过proxy转发都会有记录,格式就是client1, proxy1, proxy2,以逗号隔开各个地址，由于他是非rfc标准，所以默认是没有的，需要强制添加，在默认情况下经过proxy转发的请求，在后端看来远程地址都是proxy端的ip。也就是说在默认情况下我们使用request.getAttribute("X-Forwarded-For")获取不到用户的ip，如果我们想要通过这个变量获得用户的ip，我们需要自己在nginx添加如下配置：

 `proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;`

意思是增加一个$proxy_add_x_forwarded_for到X-Forwarded-For里去，注意是增加，而不是覆盖，当然由于默认的X-Forwarded-For值是空的，所以我们总感觉X-Forwarded-For的值就等于$proxy_add_x_forwarded_for的值，实际上当你搭建两台nginx在不同的ip上，并且都使用了这段配置，那你会发现在web服务器端通过request.getAttribute("X-Forwarded-For")获得的将会是客户端ip和第一台nginx的ip。

**3. $proxy_add_x_forwarded_for**

$proxy_add_x_forwarded_for变量包含客户端请求头中的"X-Forwarded-For"，与$remote_addr两部分，他们之间用逗号分开。

举个例子，有一个web应用，在它之前通过了两个nginx转发，[[www.linuxidc.com](http://www.linuxidc.com/)](http://www.linuxidc.com/) 即用户访问该web通过两台nginx。

在第一台nginx中,使用

```nginx
proxy_set_header      X-Forwarded-For $proxy_add_x_forwarded_for;
```

现在的$proxy_add_x_forwarded_for变量的"X-Forwarded-For"部分是空的，所以只有$remote_addr，而$remote_addr的值是用户的ip，于是赋值以后，X-Forwarded-For变量的值就是用户的真实的ip地址了。

到了第二台nginx，使用

```nginx
proxy_set_header      X-Forwarded-For $proxy_add_x_forwarded_for;
```

现在的$proxy_add_x_forwarded_for变量，X-Forwarded-For部分包含的是用户的真实ip，$remote_addr部分的值是上一台nginx的ip地址，于是通过这个赋值以后现在的X-Forwarded-For的值就变成了“用户的真实ip，第一台nginx的ip”，这样就清楚了吧。

**4. $http_x_forwarded_for**

最后我们看到还有一个$http_x_forwarded_for变量，这个变量就是X-Forwarded-For，由于之前我们说了，默认的这个X-Forwarded-For是为空的，所以当我们直接使用

```nginx
proxy_set_header      X-Forwarded-For $http_x_forwarded_for
```

时会发现，web服务器端使用request.getAttribute("X-Forwarded-For")获得的值是null。如果想要通过request.getAttribute("X-Forwarded-For")获得用户ip，就必须先使用

```nginx
proxy_set_header      X-Forwarded-For $proxy_add_x_forwarded_for;
```

这样就可以获得用户真实ip。

### 补充内容

由于x-forwarded-for可以自己设置值，而且可以设置任意格式值，使用它可能也不能获取真实IP。那么如何处理，才能杜绝这个问题呢？方法是服务器重新配置X-Forward-For为正确的值。我们要做的就是在离用户最近的前端代理上，强制设定X-Forward-For的值，后端所有机器不作任何设置，直接信任并使用前端机器传递过来的X-Forward-For值，即在最前端的Nginx 上设置：

```nginx
location  ~  ^/static {    proxy_pass  ....;    proxy_set_header X-Forward-For $remote_addr ;
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="50"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
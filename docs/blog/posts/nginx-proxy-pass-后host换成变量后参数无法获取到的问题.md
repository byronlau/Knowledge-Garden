---
title: nginx proxy_pass 后host换成变量后参数无法获取到的问题
number: 8
url: https://github.com/byronlau/Knowledge-Garden/discussions/8
date: 2023-11-01
createdAt: 2023-11-01T07:45:41Z
lastEditedAt: None
updatedAt: 2023-11-01T07:45:41Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: nginx-proxy-pass-后host换成变量后参数无法获取到的问题.md
---

### 问题背景

a、b来源的客户端GET访问同一个URL如下所示

> http://api.xxx.com/districtAPI/ip/geo/v1/district/?key=123456abcdef&ip=8.8.8.8

a正常访问，因为要对b访问过来的请求进行限流操作，b会在请求头加入自定义的请求头abc-real-ip来传递用户客户端的真实IP。

### 解决思路

后台部署不同的服务，然后通过Nginx获取是否有请求头abc-real-ip`代理到不同的服务

**最初写法**

```
set $running "127.0.0.1:18087";
if ($http_abc_real_ip){
  set $running "192.168.1.19:18087";
}

location /ip/geo/v1/district/ {
    add_header Access-Control-Allow-Origin $http_Origin always;
    proxy_set_header requestid $request_id;
    proxy_set_header realip $remote_addr;
    proxy_set_header Host $host;
      proxy_pass http://$running/districtAPI/ip/geo/v1/district/;
}
```

这个写法经过测试发现判断abc-real-ip的逻辑是生效了，但是http://api.xxx.com/districtAPI/ip/geo/v1/district/?key=123456abcdef&ip=8.8.8.8 ?后的参数无法获取到，经过分析然后换了一种写法

```
location /ip/geo/v1/district/ {
    add_header Access-Control-Allow-Origin $http_Origin always;
    proxy_set_header requestid $request_id;
    proxy_set_header realip $remote_addr;
    proxy_set_header Host $host;
    proxy_pass http://$running/districtAPI/$request_uri;
}
```

然后就访问正常了

**另一种写法**
nginx 支持在location块中使用if表达式，然后上述写法就可以简化为

```
location /ip/geo/v1/district/ {
    add_header Access-Control-Allow-Origin $http_Origin always;
    proxy_set_header requestid $request_id;
    proxy_set_header realip $remote_addr;
    proxy_set_header Host $host;
    if ($http_abc_real_ip){
    proxy_pass http://192.168.1.19:18087/districtAPI/$request_uri;
    # 匹配成功，然后终止之后的逻辑
    break;
 	 }
   proxy_pass http://127.0.0.1:18087/districtAPI/ip/geo/v1/district/;
}
```

### 问题补充" class="reference-link">问题补充

1. 参数获取失败的原因
2. proxy_pass http://192.168.1.19:18087/districtAPI/$request_uri; 这种写法就可以
3. nginx 如何解析到了abc-real-ip 请求头—> $http_abc_real_ip；
4. java 的HttpServerltRequest 中，如果客户端传入的请求头是abc_real_ip 不是abc-real-ip 则会无法识别到；

![img](https://blog.mgd2008.com/zb_users/upload/2023/05/202305301234242783578.png)nginx proxy_pass 后host换成变量后参数无法获取到的问题
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="8"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
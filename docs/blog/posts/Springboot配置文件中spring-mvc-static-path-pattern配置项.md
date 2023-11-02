---
title: Springboot配置文件中spring.mvc.static-path-pattern配置项
number: 46
url: https://github.com/byronlau/Knowledge-Garden/discussions/46
date: 2023-11-02
createdAt: 2023-11-02T05:16:34Z
lastEditedAt: None
updatedAt: 2023-11-02T05:16:34Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: Springboot配置文件中spring-mvc-static-path-pattern配置项.md
---

Springboot项目中的静态资源文件存放在static文件下面，当通过浏览器访问这些静态文件时，发现必须要添加static作为前缀才能访问，折腾了一番后发现，这个前缀跟 spring.mvc.static-path-pattern 这个配置项有关。

```
spring:
  mvc:    static-path-pattern: /static/
```

**项目中application.yml配置文件中，存在如上配置项时，访问静态资源文件要加static才行，当把这个配置项除掉时，不用加static作为前缀亦可进行正常访问。![image (https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/202307091688879498890392.png).png](https://blog.mgd2008.com/zb_users/upload/2023/07/202307091688879498890392.png)当spring boot自动装配 org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration，当执行到org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration.WebMvcAutoConfigurationAdapter#addResourceHandlers方法时，类org.springframework.boot.autoconfigure.web.WebMvcProperties#staticPathPattern的默认值为 "/**"。如果配置项文件中存在spring.mvc.static-path-pattern 配置项，默认的配置项将会被覆盖。
<!-- more -->
![image (https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/202307091688879471493651.png).png](https://blog.mgd2008.com/zb_users/upload/2023/07/202307091688879471493651.png)

当通过浏览器进行访问时，springMVC使用SimpleUrlHandlerMapping进行路由映射，当执行到方法 org.springframework.web.servlet.handler.AbstractUrlHandlerMapping#lookupHandler 时，将会使用 spring.mvc.static-path-pattern 配置项来匹配url

![image-20231102131309006](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/image-20231102131309006.png)
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="46"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
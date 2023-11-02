---
title: SpringBoot静态资源处理
number: 47
url: https://github.com/byronlau/Knowledge-Garden/discussions/47
date: 2023-11-02
createdAt: 2023-11-02T05:37:52Z
lastEditedAt: None
updatedAt: 2023-11-02T05:37:52Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: SpringBoot静态资源处理.md
---

在web开发中，静态资源的访问是必不可少的，如：图片、js、css 等资源的访问。
spring Boot 对静态资源访问提供了很好的支持，基本使用默认配置就能满足开发需求。

## 一、默认静态资源映射

Spring Boot 对静态资源映射提供了默认配置
<!-- more -->
#### Spring Boot 默认将 /** 所有访问映射到以下目录：

``` properties
classpath:/static
classpath:/publicclasspath:/resourcesclasspath:/META-INF/resources
```

#### 如：在resources目录下新建 public、resources、static 三个目录，并分别放入 a.jpg b.jpg c.jpg 图片

![image.png](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/202307091688881636567804.png)

#### 浏览器分别访问：

http://localhost:8080/a.jpg

http://localhost:8080/b.jpg

http://localhost:8080/c.jpg均能正常访问相应的图片资源。那么说明，Spring Boot 默认会挨个从 public resources static 里面找是否存在相应的资源，如果有则直接返回。

## 二、自定义静态资源映射

在实际开发中，可能需要自定义静态资源访问路径，那么可以继承WebMvcConfigurerAdapter来实现。

### 第一种方式：静态资源配置类

``` java
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurerAdapter;

/**
 * 配置静态资源映射
 *
 * @author sam * @since 2017/7/16
 **/
@Configuration
public class WebMvcConfig extends WebMvcConfigurerAdapter {
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        //将所有/static/** 访问都映射到classpath:/static/ 目录下    
        registry.addResourceHandler("/static/**").addResourceLocations("classpath:/static/");
    }
}
```

#### 重启项目，访问：http://localhost:8080/static/c.jpg能正常访问static目录下的c.jpg图片资源。

### 第二种方式：在application.properties配置

#### 在application.properties中添加配置：

``` properties
spring.mvc.static-path-pattern=/static/**
```

#### 重启项目，访问：http://localhost:8080/static/c.jpg 同样能正常访问static目录下的c.jpg图片资源。

#### 注意：通过spring.mvc.static-path-pattern这种方式配置，会使Spring Boot的默认配置失效，也就是说，/public /resources 等默认配置不能使用。

#### 配置中配置了静态模式为/static/**，就只能通过/static/**来访问。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="47"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
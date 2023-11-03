---
title: SpringBoot 中 WebMvcConfigurationSupport、WebMvcConfigurationAdapter 区别
number: 66
url: https://github.com/byronlau/Knowledge-Garden/discussions/66
date: 2023-11-03
createdAt: 2023-11-03T03:46:37Z
lastEditedAt: None
updatedAt: 2023-11-03T03:46:50Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: SpringBoot-中-WebMvcConfigurationSupport-WebMvcConfigurationAdapter-区别.md
---

```java
1、springboot默认可以访问以下路径文件(见ResourceProperties)：
    classpath:/static
    classpath:/public
    classpath:/resources
    classpath:/META-INF/resources
   当使用了@EnableWebMvc时，默认的静态资源访问无效了因为默认情况下mvc使用的配置是WebMvcAutoConfiguration，加入该配置变成了WebMvcConfigurationSupport
<!-- more -->
2、@EnableWebMvc、WebMvcConfigurationSupport、WebMvcConfigurationAdapter
    @EnableWebMvc=WebMvcConfigurationSupport，使用了@EnableWebMvc注解等于扩展了WebMvcConfigurationSupport但是没有重写任何方法
    @EnableWebMvc+extends WebMvcConfigurationAdapter，在扩展的类中重写父类的方法即可，这种方式会屏蔽springboot的WebMvcAutoConfiguration中的设置
    @EnableWebMvc+extends WebMvcConfigurationSupport 只会使用@EnableWebMvc
    extends WebMvcConfigurationSupport，在扩展的类中重写父类的方法即可，这种方式会屏蔽springboot的@WebMvcAutoConfiguration中的设置
    extends WebMvcConfigurationAdapter，在扩展的类中重写父类的方法即可，这种方式依旧使用springboot的WebMvcAutoConfiguration中的设置
    在springboot2.x中，WebMvcConfigurationAdapter已经过时，通过实现接口WebMvcConfigurer可以替代原有规则
```

在默认情况下，springboot 是启用 WebMvcAutoConfiguration，这点可以在 spring-boot-autoconfigure.jar/META-INF/spring.factories 中看到

```java
org.springframework.boot.autoconfigure.EnableAutoConfiguration=org.springframework.boot.autoconfigure.web.WebMvcAutoConfiguration
```

但是打开 WebMvcAutoConfiguration 可以看到

```java
@Configuration
@ConditionalOnWebApplication
@ConditionalOnClass({ Servlet.class, DispatcherServlet.class,
      WebMvcConfigurerAdapter.class })
@ConditionalOnMissingBean(WebMvcConfigurationSupport.class)
@AutoConfigureOrder(Ordered.HIGHEST_PRECEDENCE + 10)
@AutoConfigureAfter({ DispatcherServletAutoConfiguration.class,
      ValidationAutoConfiguration.class })
public class WebMvcAutoConfiguration
```

其中 @ConditionalOnMissingBean (WebMvcConfigurationSupport.class) 说明，当没有 WebMvcConfigurationSupport 对应的 bean 时，才会使用该配置，所以当我们使用继承 WebMvcConfigurationSupport 的方式类扩展 mvc 时，原有的配置则无效。

同时可以看下 @EnableWebMvc

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Documented
@Import(DelegatingWebMvcConfiguration.class)
public @interface EnableWebMvc {
}
```

其中 @Import (DelegatingWebMvcConfiguration.class) 为该注解的核心，

```java
@Configuration
public class DelegatingWebMvcConfiguration extends WebMvcConfigurationSupport {

   private final WebMvcConfigurerComposite configurers = new WebMvcConfigurerComposite();


   @Autowired(required = false)
   public void setConfigurers(List<WebMvcConfigurer> configurers) {
      if (!CollectionUtils.isEmpty(configurers)) {
         this.configurers.addWebMvcConfigurers(configurers);
      }
   }
```

可以看到，该类也是 WebMvcConfigurationSupport 的子类，但是相对而言，添加了自己的扩展配置，同时从 setConfigurers 可以看到，所有 WebMvcConfigurer 的子类也会被添加到配置中。

![img](http://img.mgd2008.com/4691d1e1710ff4e0bacfcc17a85a883efca.jpg)

其中 WebMvcConfigurerAdapter，也是 WebMvcConfigurer 的子类，这就是为什么我们使用 @EnableWebMvc+WebMvcConfigurer 的方式可以实现 EnableWebMvc 的配置加上自己的配置了。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="66"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
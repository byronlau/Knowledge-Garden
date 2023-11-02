---
title: SpringBoot@PropertySource加载配置文件、@ImportResource导入Spring配置文件
number: 41
url: https://github.com/byronlau/Knowledge-Garden/discussions/41
date: 2023-11-02
createdAt: 2023-11-02T04:09:19Z
lastEditedAt: None
updatedAt: 2023-11-02T04:09:20Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: SpringBoot-PropertySource加载配置文件-ImportResource导入Spring配置文件.md
---

## @PropertySource 加载 properties配置文件

1、通过《Spring Boot  @ConfigurationProperties 、@Value 注值》知道使用“@Value”与“@ConfigurationProperties”可以从全局配置文件“application.properties”或者“application.yml”中取值，然后为需要的属性赋值。

2、当应用比较大的时候，如果所有的内容都当在一个配置文件中，就会显得比较臃肿，同时也不太好理解和维护，此时可以将一个文件拆分为多个，使用 @PropertySource 注解加载指定的配置文件，注解常用属性如下：

<!-- more -->

![](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/1681107494902-681c9415-26c4-4af1-bb9d-93f30c103b2e.png)

3、下面演示使用 @PropertySource 注解 加载类路径下的 user.properties 配置文件，为 User.java POJO 对象的属性赋值。

``` java
/**
 * 用户···实体

 * {@code @Component} 将本来标识为一个 Spring 组件，因为只有是容器中的组件，容器才会为 @ConfigurationProperties 提供此注入功能

 * {@code @PropertySource} 指明加载类路径下的哪个配置文件来注入值

 * {@code @ConfigurationProperties} 表示 告诉 SpringBoot 将本类中的所有属性和配置文件中相关的配置进行绑定；

   prefix = "user1" 表示 将配置文件中 key 为 user 的下面所有的属性与本类属性进行一一映射注入值，如果配置文件中-

   不存在 "user1" 的 key，则不会为 POJO 注入值，属性值仍然为默认值

 * @author wangmaoxiong

 * Created by Administrator on 2018/7/11 0011.

 */

@Component

@PropertySource(value = {"classpath:user.properties"})

@ConfigurationProperties(prefix = "user1")

public class UserProperty {

    private Integer id;

    private String lastName;

    private Integer age;

    private Date birthday;

    private List<String> colorList;

    private Map<String, String> cityMap;

    private Dog dog;
}
```

## @PropertySource 加载 yml 配置文件
1、仍然以为实体对象注入属性值为例进行演示：
``` java 

/**
 * 用户···实体

 * {@code @Component} 将本来标识为一个 Spring 组件，因为只有是容器中的组件，容器才会为 @ConfigurationProperties 提供此注入功能

 * {@code @PropertySource} 指明加载类路径下的哪个配置文件来注入值

   factory：用于指定 @PropertySource 加载 yml 配置文件.

 * {@code @ConfigurationProperties} 表示 告诉 SpringBoot 将本类中的所有属性和配置文件中相关的配置进行绑定；

   prefix = "user" 表示 将配置文件中 key 为 user 的下面所有的属性与本类属性进行一一映射注入值，如果配置文件中-

   不存在 "user" 的 key，则不会为 POJO 注入值，属性值仍然为默认值


 * @author wangmaoxiong

 * Created by Administrator on 2018/7/11 0011.

 */

@Component

@PropertySource(value = {"classpath:user.yml"}, factory = PropertySourceFactory.class)

@ConfigurationProperties(prefix = "user")

public class UserYml {

    private Integer id;

    private String lastName;

    private Integer age;

    private Date birthday;

    private List<String> colorList;

    private Map<String, String> cityMap;

    private Dog dog;

//......

}
```
2、然后提供用于处理 yml 配置文件的属性资源工程如下：
``` java 
import org.springframework.boot.env.YamlPropertySourceLoader;
import org.springframework.core.env.PropertySource;

import org.springframework.core.io.support.DefaultPropertySourceFactory;

import org.springframework.core.io.support.EncodedResource;

import java.io.IOException;

import java.util.List;

/**

 * 用于  @PropertySource 加载 yml 配置文件.

 * @author wangmaoxiong

 * @version 1.0

 * @date 2020/5/25 20:45

 */

public class PropertySourceFactory extends DefaultPropertySourceFactory {

    @Override

    public PropertySource<?> createPropertySource(String name, EncodedResource resource) throws IOException {

        if (resource == null) {

            return super.createPropertySource(name, resource);

        }

        List<PropertySource<?>> sources = new YamlPropertySourceLoader().load(resource.getResource().getFilename(), resource.getResource());

        return sources.get(0);

    }

}
```
## @PropertySource 从本地磁盘加载文件
1、PropertySource 不仅支持加载类路径下的文件，还支持加载本地磁盘上的文件。
``` java 
/**
 * 用户···实体————读取本地磁盘上的配置文件

   @Component  将本来标识为一个 Spring 组件，因为只有是容器中的组件，容器才会为 @ConfigurationProperties 提供此注入功能

   @PropertySource 指明加载类路径下的哪个配置文件来注入值，既可以是类路径下，也可以上磁盘上

   @ConfigurationProperties 表示 告诉 SpringBoot 将本类中的所有属性和配置文件中相关的配置进行绑定；

   * prefix = "user1" 表示 将配置文件中 key 为 user 的下面所有的属性与本类属性进行一一映射注入值，如果配置文件中-

   * 不存在 "user1" 的 key，则不会为 POJO 注入值，属性值仍然为默认值

 * <p>

 * 磁盘路径可以是相对路径，绝对路径，也可以通过系统属性值指定变量

   相对路径，文件在应用根目录下：@PropertySource(value = {"file:userDisk.properties"})

   相对路径，文件在应用根目录下：@PropertySource(value = {"file:./userDisk.properties"})

   绝对路径，在指定的路径下：@PropertySource(value = {"file:D:\\project\\IDEA_project\\yuanyuan\\userDisk.properties"})

   通过系统属性值指定变量：@PropertySource(value = {"file:${user.dir}/userDisk.properties"})

   * user.dir：用户的当前工作目录

 *

 * @author wangmaoxiong

 * Created by Administrator on 2018/7/11 0011.

 */

@Component

@PropertySource(value = {"file:${user.dir}/userDisk.properties"})

@ConfigurationProperties(prefix = "user2")

public class UserDisk {

    private Integer id;

    private String lastName;

    private Integer age;

    private Date birthday;

    private List<String> colorList;

    private Map<String, String> cityMap;

    private Dog dog;
```
2. 磁盘文件(其它 yml、xml格式也是同理)：

@ImportResource 导入Spring 配置文件
1、@ImportResource 注解用来导入 Spring 的配置文件，如核心配置文件 "beans.xml"，从而让配置文件里面的内容生效；

2、如果应用中仍然想采用以前 xml 文件的配置方式，如 "beans.xml" ，则使用 “@ImportResource” 注解轻松搞定。

3、将 @ImportResource 标注在一个配置类上，通常直接放置在应用启动类上，和 @SpringBootApplication 一起即可。
``` java 
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import org.springframework.context.annotation.ImportResource;

/**

 * 应用启动类

 *

 * @ImportResource 必须放置在配置类上，通常放在启动类即可，用 value 指明导入类路径下的那个 Spring 配置文件

 */

@ImportResource(value = {"classpath:beans.xml"})

@SpringBootApplication

public class CocoApplication {

    public static void main(String[] args) {

        SpringApplication.run(CocoApplication.class, args);

    }

}
```
4、然后就可以在类路径下提供原始的 beans.xml 配置文件：
``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans&quot;

       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance&quot;

       xsi:schemaLocation="[http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd"&gt](http://www.springframework.org/schema/beans%C2%A0http://www.springframework.org/schema/beans/spring-beans.xsd%22&gt);


    <!-- 放入到Sping容器中，这是以前Spring的内容，不再累述-->

    <bean id="userService" class="com.lct.service.UserService"/>

</beans>
```
5、启动应用控制台会打印：loading XML bean definitions from class path resource [beans. xml] 表示加载成功。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="41"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
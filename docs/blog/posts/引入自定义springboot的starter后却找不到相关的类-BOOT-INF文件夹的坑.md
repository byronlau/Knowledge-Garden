---
title: 引入自定义springboot的starter后却找不到相关的类（BOOT-INF文件夹的坑）
number: 54
url: https://github.com/byronlau/Knowledge-Garden/discussions/54
date: 2023-11-02
createdAt: 2023-11-02T06:19:58Z
lastEditedAt: None
updatedAt: 2023-11-02T06:19:59Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: 引入自定义springboot的starter后却找不到相关的类-BOOT-INF文件夹的坑.md
---

- 自定义的starter是不能有启动入口的！即：只能作为工具类！类似jdk！  

- 不要把自定义的pom写成了一个可启动的项目哈！  

- 不然install后是引用不到自定义的starter里面的类的！！！  

- 可对比install后的web项目 和 install后的工具类pom ， 生成的jar文件的目录结构是不同的哈！！！  
<!-- more -->

1、工具类pom的jar包结构：

![img](https://cdn.nlark.com/yuque/0/2023/png/28895228/1681097618288-14e05d9b-ca6f-423a-9d2f-cb253dcd61cb.png)



![img](https://cdn.nlark.com/yuque/0/2023/png/28895228/1681097618281-78733552-7bb2-4529-87e2-52e99ddf7ca6.png)

2、 一个完整的[[web项目](https://so.csdn.net/so/search?q=web%E9%A1%B9%E7%9B%AE&spm=1001.2101.3001.7020)](https://so.csdn.net/so/search?q=web项目&spm=1001.2101.3001.7020)的jar包结构：

![img](https://cdn.nlark.com/yuque/0/2023/png/28895228/1681097618328-b11f2f2a-4516-4a9f-8081-6cbacdc9af7e.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/28895228/1681097618341-2d1fbb2c-3a38-480c-8a89-b8d292352de6.png)


## 情景再现：

自定义了一个starter，在idea中 mvn clean package install 安装到了本地仓库，然后在其他项目中引入starter依赖坐标。

![img](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/1681097707177-b3e72fda-7a16-4bf7-8f40-7ceafeca5594.png)

## 问题：里面的类无法使用。下图为引入后的依赖jar。

![img](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/1681097716640-bbb5d27d-48f8-486f-b633-198e40ef6668.png)

## 注意：BOOT-INF导致了下面的包找不到。正确的依赖jar应该如下图所示：

![img](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/1681097716641-d6a87c3b-77f0-41a3-aa7a-7f143b89a53b.png)

## 如何解决：

在自定义的starter项目的pom文件中的maven插件里面设置configuration标签如下即可。

```pom
    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <!--安装到仓库后，引用时不出现 BOOT-INF文件夹（会导致找不到相关类）-->
                <configuration>
                    <skip>true</skip>
                </configuration>
            </plugin>
        </plugins>
    </build>
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="54"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
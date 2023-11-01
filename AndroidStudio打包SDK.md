---
title: AndroidStudio打包SDK
number: 7
url: https://github.com/byronlau/Knowledge-Garden/discussions/7
date: 2023-11-01
createdAt: 2023-11-01T07:41:17Z
lastEditedAt: None
updatedAt: 2023-11-01T09:44:45Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: AndroidStudio打包SDK.md
---

# 前言

公司最近要搞一个安卓的SDK，需要我这边搞一下，由于之前没接触过安卓和Gradle，所以过程中遇到了需要问题，因此记录，总结经验。

# 1. 关于SDK的打包类型的一些介绍

对于SDK来说，其实就是一个辅助工具库，我们可以打成 jar，或者打包成 aar，

- jar: 包只包含了classes文件，不包含资源文件；
- aar: 不仅包含了classes文件，还包含资源文件,并且，aar的这个可以发布到maven库，然后使用者直接通过更改版本号就可以获取到最新的aar文件

打包之后生成的文件地址：

- *.jar 通常生成的目录如下位置，但又不是绝对，我的项目就不是，现在没有考究这个问题

```shell
/build/intermediates/bundles/debug(release)/classes.jar
```

*.aar 目录一般就在如下目录

```shell
/build/outputs/aar/libraryname.aar
```

# 2. 开始创建SDK工程

### 2.1.1. app应用也可以直接打包成SDK，可以参考文章

https://blog.csdn.net/u012556114/article/details/107453116

### 2.1.2. 开始创建SDK工程

1. 正常情况下，是使用新建module开始创建SDK
![image-20231101153628527](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/image-20231101153628527.png)

![img](https://cdn.nlark.com/yuque/0/2023/png/28895228/1686040861082-290c991f-35d6-4f95-ae6c-4d3cf01dd030.png)

创建后的项目结构如下

![img](https://cdn.nlark.com/yuque/0/2023/png/28895228/1686041222104-17ba40f3-a6fc-4506-aa01-108dd39a2c2d.png)

- libs: 存放第三方依赖的位置
- src/java: 工程代码目录
- AnddroidManifest.xml : 是 Android 应用程序的清单文件，它位于应用程序的根目录下。清单文件用于描述应用程序的整体结构和特性，以及声明应用程序所需的权限、组件、服务、权限等信息。
- build.gradle: 
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="7"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
---
title: 记录一次jackson映射实体类出现的问题
number: 60
url: https://github.com/byronlau/Knowledge-Garden/discussions/60
date: 2023-11-02
createdAt: 2023-11-02T09:26:34Z
lastEditedAt: None
updatedAt: 2023-11-02T09:26:35Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: 记录一次jackson映射实体类出现的问题.md
---

在一次使用 **jackson** 进行对象转JSON字符串的过程中，发现JSON每次都是空，即空的JSON对象 `{}`，经过排查是由于之前在使用的时候没有给对象添加set方法:

字段的访问器方法不符合Java Bean 规范：`ObjectMapper`默认使用Java Bean 规范来访问对象的字段和属性。简单来说，实体类对象要有get、set 方法。

<!-- more -->

## java解决jackson泛解决json字符串到实体类时报错：UnrecognizedPropertyException: Unrecognized field

**objectMapper.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false)**是使用Jackson库在Java中配置`ObjectMapper`对象的方法之一。这个配置的目的是告诉`ObjectMapper`在序列化对象时，如果对象是空的

（没有任何字段或属性），则不要抛出异常。

这可以用于避免在序列化空对象时引发`JsonMappingException`异常。默认情况下，`ObjectMapper`会抛出异常以防止意外地序列化空对象。

以下是一个示例代码，演示如何使用`configure()`方法来设置`ObjectMapper`：

```java
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.SerializationFeature;
public class Main {
    public static void main(String[] args) {
        ObjectMapper objectMapper = new ObjectMapper();     
        objectMapper.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false);        
        // 现在可以使用objectMapper进行对象的序列化操作
        // ...   
    }}
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="60"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
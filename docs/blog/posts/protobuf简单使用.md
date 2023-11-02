---
title: protobuf简单使用
number: 35
url: https://github.com/byronlau/Knowledge-Garden/discussions/35
date: 2023-11-02
createdAt: 2023-11-02T03:13:48Z
lastEditedAt: None
updatedAt: 2023-11-02T03:13:49Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: protobuf简单使用.md
---

## 什么是protobuf
它是一个灵活、高效、结构化的序列化数据结构，它与传统的XML、JSON等相比，它更小、更快、更简单。

ProtoBuf是由Google开发的一种数据序列化协议（类似于XML、JSON、hessian）。ProtoBuf能够将数据进行序列化，并广泛应用在数据存储、通信协议等方面。protobuf压缩和传输效率高，语法简单，表达力强。

<!-- more -->

**我们说的 protobuf 通常包括下面三点:**

- 一种二进制数据交换格式。可以将 C++ 中定义的存储类的内容 与 二进制序列串 相互转换，主要用于数据传输或保存；
- 定义了一种源文件，扩展名为 .proto(类比.cpp文件)，使用这种源文件，可以定义存储类的内容；
- protobuf有自己的编译器 protoc，可以将 .proto 编译成.cc文件，使之成为一个可以在 C++ 工程中直接使用的类；

**序列化：将数据结构或对象转换成二进制串的过程。反序列化：将在序列化过程中所产生的二进制串转换成数据结构或对象的过程。**

## 简单使用
### 1. 导入pom依赖
``` xml
<dependency>
    <groupId>io.protostuff</groupId>
    <artifactId>protostuff-core</artifactId>
    <version>1.5.2</version>
</dependency>
<dependency>
    <groupId>io.protostuff</groupId>
    <artifactId>protostuff-runtime</artifactId>
    <version>1.5.2</version>
</dependency>
```
### 2. 举例
``` java 
package com.liuyb.test.Utils;
import cn.hutool.core.util.ArrayUtil;
import com.liuyb.test.entity.Person;
import io.protostuff.LinkedBuffer;
import io.protostuff.ProtobufIOUtil;
import io.protostuff.runtime.RuntimeSchema;

/**
 * @Author: liuyb
 * @Date: 2023/04/08/16:15
 * @Description: 高效的序列化工具 ProtobufIOUtil使用举例
 */
public class ProtobufIOUtilExample {
    public final static RuntimeSchema<Person> schema = RuntimeSchema.createFrom(Person.class);
    /**
     * 序列化
     * @param person
     * @return
     */

    public static byte[] serializer(Person person) {
        return ProtobufIOUtil.toByteArray(person, schema, LinkedBuffer.allocate(LinkedBuffer.DEFAULT_BUFFER_SIZE));

    }

    /**
     * 反序列化
     * @param bytes
     * @return
     */

    public static Person deserializer(byte[] bytes) {
        Person person = schema.newMessage();
        ProtobufIOUtil.mergeFrom(bytes, person, schema);
        return person;
    }

    public static void main(String[] args) {
        Person person = new Person();
        person.setAge(10);
        person.setLastName("牛逼");
        byte[] serializer = serializer(person);
        System.out.println(ArrayUtil.toString(serializer));
        System.out.println(deserializer(serializer));
    }
}
```

<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="35"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
---
title: Go指针的作用和Java中为什么没有用到指针
number: 12
url: https://github.com/byronlau/Knowledge-Garden/discussions/12
date: 2023-11-01
createdAt: 2023-11-01T09:51:29Z
lastEditedAt: 2023-11-02T01:43:38Z
updatedAt: 2023-11-02T01:43:38Z
authors: [byronlau]
categories: 
  - Go
labels: []
filename: Go指针的作用和Java中为什么没有用到指针.md
---

> 在Go语言中，指针是一种特殊的数据类型，它存储了一个变量的内存地址。通过使用指针，可以直接操作该内存地址上的数据，而不是通过变量名来访问。

**指针在Go语言中有以下作用:**
1. 传递内存地址：通过将指针作为参数传递给函数，可以直接修改函数外部的变量，而不是创建一个副本。这对于需要修改大型数据结构或者需要避免大量数据拷贝的情况非常有用。

2. 动态分配内存：使用指针可以在堆上动态分配内存，这样可以创建变量的生命周期不依赖于函数的作用域。这对于创建复杂的数据结构、在函数调用之间保留状态等情况非常有用。

3. 与结构体配合使用：指针可以与结构体配合使用，通过指针访问和修改结构体中的字段，这样可以避免将整个结构体作为参数传递，提高效率。相比之下，Java语言没有显式的指针操作。这是因为Java的设计目标之一是提供一种相对安全和易于使用的编程语言。Java使用引用来实现对对象的引用，而不是直接操作内存地址。通过引用，可以访问和修改Java对象的属性，而无需直接操作内存地址。这种设计决策简化了Java的内存管理，并且有助于减少内存错误和安全漏洞的发生。

总之，Go语言中的指针提供了更多低级别的内存操作功能，而Java语言则通过引用提供了更高级别的抽象和更安全的内存管理。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="12"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
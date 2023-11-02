---
title: 使用Stream 中的Collectors.toMap() 进行分组
number: 48
url: https://github.com/byronlau/Knowledge-Garden/discussions/48
date: 2023-11-02
createdAt: 2023-11-02T05:44:18Z
lastEditedAt: None
updatedAt: 2023-11-02T05:44:19Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: 使用Stream-中的Collectors-toMap-进行分组.md
---

`Collectors.toMap(CallCenterInfo::getType, Function.identity(), (existing, replacement) -> existing)` 是使用 Java 8 中的流式操作的 `Collectors` 类的一个静态方法，用于将流中的元素映射到一个 `Map` 对象中。

<!-- more -->
``` java
 Map<String, List<CallCenterInfo>> collect = callCenterInfos.stream().collect(Collectors.groupingBy(CallCenterInfo::getType)); 
```

因为 `CallCenterInfo` 中的type 不重复，所以最终的Map 可以转化为

``` java
Map<String, CallCenterInfo> collect = callCenterInfos.stream()
                .collect(Collectors.toMap(CallCenterInfo::getType, Function.identity(), (existing, replacement) -> existing));
```

下面是对这个方法各个参数的详细解释：

1. `CallCenterInfo::getType`：这是一个方法引用，用于指定键的提取方式。它表示将 `CallCenterInfo` 对象的 `type` 字段的值作为键。
2. `Function.identity()`：这也是一个方法引用，用于指定值的提取方式。它表示将原始的 `CallCenterInfo` 对象作为值。
3. `(existing, replacement) -> existing`：这是一个合并函数。当遇到具有相同键的元素时，该函数定义如何合并旧值和新值。在这个例子中，使用 `(existing, replacement) -> existing` 表示保留已存在的值，即如果存在重复的键，就保留旧值不替换为新值。

综合起来，`Collectors.toMap(CallCenterInfo::getType, Function.identity(), (existing, replacement) -> existing)` 将会创建一个 `Map` 对象，其中键是 `CallCenterInfo` 对象的 `type` 字段的值，值是对应的 `CallCenterInfo` 对象。同时，当遇到具有相同键的元素时，保留旧值。

需要注意的是，如果存在重复的键并且不使用合并函数 `(existing, replacement) -> existing`，则会抛出 `IllegalStateException` 异常。使用合并函数可以避免这种异常并指定如何处理重复的键。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="48"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
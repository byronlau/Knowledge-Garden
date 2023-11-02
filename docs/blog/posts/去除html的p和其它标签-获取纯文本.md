---
title: 去除html的p和其它标签，获取纯文本
number: 55
url: https://github.com/byronlau/Knowledge-Garden/discussions/55
date: 2023-11-02
createdAt: 2023-11-02T06:22:33Z
lastEditedAt: None
updatedAt: 2023-11-02T06:22:34Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: 去除html的p和其它标签-获取纯文本.md
---

如果 `<p>` 和 `<span>` 标签中包含了样式（style）属性，并且你想要去除这些样式。

首先，我们需要将正则表达式模式修改为匹配包含 style 属性的标签。可以使用` <p.*?>` 和 `<span.*?>` 这样就能匹配到带有样式属性的标签了。

其次，在处理文本片段之前，我们需要将样式属性从标签中移除。可以使用正则表达式的 replaceAll 方法，并传入 style="[^"]*" 作为要替换的模式。这个模式将匹配到 style=" 开头，紧接着是零个或多个非双引号字符（样式属性值），最后以 " 结尾的字符串。将它们替换为空字符串即可移除样式属性。
<!-- more -->
代码如下：
``` java
private static List<String> extractParagraphs(String text) {
    List<String> paragraphList = new ArrayList<>();
    Pattern pattern = Pattern.compile("<p.*?>(.*?)</p>|<span.*?>(.*?)</span>");
    Matcher matcher = pattern.matcher(text);
    while (matcher.find()) {
        String paragraph = matcher.group(1);
        if (paragraph != null && !paragraph.isEmpty()) {
            paragraph = paragraph.replaceAll("</?[^>]+>", "");
            paragraph = paragraph.replaceAll("\\s+", " ");

            // 移除样式属性
            paragraph = paragraph.replaceAll(" style=\"[^\"]*\"", "");

            paragraphList.add(paragraph);
        }
    }
    return paragraphList;
}
```
通过这个修改，代码将会移除 `<p>` 和 `<span>` 标签中的样式属性，将纯文本提取出来存储在 paragraphList 列表中。


<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="55"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
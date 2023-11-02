---
title: 编写Pythonyaml和Json中出现的问题
number: 58
url: https://github.com/byronlau/Knowledge-Garden/discussions/58
date: 2023-11-02
createdAt: 2023-11-02T09:21:02Z
lastEditedAt: None
updatedAt: 2023-11-02T09:21:03Z
authors: [byronlau]
categories: 
  - Python
labels: []
filename: 编写Pythonyaml和Json中出现的问题.md
---

# How do I convert a python list to simple YAML?

[[How do I convert a python list to simple YAML?](https://stackoverflow.com/questions/30778134/how-do-i-convert-a-python-list-to-simple-yaml)](https://stackoverflow.com/questions/30778134/how-do-i-convert-a-python-list-to-simple-yaml)

您必须将以下参数设置为转储功能：

- explicit_start=True对于---输出的开头。
- default_flow_style=False打印每行中分隔的项目。

```python
import yaml
a = ['item 1','item 2','item 3','item 4']yaml.dump(a, explicit_start=True, default_flow_style=False)
```
<!-- more -->
会给你

'---\n- item 1\n- item 2\n- item 3\n- item 4\n'

如果你print输出，你会得到

```yaml
---- item 1- item 2- item 3- item 4
```

## pyYaml 转储选项

使用 pyYaml 为小型数据库迁移项目创建输入文件，我没有找到任何地方描述 yaml.dump 方法接受的关键字属性的详尽列表。这是第一个猜测：

在python-yaml的cyaml.py文件中找到了一些信息。其中一些在 PyYAML 文档页面 ( http://pyyaml.org/wiki/PyYAMLDocumentation%3C/span%3E%3C/a%3E%3Cspan class="ne-text" style="color: #333333; font-size: 12px"> ) 中进行了描述。因此，我不是 YAML 专家，请发表评论以纠正我描述中的误解或错误。

python-yaml 中方法**def dump(data, stream=None, Dumper=Dumper, \**kwds)的有效关键字：**

**default_style**：指示标量的样式。可能的值为None、''、'\''、'"'、'|' , '>'。

**default_flow_style**：指示集合是块还是流。可能的值为None、True、False。

**canonical**：如果为 True 则将标签类型导出到输出文件

**缩进**：设置首选缩进

**width** : 设置首选行宽
**allow_unicode** : 在输出文件中允许unicode

**line_break** : 指定你需要的换行符

**encoding** : 输出编码，默认为utf-8

**explicit_start**：如果为真，则使用“—”添加显式开始

**explicit_end**：如果为真，则使用“—”添加一个明确的结尾

**version**：YAML 解析器的版本，元组（主要，次要），仅支持主要版本 1

**tags**：我没有找到关于这个参数的任何信息……也没有时间测试它 ;-)。

# python读写中文-Python读写文件（json.dump()）中文被转成Unicode问题

如果无任何配置，或者说使用默认配置，输出的会是ASCII字符，而不是真正的中文，这是因为json.dumps 序列化时对中文默认使用的ASCII编码

```python
json.dump(content_json, f, ensure_ascii=False, indent=4)
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="58"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
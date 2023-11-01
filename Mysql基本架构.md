---
title: Mysql基本架构
number: 25
url: https://github.com/byronlau/Knowledge-Garden/discussions/25
date: 2023-11-01
createdAt: 2023-11-01T09:59:23Z
lastEditedAt: None
updatedAt: 2023-11-01T09:59:25Z
authors: [byronlau]
categories: 
  - DB
labels: []
filename: Mysql基本架构.md
---

<section class="output_wrapper" id="output_wrapper_id" style="font-size: 15px; color: rgb(62, 62, 62); line-height: 1.8; word-spacing: 2px; letter-spacing: 2px; font-family: &quot;Helvetica Neue&quot;, Helvetica, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, Arial, sans-serif; background-image: linear-gradient(90deg, rgba(50, 0, 0, 0.05) 3%, rgba(0, 0, 0, 0) 3%), linear-gradient(360deg, rgba(50, 0, 0, 0.05) 3%, rgba(0, 0, 0, 0) 3%); background-size: 20px 20px; background-position: center center;"><p style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px; margin-top: 1.7em; margin-bottom: 1.7em;">我们在使用 <code style="font-size: inherit; line-height: inherit; overflow-wrap: break-word; padding: 2px 4px; border-radius: 4px; margin: 0px 2px; color: rgb(248, 35, 117); background: rgb(248, 248, 248);">MySQL</code> 的时候只是停留在表层我们看到的只是输入一条语句，返回一个结果，却不知道这条语句在 <code style="font-size: inherit; line-height: inherit; overflow-wrap: break-word; padding: 2px 4px; border-radius: 4px; margin: 0px 2px; color: rgb(248, 35, 117); background: rgb(248, 248, 248);">MySQL</code> 内部的执行。下方是 <code style="font-size: inherit; line-height: inherit; overflow-wrap: break-word; padding: 2px 4px; border-radius: 4px; margin: 0px 2px; color: rgb(248, 35, 117); background: rgb(248, 248, 248);">MySQL</code> 的基本架构示意图。<br/></p><figure style="font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;"><img src="http://img.mgd2008.com/FoO8o4lzxSA5oUFv2y8HdDo4xGWC" alt="" title="" style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px; display: block; margin: 0px auto; max-width: 100%;"/><figcaption style="line-height: inherit; margin: 0px; padding: 0px; margin-top: 10px; text-align: center; color: rgb(153, 153, 153); font-size: 0.7em;"></figcaption></figure><br/>大体来说，<code style="font-size: inherit; line-height: inherit; overflow-wrap: break-word; padding: 2px 4px; border-radius: 4px; margin: 0px 2px; color: rgb(248, 35, 117); background: rgb(248, 248, 248);">MySQl</code> 分为 Server 层和存储引擎层<br/>Server 层主要包含：<ol style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px 0px 0px 32px;" class=" list-paddingleft-2"><li><p><span style="font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;">连接器: 管理连接、权限验证</span></p></li><li><p><span style="font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;">查询缓存: 命中则返回结果（8.0 之后删除这个过程）</span></p></li><li><p><span style="font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;">分析器: （要做什么）词法分析、语法分析</span></p></li><li><p><span style="font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;">优化器: （该怎么做）优化器是在表里面有多个索引的时候，决定使用哪个索引；或者在一个语句有多表关联（join）的时候，决定各个表的连接顺序。</span></p></li><li><p><span style="font-size: inherit; color: inherit; line-height: inherit; margin: 0px; padding: 0px;">执行器: 操做引擎，返回结果</span></p></li></ol><p style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px; margin-top: 1.7em; margin-bottom: 1.7em;"><strong style="font-size: inherit; line-height: inherit; margin: 0px; padding: 0px; color: rgb(233, 105, 0);">Server 层</strong>包括连接器、查询缓存、分析器、优化器、执行器等，涵盖 MySQL 的大多数核心服务功能，以及所有的内置函数（如日期、时间、数学和加密函数等），所有跨存储引擎的功能都在这一层实现，比如存储过程、触发器、视图等。</p><p style="font-size: inherit; color: inherit; line-height: inherit; padding: 0px; margin-top: 1.7em; margin-bottom: 1.7em;">而<strong style="font-size: inherit; line-height: inherit; margin: 0px; padding: 0px; color: rgb(233, 105, 0);">存储引擎层</strong>负责数据的存储和提取。其架构模式是插件式的，支持 InnoDB、MyISAM、Memory 等多个存储引擎。现在最常用的存储引擎是 InnoDB，它从 MySQL5.5.5 版本开始成为了默认存储引擎。</p></section>
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="25"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
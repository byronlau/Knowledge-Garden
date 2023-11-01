---
title: Mybatis批量操作
number: 22
url: https://github.com/byronlau/Knowledge-Garden/discussions/22
date: 2023-11-01
createdAt: 2023-11-01T09:57:35Z
lastEditedAt: None
updatedAt: 2023-11-01T09:57:36Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: Mybatis批量操作.md
---

<h1>1、批量添加<br/></h1><pre class="prism-highlight prism-language-markup">&nbsp;&lt;!--&nbsp;批量插入活动表--&gt;

&nbsp;&nbsp;&nbsp;&nbsp;&lt;insert&nbsp;id=&quot;insertBatchActivity&quot;&gt;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;INSERT&nbsp;INTO&nbsp;activity

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activity_id,&nbsp;user_id,&nbsp;create_time

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;VALUES

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;foreach&nbsp;collection=&quot;list&quot;&nbsp;item=&quot;item&quot;&nbsp;separator=&quot;,&quot;&gt;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#{item.activityId},

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;#{item.userId},

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;now()

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/foreach&gt;

&nbsp;&nbsp;&nbsp;&nbsp;&lt;/insert&gt;</pre><h1 style="text-wrap: wrap;">2、批量更新</h1><p><span style="color: #4D4D4D; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-size: 16px; font-variant-ligatures: no-common-ligatures; text-wrap: wrap; background-color: #FFFFFF;">在mybatis的xml文件中，使用foreach动态标签拼接SQL语句，每一条数据的更新语句对应一条</span>update语句，<span style="color: #4D4D4D; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-size: 16px; font-variant-ligatures: no-common-ligatures; text-wrap: wrap; background-color: #FFFFFF;">多条语句最终使用&quot;;&quot;号进行拼接。</span></p><pre class="prism-highlight prism-language-markup">&lt;update&nbsp;id=&quot;updateBatchById&quot;&gt;

&nbsp;&nbsp;&nbsp;&nbsp;&lt;foreach&nbsp;collection=&quot;list&quot;&nbsp;item=&quot;item&quot;&nbsp;separator=&quot;;&quot;&gt;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`t_student`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name`&nbsp;=&nbsp;#{item.name},

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`age`&nbsp;=&nbsp;#{item.age}

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id&nbsp;=&nbsp;#{item.id}

&nbsp;&nbsp;&nbsp;&nbsp;&lt;/foreach&gt;

&lt;/update&gt;</pre><p>---补充</p><pre class="prism-highlight prism-language-bash">Cause:&nbsp;java.sql.SQLException:&nbsp;sql&nbsp;injection&nbsp;violation,&nbsp;multi-statement&nbsp;not&nbsp;allow&nbsp;:&nbsp;update&nbsp;ipplus360_mall.users_library_version_authority&nbsp;set&nbsp;shew&nbsp;=?,updated_time&nbsp;=?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;where&nbsp;user_id=?&nbsp;and&nbsp;library_version&nbsp;=&nbsp;?</pre><p><br/></p><p>解决方法</p><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif, SimHei, SimSun; text-wrap: wrap; background-color: rgb(255, 255, 255); user-select: auto !important; line-height: 24px !important;"><span style="box-sizing: border-box; outline: 0px; user-select: auto !important; font-weight: 700; overflow-wrap: break-word;">1.配置中去掉wall这个filter。</span></p><pre class="prism-highlight prism-language-markup">spring.datasource.druid.filters=config,wall,slf4j</pre><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif, SimHei, SimSun; text-wrap: wrap; background-color: rgb(255, 255, 255); user-select: auto !important; line-height: 24px !important;">改为</p><pre class="prism-highlight prism-language-markup">spring.datasource.druid.filters=config,slf4j</pre><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif, SimHei, SimSun; text-wrap: wrap; background-color: rgb(255, 255, 255); user-select: auto !important; line-height: 24px !important;"><span style="box-sizing: border-box; outline: 0px; user-select: auto !important; font-weight: 700; overflow-wrap: break-word;">2.数据库连接加上&nbsp;&amp;allowMultiQueries=true</span></p><pre class="prism-highlight prism-language-markup">spring.datasource.url&nbsp;=&nbsp;jdbc:mysql://127.0.0.1:3306/test?useSSL=false&amp;zeroDateTimeBehavior=convertToNull&amp;autoReconnect=true&amp;allowMultiQueries=true&amp;characterEncoding=UTF-8&amp;characterSetResults=UTF-8</pre><p><br/></p>
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="22"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
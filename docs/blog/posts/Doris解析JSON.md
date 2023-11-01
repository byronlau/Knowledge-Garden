---
title: Doris解析JSON
number: 10
url: https://github.com/byronlau/Knowledge-Garden/discussions/10
date: 2023-11-01
createdAt: 2023-11-01T09:50:13Z
lastEditedAt: None
updatedAt: 2023-11-01T09:50:13Z
authors: [byronlau]
categories: 
  - DB
labels: []
filename: Doris解析JSON.md
---

<pre class="prism-highlight prism-language-sql">get_json_string(res_data,’$.charge’)&nbsp;&gt;&nbsp;‘true’</pre><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); line-height: 26px; overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-variant-ligatures: no-common-ligatures; white-space: normal; background-color: rgb(255, 255, 255); user-select: auto !important;"><strong>Doris支持json解析函数，提供了3个json解析函数，分别是</strong></p><ul class=" list-paddingleft-2" style="list-style-type: disc;"><li><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); line-height: 26px; overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-variant-ligatures: no-common-ligatures; white-space: normal; background-color: rgb(255, 255, 255); user-select: auto !important;">get_json_int（string，string）</p></li><li><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); line-height: 26px; overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-variant-ligatures: no-common-ligatures; white-space: normal; background-color: rgb(255, 255, 255); user-select: auto !important;">get_json_string（string，string）</p></li><li><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); line-height: 26px; overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-variant-ligatures: no-common-ligatures; white-space: normal; background-color: rgb(255, 255, 255); user-select: auto !important;">get_json_double（string，string）</p></li></ul><p style="box-sizing: border-box; outline: 0px; margin-top: 0px; margin-bottom: 16px; padding: 0px; font-size: 16px; color: rgb(77, 77, 77); line-height: 26px; overflow: auto hidden; overflow-wrap: break-word; font-family: -apple-system, &quot;SF UI Text&quot;, Arial, &quot;PingFang SC&quot;, &quot;Hiragino Sans GB&quot;, &quot;Microsoft YaHei&quot;, &quot;WenQuanYi Micro Hei&quot;, sans-serif; font-variant-ligatures: no-common-ligatures; white-space: normal; background-color: rgb(255, 255, 255); user-select: auto !important;">第一个参数为json字符串，第二个参数为json内的路径。</p><p><br/></p>
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="10"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
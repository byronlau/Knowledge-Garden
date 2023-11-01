---
title: nginx反向代理proxy_passurl后加和不加的区别
number: 30
url: https://github.com/byronlau/Knowledge-Garden/discussions/30
date: 2023-11-01
createdAt: 2023-11-01T10:01:38Z
lastEditedAt: None
updatedAt: 2023-11-01T10:01:39Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: nginx反向代理proxy-passurl后加和不加的区别.md
---

<div class="lake-content" typography="classic"><p id="udad9b1b9" class="ne-p" style="margin-top: 0px; margin-bottom: 0px; padding: 0px; min-height: 24px;"><span class="ne-text" style="color: #23263B; font-size: 16px">在nginx中配置proxy_pass反向代理时，当在后面的url加上了/，相当于是绝对根路径，则nginx不会把location中匹配的路径部分代理走;如果没有/，则会把匹配的路径部分也给代理走。</span></p><p id="uefdf2e92" class="ne-p" style="margin-top: 0px; margin-bottom: 0px; padding: 0px; min-height: 24px;"><span class="ne-text" style="color: #23263B; font-size: 16px">例：访问路径为</span><span class="ne-text" style="color: #23263B; font-size: 16px"> </span><span class="ne-text" style="color: #D83B64; background-color: #F9F2F4; font-size: 12px">/pss/bill.html</span></p><p id="u400769a9" class="ne-p" style="margin-top: 0px; margin-bottom: 0px; padding: 0px; min-height: 24px;"><span class="ne-text" style="color: #23263B; font-size: 16px">当nginx配置文件proxy_pass后边的url带&quot;/&quot;时，代理到后端的路径为：</span><span class="ne-text" style="color: #D83B64; background-color: #F9F2F4; font-size: 12px">http://127.0.0.1:18081/bill.html</span><span class="ne-text" style="color: #23263B; font-size: 16px">，省略了匹配到的</span><span class="ne-text" style="color: #D83B64; background-color: #F9F2F4; font-size: 12px">/pss/</span><span class="ne-text" style="color: #23263B; font-size: 16px">路径；</span></p><pre data-language="nginx" id="zHN64" class="ne-codeblock language-nginx" style="border: 1px solid rgb(232, 232, 232); border-radius: 2px; background-color: rgb(249, 249, 249); padding: 16px; font-size: 13px; color: rgb(89, 89, 89);">location&nbsp;/pss/&nbsp;{

&nbsp;&nbsp;proxy_pass&nbsp;http://127.0.0.1:18081/;

}</pre><p id="u3040f7a8" class="ne-p" style="margin-top: 0px; margin-bottom: 0px; padding: 0px; min-height: 24px;"><span class="ne-text" style="color: #23263B; font-size: 16px">当nginx配置文件proxy_pass后边的url不带&quot;/&quot;时，代理到后端的路径为：</span><span class="ne-text" style="color: #D83B64; background-color: #F9F2F4; font-size: 12px">http://127.0.0.1:18081/pss/bill.html</span><span class="ne-text" style="color: #23263B; font-size: 16px">，连同匹配到的</span><span class="ne-text" style="color: #D83B64; background-color: #F9F2F4; font-size: 12px">/pss/</span><span class="ne-text" style="color: #23263B; font-size: 16px">路径，一起进行反向代理；</span></p><pre data-language="nginx" id="kIdKW" class="ne-codeblock language-nginx" style="border: 1px solid rgb(232, 232, 232); border-radius: 2px; background-color: rgb(249, 249, 249); padding: 16px; font-size: 13px; color: rgb(89, 89, 89);">location&nbsp;/pss/&nbsp;{

&nbsp;&nbsp;proxy_pass&nbsp;http://127.0.0.1:18081;

}</pre><p id="uc96b1609" class="ne-p" style="margin-top: 0px; margin-bottom: 0px; padding: 0px; min-height: 24px;"><span class="ne-text" style="font-size: 16px"></span></p><p id="u80fba07d" class="ne-p" style="margin-top: 0px; margin-bottom: 0px; padding: 0px; min-height: 24px;"><span class="ne-text" style="font-size: 16px"></span></p></div><p><br/></p>
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="30"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
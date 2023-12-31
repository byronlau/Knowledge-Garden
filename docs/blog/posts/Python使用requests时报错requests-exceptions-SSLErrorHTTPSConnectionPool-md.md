---
title: Python使用requests时报错requests.exceptions.SSLErrorHTTPSConnectionPool.md
number: 37
url: https://github.com/byronlau/Knowledge-Garden/discussions/37
date: 2023-11-02
createdAt: 2023-11-02T03:30:33Z
lastEditedAt: None
updatedAt: 2023-11-02T03:30:34Z
authors: [byronlau]
categories: 
  - Python
labels: []
filename: Python使用requests时报错requests-exceptions-SSLErrorHTTPSConnectionPool-md.md
---

**报错如下:**

 <span style="color: red;">requests.exceptions.SSLError: HTTPSConnectionPool(host=‘www.baidu.com’, port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, u’[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:581)’),))</span>

<!-- more -->

错误提示就是上面这样的。首先我找了很多的资料，

有很多人说关闭证书验证（verify=False））可以解决这个问题

或者说是在进行GET时,指定SSL证书.
response = requests.get(‘http://www.baidu.com/’, headers = header, verify=False)
但我用以上两种方法都没有完美解决此问题，而且有些还有后续错误比如InsecureRequestWarning

**正确的做法参考文档资料**

https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings](about:blank)

https://urllib3.readthedocs.io/en/latest/user-guide.html#ssl

只要安装一下几个requests依赖包就可以解决此问题
``` python
pip install cryptography  pip install pyOpenSSL pip install certifi
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="37"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
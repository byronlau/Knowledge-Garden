---
title: Ubuntussh无法连接问题排查
number: 64
url: https://github.com/byronlau/Knowledge-Garden/discussions/64
date: 2023-11-02
createdAt: 2023-11-02T09:41:49Z
lastEditedAt: None
updatedAt: 2023-11-02T09:41:50Z
authors: [byronlau]
categories: 
  - Sundry
labels: []
filename: Ubuntussh无法连接问题排查.md
---

今天我的Ubuntu Linux 笔记本突然别人ssh 无法登录，查看防火墙是关闭状态，并且端口我也开放22了，但就是连不上。后边我突发奇想使用宝塔登录进去看一下，结果宝塔报错如下。

<!-- more -->

![img](https://fastly.jsdelivr.net/gh/byronlau/imgs/doc/202307072219135387034.png)

**原因是：sshd_config配置文件不存在 导致外部无法连接ssh**

### 解决方案:

#### 1.完全卸载

```shell
sudo apt-get remove openssh-server openssh-client --purge -y
```

#### 2. openssh安装

```shell
apt-get install openssh-server openssh-client -y
```

#### 3. openssh重启

```shell
systemctl restart ssh
```

然后就好了

**引用**：[sshd_config 配置文件不存在 导致外部无法连接 ssh](https://www.cnblogs.com/rainsc/p/16804277.html)
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="64"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
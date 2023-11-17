---
title: 新的服务器直接移植旧的tomcat 包，启动程序报错
number: 70
url: https://github.com/byronlau/Knowledge-Garden/discussions/70
date: 2023-11-17
createdAt: 2023-11-17T10:13:34Z
lastEditedAt: 2023-11-17T10:14:05Z
updatedAt: 2023-11-17T10:14:05Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: 新的服务器直接移植旧的tomcat-包-启动程序报错.md
---

## 背景
最近测试环境网络异常，运维建议迁移一台新的，有个服务在启动tomcat的时候，启动失败 `catalina.sh: 1: eval: /projects/middleware/jdk/jre/bin/java: not found`，因为整个tomcat都是从就服务器拷贝过来的，理应没问题，但现在报错，而且报错 java 环境找不到，找不到的java 环境路径，正是旧服务上的，并且因为新服务器上的java 环境我是直接用 apt  命令安装的，整个路径根本就不存在，因为是catalina.sh 第一行报错，但是进入脚本中根本未发现和 /projects/middleware/ 有关的信息，因此通过命令行

``` bash
grep -rnw  -e  '/projects/middleware'
```
查找结果如下
``` bash
root@ubuntu:/projects/apps/mall/tomcat-mall-web/bin# grep -rnw  -e  '/projects/middleware'
setclasspath.sh:3:export JAVA_HOME=/projects/middleware/jdk
setclasspath.sh:4:export JRE_HOME=/projects/middleware/jdk/jre
```
进入 `setclasspath.sh` 果然发现前两行写着
经过注释重启服务，服务 正常启动


<-- more -->
## GPT 给的提示如下

`bin/catalina.sh: 1: eval: /projects/middleware/jdk/jre/bin/java: not found`

这个错误提示表明你在尝试运行Apache Tomcat时遇到了问题。具体的错误原因是找不到你指定的JDK路径下的java可执行文件。

你可以按照以下步骤排查并解决这个问题：

1. 首先确认你的JDK是否正确安装，并且java可执行文件位于你所指定的路径下。你可以通过打开终端并输入which java或where java（Windows系统下）查看当前系统的默认Java解释器的位置。
如果上述步骤中的结果并不是你期望的结果，请修改Tomcat的配置文件catalina.sh或setclasspath.bat（Windows系统下），使其指向正确的Java路径。 在Unix/Linux系统中，你需要找到如下代码段：
``` bash
if [ -z "$CATALINA_HOME" ] ; then
    CATALINA_HOME="$PRGDIR"
fi

if [ ! -r "$CATALINA_HOME"/bin/setenv.sh ]; then
    echo "Cannot find $CATALINA_HOME/bin/setenv.sh"
    exit 1
fi
. "$CATALINA_HOME"/bin/setenv.sh
exec "$_RUNJAVA" $JAVA_OPTS -Djava.endorsed.dirs="$JAVA_ENDORSED_DIRS" -classpath "$CLASSPATH" \
    -Dcatalina.base="$CATALINA_BASE" -Dcatalina.home="$CATALINA_HOME" \
    -Djava.io.tmpdir="$CATALINA_TMPDIR" org.apache.catalina.startup.Bootstrap "$@" start
```
2. 然后修改$_RUNJAVA为你实际的Java路径，例如：/usr/local/jdk/bin/java。
3. 再次运行Apache Tomcat，看看问题是否得到解决。

<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="70"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
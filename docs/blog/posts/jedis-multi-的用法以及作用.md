---
title: jedis.multi();的用法以及作用
number: 17
url: https://github.com/byronlau/Knowledge-Garden/discussions/17
date: 2023-11-01
createdAt: 2023-11-01T09:54:26Z
lastEditedAt: None
updatedAt: 2023-11-01T09:54:26Z
authors: [byronlau]
categories: 
  - NoDB
labels: []
filename: jedis-multi-的用法以及作用.md
---

<head></head><body><h2 id="h2-u524Du8A00"><a class="reference-link" name="前言"></a><span class="header-link octicon octicon-link"></span>前言</h2><blockquote>

<p>本文使用Redis工具Jedis对Redis进行操作<br>在开始正文之前，我们先整理一下，如何使用Jedis对Redis客户端进行操作</p>

</blockquote>

<pre><code class="language-java">package com.ipplus360.api.common.util;



import org.apache.commons.pool2.impl.GenericObjectPoolConfig;

import org.slf4j.Logger;

import org.slf4j.LoggerFactory;

import redis.clients.jedis.Jedis;

import redis.clients.jedis.JedisPool;



import java.util.Set;



/**

 * @Author: byron

 * @Date: 2023/05/05/10:56

 * @Description:

 */

public class RedisUtil {

    private static final Logger LOGGER = LoggerFactory

            .getLogger(RedisUtil.class);

    private final JedisPool jedisPool;



    /**

     * @param host    主机地址

     * @param port    端口

     * @param timeout 超时间（毫秒）

     * @param password 密码

     * @param bd_index 制定数据库索引

     * @throws Exception

     */

    public RedisUtil(String host, int port, String password) throws Exception {

        this.jedisPool = new JedisPool(new GenericObjectPoolConfig(), host, port, timeout, "passward", bd_index);

    }

}

</code></pre>

<h2 id="h2-u6B63u6587"><a class="reference-link" name="正文"></a><span class="header-link octicon octicon-link"></span>正文</h2><blockquote>

<p>Transaction transaction = jedis.multi(); 的用法以及作用</p>

</blockquote>

<p>Jedis 中的行Transaction transaction = jedis.multi();用于初始化一个新的事务对象。</p>

<p>在 Redis 中，事务允许您将多个命令组合在一起并以原子方式执行它们。使用事务的目的是确保事务中的所有命令都成功执行，或者都不应用。</p>

<p>以下是Transaction对象和multi()方法的工作原理：</p>

<h3 id="h3-1-jedis-"><a class="reference-link" name="1.创建Jedis 实例："></a><span class="header-link octicon octicon-link"></span>1.创建Jedis 实例：</h3><p>在使用事务之前，您需要创建该类的一个实例Jedis，它表示与 Redis 服务器的连接。您通常会提供主机和端口信息以连接到 Redis 服务器。<br><mark>如文章最开始</mark></p>

<h3 id="h3-2-"><a class="reference-link" name="2.开始一个事务："></a><span class="header-link octicon octicon-link"></span>2.开始一个事务：</h3><p>一旦你有了实例Jedis，你就可以通过调用multi()实例上的方法来开始一个新的事务。此方法返回该类的一个实例Transaction。</p>

<pre><code class="language-java">Transaction transaction = jedis.multi();

</code></pre>

<p>在事务内排队命令：获取Transaction对象后，可以在事务内将要执行的Redis命令排队。这些命令将存储在队列中，并在提交事务时自动执行。</p>

<pre><code class="language-java">transaction.set("key1", "value1");

transaction.set("key2", "value2");

transaction.del("key3");

</code></pre>

<p>在上面的示例中，我们在事务中对三个命令（ SET、SET和）进行了排队。DEL这些命令将作为一个原子单元一起执行。</p>

<p>执行事务：要执行事务，您需要调用对象Transaction上的方法exec()。此方法返回表示事务中每个命令的结果的对象列表。</p>

<pre><code class="language-java">List&lt;Object&gt; results = transaction.exec();

</code></pre>

<p>该exec()方法将自动执行所有排队的命令。如果事务中的所有命令都成功执行，该exec()方法将返回结果列表。如果任何命令失败或发生错误，事务将回滚并exec()返回null。</p>

<p>处理结果：执行事务后，您可以处理从exec()方法中获得的结果。结果以对象列表的形式返回，其中每个对象代表事务中相应命令的结果。</p>

<pre><code class="language-java">for (Object result : results) {

    // Handle individual command results

}

</code></pre>

<p>您可以遍历结果列表并相应地处理每个命令结果。</p>

<p>请记住在使用完Jedis实例和对象后正确关闭它们以释放资源。Transaction</p>

<pre><code class="language-java">transaction.close();

</code></pre>

<h3 id="h3-3-"><a class="reference-link" name="3.具体实例"></a><span class="header-link octicon octicon-link"></span>3.具体实例</h3><pre><code class="language-java">public void pay(String key, Integer dailyLimit) throws Exception {

        // 自动关闭 redis 客户端

        try (Jedis jedis = jedisPool.getResource()) {

            String val = jedis.get(key);

            // 获取第二天开始时间

            Date startOfDay = DateUtil.ldt2Date(DateUtil.getStartOfTomorrow(null));



            if (StringUtils.isBlank(val)) {

                setExpireByDay(key, "1", startOfDay);

            } else {

                long limitCount = Long.valueOf(val);

                if (limitCount &lt; dailyLimit) {

                    Transaction transaction = jedis.multi();

                        transaction.incr(key);

                        transaction.exec();

                        // 手动关闭事务

                        transaction.close();

                } else {

                    throw new MyRuntimeException(ServiceStatusEnums.DAILY_LIMITED);

                }

            }



        }

    }

</code></pre>

</body>
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="17"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
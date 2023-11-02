---
title: RedisTemplate与StringRedisTemplate的区别
number: 38
url: https://github.com/byronlau/Knowledge-Garden/discussions/38
date: 2023-11-02
createdAt: 2023-11-02T03:39:41Z
lastEditedAt: None
updatedAt: 2023-11-02T03:39:42Z
authors: [byronlau]
categories: 
  - Python
labels: []
filename: RedisTemplate与StringRedisTemplate的区别.md
---

RedisTemplate和StringRedisTemplate的区别如下：

- 两者的关系：StringRedisTemplate继承自RedisTemplate。
- 两者的数据不共通：StringRedisTemplate只能管理StringRedisTemplate里面的数据，RedisTemplate只能管理RedisTemplate中的数据。
- 默认的序列化策略：SDR（即Simple Data Replication，简单数据复制）有两种默认的序列化策略，一种是String的序列化策略，一种是JDK的序列化策略。StringRedisTemplate默认采用的是String的序列化策略，保存的key和value都是采用此策略序列化保存的。而RedisTemplate默认采用的是JDK的序列化策略，保存的key和value都是采用此策略序列化保存的。

<!-- more -->

**配置两者对象**
``` java
package com.ipplus360.bms.config;
import com.fasterxml.jackson.annotation.JsonAutoDetect;

import com.fasterxml.jackson.annotation.JsonTypeInfo;

import com.fasterxml.jackson.annotation.PropertyAccessor;

import com.fasterxml.jackson.databind.ObjectMapper;

import com.fasterxml.jackson.databind.jsontype.impl.LaissezFaireSubTypeValidator;

import lombok.extern.slf4j.Slf4j;

import org.springframework.cache.CacheManager;

import org.springframework.cache.annotation.EnableCaching;

import org.springframework.context.annotation.Bean;

import org.springframework.context.annotation.Configuration;

import org.springframework.data.redis.cache.RedisCacheConfiguration;

import org.springframework.data.redis.cache.RedisCacheManager;

import org.springframework.data.redis.connection.RedisConnectionFactory;

import org.springframework.data.redis.connection.lettuce.LettuceConnectionFactory;

import org.springframework.data.redis.core.RedisTemplate;

import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;

import org.springframework.data.redis.serializer.RedisSerializationContext;

import org.springframework.data.redis.serializer.StringRedisSerializer;

import java.time.Duration;

@Slf4j

@Configuration

@EnableCaching  //开启spring-cache

public class RedisConfig {

    // 使用Jackson2JsonRedisSerialize 替换默认序列化

    @Bean

    public Jackson2JsonRedisSerializer<Object> jackson2JsonRedisSerializer() {

        Jackson2JsonRedisSerializer<Object> jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer<Object>(Object.class);


        ObjectMapper objectMapper = new ObjectMapper();

        objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);

        objectMapper.activateDefaultTyping(LaissezFaireSubTypeValidator.instance, ObjectMapper.DefaultTyping.NON_FINAL, JsonTypeInfo.As.WRAPPER_ARRAY);


        jackson2JsonRedisSerializer.setObjectMapper(objectMapper);

        return jackson2JsonRedisSerializer;

    }

   
    /**

    * redisTemplate 默认使用JDK的序列化机制, 存储二进制字节码, 所以自定义序列化类



    * @param redisConnectionFactory redis连接工厂类

    * @return RedisTemplate

    */

    @Bean

    public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory redisConnectionFactory, Jackson2JsonRedisSerializer<Object> jackson2JsonRedisSerializer) {

        RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();

        redisTemplate.setConnectionFactory(redisConnectionFactory);

        // 设置value的序列化规则和 key的序列化规则

        redisTemplate.setKeySerializer(new StringRedisSerializer());

        redisTemplate.setValueSerializer(jackson2JsonRedisSerializer);

        redisTemplate.afterPropertiesSet();

        return redisTemplate;

    }


    /**

    * redis缓存管理器


    * @param factory

    * @param jackson2JsonRedisSerializer

    * @return

    */

    @Bean

    public CacheManager cacheManager(RedisConnectionFactory factory, Jackson2JsonRedisSerializer<Object> jackson2JsonRedisSerializer) {

        // 配置序列化（解决乱码的问题）

        RedisCacheConfiguration config = RedisCacheConfiguration.defaultCacheConfig()

            // 缓存有效期

            .entryTtl(Duration.ofHours(1))

            // 使用StringRedisSerializer来序列化和反序列化redis的key值

            .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(new StringRedisSerializer()))

            // 使用Jackson2JsonRedisSerializer来序列化和反序列化redis的value值

            .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(jackson2JsonRedisSerializer))

            // 禁用空值

            .disableCachingNullValues();


        return RedisCacheManager.builder(factory)

            .cacheDefaults(config)

            .build();

    }

    

    @Bean(name = "redisTemplate_db2")

    public RedisTemplate<String, String> redisTemplate2(LettuceConnectionFactory factory) {

        LettuceConnectionFactory lettuceConnectionFactory = new LettuceConnectionFactory(factory.getStandaloneConfiguration(), factory.getClientConfiguration());

        lettuceConnectionFactory.setDatabase(2);

        lettuceConnectionFactory.afterPropertiesSet();

        RedisTemplate<String, String> redisTemplate = new RedisTemplate<>();

        redisTemplate.setConnectionFactory(lettuceConnectionFactory);

        // 设置value的序列化规则和 key的序列化规则

        redisTemplate.setKeySerializer(new StringRedisSerializer());

        redisTemplate.setValueSerializer(new StringRedisSerializer());

        redisTemplate.afterPropertiesSet();

        return redisTemplate;

    }

}
``` 
引用：[RedisTemplate与StringRedisTemplate的区别](https://blog.csdn.net/weixin_42140580/article/details/85211887)































































































































































































































































































































































































<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="38"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
---
title: redis分布式锁的实现
number: 39
url: https://github.com/byronlau/Knowledge-Garden/discussions/39
date: 2023-11-02
createdAt: 2023-11-02T03:42:21Z
lastEditedAt: 2023-11-02T03:48:34Z
updatedAt: 2023-11-02T03:48:34Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: redis分布式锁的实现.md
---

Java 版本的基于Jedis 的 Redis 分布式锁实现
<!-- more -->

### 锁实现
``` java 
 private static final String LOCK_SUCCESS = "OK";
    private static final String SET_IF_NOT_EXIST = "NX";
    private static final String SET_WITH_EXPIRE_TIME = "PX";

    public boolean tryGetDistributedLock(String lockKey, String requestId, int expireTime) {
        try (Jedis resource = jedisPool.getResource()) {
            String result = resource.set(lockKey, requestId, SET_IF_NOT_EXIST, SET_WITH_EXPIRE_TIME, expireTime);
            if (LOCK_SUCCESS.equals(result)) {
                return true;
            }
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
        return false;
    }

    /**
     * 释放锁 - 利用lua脚本
     */
    public boolean unLockByLua(String lockKey, String requestId) {
        String script = "if redis.call('get', KEYS[1]) == ARGV[1] then return redis.call('del', KEYS[1]) else return 0 end";
        try (Jedis resource = jedisPool.getResource()) {
            Object result = resource.eval(script, Collections.singletonList(lockKey), Collections.singletonList(requestId));
            if (Objects.equals(1, result)) {
                return true;
            }
        }
        return false;
    }
``` 
### 使用方式
``` java
try{

    if(!tryGetDistributedLock(lock,requestId,timeout)){
         throw new MyException("锁等待",403);
    }
       ...需要锁的内容
    }catch(Exception e){
       ...异常捕捉
    }finnaly{
       unLockByLua(lockKey,requestId);
}
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="39"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
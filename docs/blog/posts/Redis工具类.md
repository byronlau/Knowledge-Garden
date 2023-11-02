---
title: Redis工具类
number: 40
url: https://github.com/byronlau/Knowledge-Garden/discussions/40
date: 2023-11-02
createdAt: 2023-11-02T03:44:47Z
lastEditedAt: None
updatedAt: 2023-11-02T03:44:47Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: Redis工具类.md
---

Java 版本的Redis 工具类
<!-- more -->
``` java
public final class RedisUtil {

    //Redis服务器IP
    private static String ADDR;

    //Redis的端口号
    private static int PORT;

    //访问密码
    private static String AUTH;

    //可用连接实例的最大数目，默认值为8；
    //如果赋值为-1，则表示不限制；如果pool已经分配了maxActive个jedis实例，则此时pool的状态为exhausted(耗尽)。
    private static int MAX_ACTIVE;

    //控制一个pool最多有多少个状态为idle(空闲的)的jedis实例，默认值也是8。
    private static int MAX_IDLE;

    //等待可用连接的最大时间，单位毫秒，默认值为-1，表示永不超时。如果超过等待时间，则直接抛出JedisConnectionException；
    private static int MAX_WAIT;

    private static int TIMEOUT;

    //在borrow一个jedis实例时，是否提前进行validate操作；如果为true，则得到的jedis实例均是可用的；
    private static boolean TEST_ON_BORROW = true;

    private static JedisPool jedisPool = null;


    /**
     * 初始化Redis连接池
     */
    static {
        Resource resource = new ClassPathResource("config/redis.properties");
        Properties props = null;
        try {
            props = PropertiesLoaderUtils.loadProperties(resource);
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            ADDR = props.getProperty("redis.ip");
            PORT = Integer.valueOf(props.getProperty("redis.port")).intValue();
            AUTH = props.getProperty("redis.pass");
            TIMEOUT = Integer.valueOf(props.getProperty("redis.timeout")).intValue();
            MAX_ACTIVE = Integer.valueOf(props.getProperty("redis.pool.maxTotal")).intValue();
            MAX_IDLE = Integer.valueOf(props.getProperty("redis.pool.maxIdle")).intValue();
            MAX_WAIT = Integer.valueOf(props.getProperty("redis.pool.maxWaitMillis")).intValue();
            TEST_ON_BORROW = Boolean.parseBoolean(props.getProperty("redis.pool.testOnBorrow"));

            JedisPoolConfig config = new JedisPoolConfig();
            config.setMaxIdle(MAX_IDLE);
            config.setMaxTotal(MAX_ACTIVE);
            config.setMaxWaitMillis(MAX_WAIT);
            config.setTestOnBorrow(TEST_ON_BORROW);
            if(StringUtil.isBlank(AUTH)){
                jedisPool = new JedisPool(config, ADDR, PORT, TIMEOUT);
            }else{
                jedisPool = new JedisPool(config, ADDR, PORT, TIMEOUT, AUTH);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * 获取Jedis实例
     * @return
     */
    public synchronized static Jedis getJedis() {
        try {
            if (jedisPool != null) {
                Jedis resource = jedisPool.getResource();
                return resource;
            } else {
                return null;
            }
        } catch (Exception e) {
            System.out.println("Redis异常:" + e.getMessage());
            return null;
        }
    }

    /***
     * 回收一个jedis对象到连接池
     * @param jedis
     */
    public static void gc(Jedis jedis){
        if (jedis != null && jedisPool !=null) {
            jedisPool.returnResource(jedis);
        }
    }

    /**
     * 添加元素，将一个或多个 member 元素及其 score 值加入到有序集 key 当中。
     * @param key
     * @return
     */
    public static Long zAdd(String key, Map<String, Double> scoreMembers){
        Jedis jedis = null;
        try {
            jedis = getJedis();
            if(jedis != null){
                return jedis.zadd(key, scoreMembers);
            }
        }catch(Exception e) {
        }finally{
            gc(jedis);
        }
        return 0L;
    }

    /**
     * 返回有序集 key 中，指定区间内的成员。
     * 其中成员的位置按 score 值递增(从小到大)来排序。
     * 具有相同 score 值的成员按字典序(lexicographical order )来排列。
     * 如果你需要成员按 score 值递减(从大到小)来排列，请使用 ZREVRANGE 命令。
     * 下标参数 start 和 stop 都以 0 为底，也就是说，以 0 表示有序集第一个成员，以 1 表示有序集第二个成员，以此类推。
     * 你也可以使用负数下标，以 -1 表示最后一个成员， -2 表示倒数第二个成员，以此类推。
     * @param key
     * @param start
     * @param end
     * @return
     */
    public static Set<String> zRange(String key, long start, long end){
        Jedis jedis = null;
        try {
            jedis = getJedis();
            if(jedis != null){
                return jedis.zrange(key, start, end);
            }
        }catch(Exception e) {
        }finally{
            gc(jedis);
        }
        return null;
    }

    public static Set<String> zRevrange(String key, long start, long end){
        Jedis jedis = null;
        try {
            jedis = getJedis();
            if(jedis != null){
                return jedis.zrevrange(key, start, end);
            }
        }catch(Exception e) {
        }finally{
            gc(jedis);
        }
        return null;
    }

    /**
     * 为有序集 key 的成员 member 的 score 值加上增量 increment 。
     * 可以通过传递一个负数值 increment ，让 score 减去相应的值，比如 ZINCRBY key -5 member ，就是让 member 的 score 值减去 5 。
     * 当 key 不存在，或 member 不是 key 的成员时， ZINCRBY key increment member 等同于 ZADD key increment member 。
     * 当 key 不是有序集类型时，返回一个错误。
     * @param key
     * @param score
     * @param value
     * @return
     */
    public static Double zIncrby(String key, double score, String value){
        Jedis jedis = null;
        try {
            jedis = getJedis();
            if(jedis != null){
                return jedis.zincrby(key, score, value);
            }
        }catch(Exception e) {
        }finally{
            gc(jedis);
        }
        return 0D;
    }

    private static final String LOCK_SUCCESS = "OK";
    /**
     * NX ：只在键不存在时，才对键进行设置操作。 SET key value NX 效果等同于 SETNX key value
     * XX ：只在键已经存在时，才对键进行设置操作。
     */
    private static final String SET_IF_NOT_EXIST = "NX";
    /**
     * PX millisecond ：设置键的过期时间为 millisecond 毫秒
     * EX second ：设置键的过期时间为 second 秒
     */
    private static final String SET_WITH_EXPIRE_TIME = "PX";

    /**
     * 尝试获取分布式锁
     * @param lockKey 锁
     * @param value 请求标识
     * @param expireTime 超期时间
     * @return 是否获取成功
     */
    public static boolean tryGetDistributedLock(String lockKey, String value, int expireTime){
        Jedis jedis = null;
        String result = "";
        try {
            jedis = getJedis();
            if(jedis != null){
                result = jedis.set(lockKey, value, SET_IF_NOT_EXIST, SET_WITH_EXPIRE_TIME, expireTime);
            }
        }catch(Exception e) {
        }finally{
            gc(jedis);
        }
        return LOCK_SUCCESS.equals(result);
    }
}

/**
 * 解锁
 */
public static Long del(String key){
        Jedis jedis = null;
        try {
            jedis = getJedis();
            if(jedis != null){
                return jedis.del(key);
            }
        }catch(Exception e) {

        }finally{
            gc(jedis);
        }
        return 0L;
    }
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="40"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
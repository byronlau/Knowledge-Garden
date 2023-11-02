---
title: 记一次AndroidSDK开发经验
number: 59
url: https://github.com/byronlau/Knowledge-Garden/discussions/59
date: 2023-11-02
createdAt: 2023-11-02T09:23:40Z
lastEditedAt: 2023-11-02T09:24:01Z
updatedAt: 2023-11-02T09:24:01Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: 记一次AndroidSDK开发经验.md
---

## libs 引入第三方包，build.gradle 的写法 

```gradle
dependencies {
    implementation fileTree(dir: 'libs',includes: ['.jar','.aar'])
}
```

## Android 异常 android.os.NetworkOnMainThreadException
<!-- more -->
**安卓项目在请求时出现这个异常**

Caused by: android.os.NetworkOnMainThreadException

**官方的解释如下:**

```bash
Class OverviewThe exception that is thrown when an application attempts to perform a networking operation on its main thread. This is only thrown for applications targeting the Honeycomb SDK or higher. Applications targeting earlier SDK versions are allowed to do networking on their main event loop threads, but it's heavily discouraged. See the document Designing for Responsiveness. Also see StrictMode.
```

上面的意思是，从SDK3.0开始，google不再允许网络请求（HTTP、Socket）等相关操作直接在主线程中，其实本来就不应该这样做，直接在UI线程进行网络操作，会阻塞UI、用户体验不好。
也就是说，在SDK3.0以下的版本，还可以继续在主线程里这样做，在3.0以上，就不行了。

**解决办法**

```java
Thread thread = new Thread(new Runnable() {
    @Override
    public void run() {
        try  {
            //Your code goes here(请求)
        } catch (Exception e) {
            e.printStackTrace();        
        }    
    }});thread.start();
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="59"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
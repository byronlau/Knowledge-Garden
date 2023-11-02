---
title: SpringBoot自带了一个轻量级的HTTP客户端工具
number: 45
url: https://github.com/byronlau/Knowledge-Garden/discussions/45
date: 2023-11-02
createdAt: 2023-11-02T05:10:04Z
lastEditedAt: None
updatedAt: 2023-11-02T05:10:05Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: SpringBoot自带了一个轻量级的HTTP客户端工具.md
---

Spring Boot自带了一个轻量级的HTTP客户端工具，该工具基于Java的标准HTTP库  `java.net.URLConnection`。您可以使用它来发送HTTP请求并与外部的HTTP资源进行通信。

下面是使用Spring Boot默认的HTTP工具进行HTTP请求的基本示例：
``` java 
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

public class HttpClientExample {
    public static void main(String[] args) {
        RestTemplate restTemplate = new RestTemplateBuilder().build();

        // 发送GET请求
        ResponseEntity<String> response = restTemplate.getForEntity("https://api.example.com/users", String.class);
        System.out.println(response.getBody());

        // 发送POST请求
        String requestBody = "{\"username\": \"test\", \"password\": \"123456\"}";
        ResponseEntity<String> postResponse = restTemplate.postForEntity("https://api.example.com/login", requestBody, String.class);
        System.out.println(postResponse.getBody());
    }
}
```
上述代码中使用了RestTemplate类来发送HTTP请求。您可以使用getForEntity()发送GET请求，postForEntity()发送POST请求等。这里的请求URL可以根据您的实际需求进行修改。

请注意，从Spring 5.0版本开始，RestTemplate已经被宣布为过时，并在将来的Spring版本中将被移除。官方推荐使用WebClient作为替代方案，它提供了更先进的异步非阻塞特性。因此，如果您使用的是较新的Spring Boot版本，可以考虑使用WebClient类来发送HTTP请求。
``` java 
import org.springframework.web.reactive.function.client.WebClient;

public class HttpClientExample {
    public static void main(String[] args) {
        WebClient client = WebClient.create();

        // 发送GET请求
        client.get()
                .uri("https://api.example.com/users")
                .retrieve()
                .bodyToMono(String.class)
                .subscribe(System.out::println);

        // 发送POST请求
        String requestBody = "{\"username\": \"test\", \"password\": \"123456\"}";
        client.post()
                .uri("https://api.example.com/login")
                .bodyValue(requestBody)
                .retrieve()
                .bodyToMono(String.class)
                .subscribe(System.out::println);
    }
}
```
在此示例中，我们使用WebClient类来发送GET和POST请求。.uri()方法用于设置请求的URL，.retrieve()用于发起请求，.bodyToMono()用于解析响应体的内容。
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="45"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
---
title: 使用pageHelper，在对数据进行对象转换或者使用stream操作之后分页失效
number: 5
url: https://github.com/byronlau/Knowledge-Garden/discussions/5
date: 2023-10-30
createdAt: 2023-10-30T07:35:24Z
lastEditedAt: 2023-10-31T00:20:05Z
updatedAt: 2023-10-31T00:20:05Z
authors: [byronlau]
categories: 
  - 乱弹
labels: []
filename: 使用pageHelper-在对数据进行对象转换或者使用stream操作之后分页失效.md
---

> 使用pagehelper，在对数据进行对象转换或者使用stream操作之后分页失效

### 问题描述
使用MyBatis-Plus操作数据库，使用PageHelper插件进行分页操作，直接返回Mapper的分页查询结果数据时分页状态正常，对数据对象进行转换后返回转换后的list则分页出现异常，分页数据的total变成当前返回数据list的size，页数始终为1
```java
PageHelper.startPage(1, 10);
List<Data> datas = dataService.finddataList();
// 使用stream处理数据 或者 对象转换dataList = datas.stream().xxxxx;
return new PageInfo<>(dataList);
```
### 问题排查
【第一步】：分页查询
分页查询的时候，得到的datas是一个特殊的ArrayList，Page对象，在源码中可以看到
```java 
public class Page<E> extends ArrayList<E> implements Closeable {

}
```
【第二步】：返回PageInfo对象 在返回PageInfo对象的时候，源码中会做如下判断
```java
public PageInfo(List list, int navigatePages) {
    super(list);
    this.isFirstPage = false;
    this.isLastPage = false;
    this.hasPreviousPage = false;
    this.hasNextPage = false;
    if (list instanceof Page) {
        // Page 对象           
        Page page = (Page) list;
        this.pageNum = page.getPageNum();
        // 正常的pageNum、pageSize 等返回结果            
        this.pageSize = page.getPageSize();
        this.pages = page.getPages();
        this.size = page.size();
        if (this.size == 0) {
            this.startRow = 0L;
            this.endRow = 0L;
        } else {
            this.startRow = page.getStartRow() + 1L;
            this.endRow = this.startRow - 1L + (long) this.size;
        }
    } else if (list instanceof Collection) {
        // 非Page 对象  
        this.pageNum = 1;
        // pageNum 设置为了1  
        this.pageSize = list.size();
        // pageSzie 被设置为了列表元素数 
        this.pages = this.pageSize > 0 ? 1 : 0;
        this.size = list.size();
        this.startRow = 0L;
        this.endRow = list.size() > 0 ? (long) (list.size() - 1) : 0L;
    }
    if (list instanceof Collection) {
        this.calcByNavigatePages(navigatePages);
    }
}
```
【结论】由于使用stream和类型转换之后对被象收集为了普通的ArrayList对象，并不是Page对象，所以在第二步返回时被判定为非page对象，被当做一个普通的ArrayList设置了pageNum(写死为第一页了)、total等，所以分页就失效了 stream把可正常分页的Page对象(ArrayList的子对象)，转换成了不能分页的ArrayList对象

### 解决方法
```java 
Page<MessageVo> messageVos = new Page<>();  
BeanUtils.copyProperties(messages, messageVos);
messages.forEach(n -> {     
MessageVo nVo = new MessageVo(); 
nVo.setType(n.getType());     
nVo.setTitle(n.getTitle());  
....      messageVos.add(nVo); 
}); 
PageInfo<MessageVo> pageInfo = new PageInfo<>(messageVos);  
return pageInfo;
```


1. 首先新建一个Page<Vo>对象；
2. 将分页查询出来的分页属性结果拷贝进Page中；
3. 增强 for 设置视图属性；
4. 将视图结果放入PageInfo；

<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="5"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
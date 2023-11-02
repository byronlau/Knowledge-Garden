---
title: mybatis传参的七种方式
number: 21
url: https://github.com/byronlau/Knowledge-Garden/discussions/21
date: 2023-11-01
createdAt: 2023-11-01T09:57:14Z
lastEditedAt: 2023-11-02T05:05:54Z
updatedAt: 2023-11-02T05:05:54Z
authors: [byronlau]
categories: 
  - Java
labels: []
filename: mybatis传参的七种方式.md
---

> 在实际开发过程中，增删改查操作都要涉及到请求参数的传递，今天这节就集中讲下在mybatis中传递参数的7中方法

单个参数的传递很简单没有什么好将的，这里主要说下多个参数的传递
<!-- more -->
### 1.第一种方式 匿名参数 顺序传递参数

**controller**

```java
@ApiOperation(value = "多个参数查询_匿名顺序传参")
@GetMapping("findByParams")
public ResultMsg findByParams(Short gender,String age)
{
    List result= employeeMapper.selectByGenderAndAge(gender,age);
    return ResultMsg.getMsg(result);
}
```

**mapper**

```java
List<Employee> selectByGenderAndAge(Short gender,String age );
```

**xml**

```xml
<select id="selectByGenderAndAge" resultMap="BaseResultMap" >
  select * from employee where gender = #{gender} and age = #{age}
</select>
```

注意这里按参数名去引用的话会报如下错误，mybatis错误提示很细致，这里明确给我们提示，匿名参数只能使用arg1, arg0, param1, param2 类似的形式这种传参方式的缺点是不够灵活，必须严格按照参数顺序来引用

```java
BindingException: Parameter 'gender' not found. Available parameters are [arg1, arg0, param1, param2] 
```

> 所以正确的引用方式如下：

```xml
 <select id="selectByGenderAndAge" resultMap="BaseResultMap" >
    select *  from employee where gender = #{param1} and age = #{param2}
  </select>
```

> mybatis从3.4.1开始支持java 8 的反射获取入参名了，所以入参不再是arg0，arg1了，不过仍然可以使用param1，param2的这种形式，在java8 编译时指定 -parameters 选项，可以直接使用#{username} #{password}，而不用改变你的接口入参
> 参考mybatis3.4.1更新日志：https://github.com/mybatis/mybatis-3/releases/tag/mybatis-3.4.1

### 2.第二种方式 使用@Param注解

**controller**

```java
@ApiOperation(value = "多个参数查询_注解方式传参")
@GetMapping("findByParams2")
public ResultMsg findByParams2(Short gender,String age)
{
    List result= employeeMapper.selectByGenderAndAge2(gender,age);
    return ResultMsg.getMsg(result);
}
```

**mapper**

> 使用@Param注解显示的告诉mybatis参数的名字，这样在xml中就可以按照参数名去引用了

```java
List<Employee> selectByGenderAndAge( @Param("gender") Short gender,@Param("age") String age );
```

**xml**

```xml
<select id="selectByGenderAndAge" resultMap="BaseResultMap" >
  select * from employee where gender = #{gender} and age = #{age}
</select>
```

### 3.使用Map传递参数

实际开发中使用map来传递多个参数是一种推荐的方式

**controller**

```java
@ApiOperation(value = "多个参数查询")
@GetMapping("findByMapParams")
public ResultMsg findByMapParams(Short gender,String age)
{
    Map params = new HashMap<>();
    params.put("gender",gender);
    params.put("age",age);
    List result= employeeMapper.selectByMapParams(params);
    return ResultMsg.getMsg(result);
}
```

**mapper**

```java
List<Employee> selectByMapParams(Map params);
```

**xml**

可以看到使用map来传递多个参数，可以直接使用参数名称进行引用

```xml
<select id="selectByMapParams" resultMap="BaseResultMap" parameterType="map">
  select * from employee where gender = #{gender} and age = #{age}
</select>
```

### 4.用过java bean传递多个参数

也可以使用bean的方式来传递多个参数，使用时parameterType指定为对应的bean类型即可

> 这就传参方式的优点是比较方便，controller层使用@RequestBody接收到实体类参数后，直接传递给mapper层调用即可，不需要在进行参数的转换

**controller**

```java
@ApiOperation(value = "多个参数查询_通过Java Bean传递多个参数")
@PostMapping("findByBeans")
public ResultMsg findByBeans(@RequestBody Employee employee)
{
    List result= employeeMapper.selectByBeans(employee);
    return ResultMsg.getMsg(result);
}
```

**mapper**

```java
List <Employee> selectByBeans(Employee employee);
```

**xml**

参数的引用直接使用bean的字段

```xml
<select id="selectByBeans" resultMap="BaseResultMap" parameterType="com.wg.demo.po.Employee">
  select
  *
  from employee where gender = #{gender} and age = #{age}
</select>
```

### 5.直接使用JSON传递参数

这也是推荐的一种传参方式，controller层收到JSON型数据后，直接传递给mapper层进行查询操作，简单 方便

**controller**

```java
@ApiOperation(value = "多个参数查询_通过JSON传递多个参数")
@PostMapping("findByJSONObject")
public ResultMsg findByJSONObject(@RequestBody JSONObject params)
{
    List result= employeeMapper.findByJSONObject(params);
    return ResultMsg.getMsg(result);
} 
```

**mapper**

```java
List <Employee> findByJSONObject(JSONObject params);
```

 **xml**

```xml

<select id="findByJSONObject" resultMap="BaseResultMap" parameterType="com.alibaba.fastjson.JSONObject">
  select
  *
  from employee where gender = #{gender} and age = #{age}
</select>
```

### 6.传递集合类型参数List、Set、Array

在一些复杂的查询中（如 sql中的 in操作），传统的参数传递已无法满足需求，这时候就要用到List、Set、Array类型的参数传递，具体使用如下：

**controller**

```java
@ApiOperation(value = "多个参数查询_通过List、Set、Array传递多个参数")
@PostMapping("findByList")
public ResultMsg findByList(@RequestBody List<String> list)
{
    List result= employeeMapper.findByList (list);
    return ResultMsg.getMsg(result);
}
```

**mapper**

```java
List <Employee> findByList(List list);
```

**xml**

```xml
  <select id="findByList" resultMap="BaseResultMap" >
SELECT * from employee where age in
    <foreach collection="list" open="(" separator="," close=")" item="age">
      #{age}
    </foreach>
  </select>
```

这里foreach表示循环操作，具体的参数含义如下：

> foreach元素的属性主要有 item，index，collection，open，separator，close。
> item表示集合中每一个元素进行迭代时的别名，
> index指定一个名字，用于表示在迭代过程中，每次迭代到的位置，
> open表示该语句以什么开始，
> separator表示在每次进行迭代之间以什么符号作为分隔符，
>
> close表示以什么结束
>
> 在使用foreach的时候最关键的也是最容易出错的就是collection属性，该属性是必须指定的，但是在不同情况下，该属性的值是不一样的，主要有一下3种情况：
>
> - 1.如果传入的是单参数且参数类型是一个List的时候，collection属性值为list
> - 2.如果传入的是单参数且参数类型是一个array数组的时候，collection的属性值为array
> - 3.如果传入的参数是多个的时候，我们就需要把它们封装成一个Map或者Object

### 7.参数类型为对象+集合

该类参数与java Bean参数形式类似，只不过更复杂一些，如下面的Department类，除了基本字段还包括一个Employee的列表

**bean**

```java
@Data
public class Department {
    private Long id;

    private String deptName;

    private String descr;

    private Date createTime;

    List<Employee> employees;

}
```

**controller**

```java
@ApiOperation(value = "多个参数查询_对象+集合参数")
@PostMapping("findByDepartment")
public ResultMsg findByDepartment(@RequestBody Department department)
{
    List result= employeeMapper.findByDepartment(department);
    return ResultMsg.getMsg(result);
}
```

**mapper**

```java
List <Employee> findByDepartment(@Param("department")Department department);
```

**xml**

```xml
<select id="findByDepartment" resultMap="BaseResultMap" parameterType="com.wg.demo.po.Department">
    SELECT * from employee where dept_id =#{department.id} and age in
    <foreach collection="department.employees" open="(" separator="," close=")" item="employee">
        #{employee.age}
    </foreach>
</select>
```

> 这里foreach 对应Departmen部门中的List employees

请求参数： 查询部门Id=1，并且年龄 等于24和25的员工

```json
{
  "createTime": "2019-07-02T10:17:16.756Z",
  "deptName": "string",
  "descr": "string",
  "employees": [
    {
      "age": "24",
    },
    {
      "age": "25",
    }
  ],
  "id": 1
}
```

结果：

```json
{
  "data": [
    {
      "address": "北新街ndcpc",
      "age": "24",
      "createTime": 1562062434000,
      "deptId": "1",
      "gender": 1,
      "id": "318397755696631808",
      "name": "kls0bx19cy"
    },
    {
      "address": "北新街lavi0",
      "age": "25",
      "createTime": 1562062436000,
      "deptId": "1",
      "gender": 1,
      "id": "318397755801489408",
      "name": "gj9q3ygikh"
    }
  ],
  "result": "SUCCESS",
  "resultCode": 200,
  "resultMsg": ""
}
```
<script src="https://giscus.app/client.js"
    data-repo="byronlau/Knowledge-Garden"
    data-repo-id="R_kgDOKkfaDQ"
    data-mapping="number"
    data-term="21"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="zh-CN"
    crossorigin="anonymous"
    async>
</script>
        
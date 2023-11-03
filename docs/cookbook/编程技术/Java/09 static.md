---
title: static关键字是什么
---

static这个关键字是很多初学者在编写和阅读代码的时碰到的比较难以理解的关键字，也是很多面试官喜欢问到的问题之一。我们在使用的过程中会发现用它或不用它，对于代码来说有些时候似乎没有什么差异，但有些时候又的确有根本的不同。
那么接下来，我们就用这篇文章给大家梳理一下关于static的那些事儿。

## static到底是干什么的？

static这个关键字是每个Java程序员都一定会碰到的，就算你就只写过一个“Hello World”，你也遇到了它，因为它就在main方法的声明语法中🤷‍♂️。

```java
public static void main(String[] args){...}
```

只是在一开始学习的时候大家没有关注它的具体含义，仅仅只是把它当作了main方法固定语法的一部分，原封不动的照写照背了而已；
然后，我们就到了编程基础课程。在学习方法（函数）的时候，由于那个阶段我们还没有学习任何类和对象的概念，所以在Java这门面向对象的语言中我们只有通过给方法加上static修饰，才能让大家直接在main方法中调用到我们自己的自定义函数。

```java
public class Test{
    //自定义方法
    public static void func(int a){...}
    
    public static void main(String[] args){
        func(5);//main方法调用func方法
    }
}
```

在这期间，同学们的主要精力都在模块化过程、参数、返回等与方法更直接相关的知识点上，所以static就又不幸被忽略了🙅‍♂️，成了只要声明方法就“无脑”添加的一个关键字；
真正让我们同学感觉到static不但不是**“无脑”**😉反而还是**“烧脑”**🔥，是发生在我们开始学习面向对象的时候。这个时候我们发现：
1、方法的声明也可以不写static；
2、写和不写对于这个方法在外部的被调用是有不同的；
3、写和不写对于这个方法内部的实现也有区别；
4、再后面发现不仅方法可以选择是否使用static修饰，属性居然也可以选择，并且属性有没有static修饰也有很多现象上的差异。
[![img](http://img.mgd2008.com/whatHell.jpg)](https://hyktech.gitee.io/javatech/img/20170917/whatHell.jpg)

由于static的应用情况比较多，所以为了帮助大家能够更好的认知它，我们先奉上一个关于它的核心认识：

> 凡是用static修饰的类内容，都具有两个共性：
> 1、该内容与对象无关；
> 2、在加载期有特殊动作。

请大家在下面的学习中，带着这两点去进行理解、归纳和总结。

## static修饰属性

### 现象

```java
public class ClassA{
    public int fieldA;//普通属性     
    public static int fieldB;//静态属性
}
```

我们定义了一个叫做ClassA的类，包含两个属性fieldA和fieldB。其中fieldA是没有static修饰的，fieldB是用static修饰的。为了不带入其它知识点，我们把这两个属性设计为public的，能够让它们在类外部被直接访问到。接下来，我们看看使用它们的现象（有条件的同学可以边跟着写代码边学习，这样效果更好）。

```java
public class Test{
    public static void main(String[] args){
        ClassA ca = new ClassA();//产生一个ClassA对象
        
        System.out.println(ca.fieldA);//编译运行成功
        System.out.println(ca.fieldB);//编译运行成功
        System.out.println(ClasA.fieldA);//编译即失败
        System.out.println(ClassA.fieldB);//编译运行成功
    }
}
```

**这段测试代码说明：
1、普通属性（fieldA）只能通过对象进行访问，这说明普通属性是绑定在对象身上的（必须先产生对象，对象才有这个属性）；
2、静态属性（fieldB）既可以通过对象进行访问，也能通过类名直接访问（就算没有对象，这个属性也已经存在）。**

同样ClasA类不变，再来看一个测试：

```java
public class Test{
    public static void main(String[] args){
        //产生两个ClassA对象
        ClassA ca0 = new ClassA();
        ClassA ca1 = new ClassA();
        //测试普通属性
        ca0.fieldA = 100;
        ca1.fieldA = 200;
        System.out.println(ca0.fieldA);//控制台打印结果：100
        System.out.println(ca1.fieldA);//控制台打印结果：200
        //测试静态属性
        ca0.fieldB = 300；
        ca1.fieldB = 400;
        System.out.println(ca0.fieldB);//控制台打印结果：400
        System.out.println(ca1.fieldB);//控制台打印结果：400
           
    }
}
```

**这段测试代码说明：
1、普通属性是每个对象都拥有一个单独的存储，相互之间并不影响；
2、静态属性是所有对象共享了一个值，只要有一个对象改动了这个属性的值，该类型所有对象的这个值都被修改了。**
我们修改之前的代码：

```java
ca0.fieldB = 300；
ca1.fieldB = 400;
ClassA.fieldB = 500;//增加代码
System.out.println(ca0.fieldB);//控制台打印结果：500
System.out.println(ca1.fieldB);//控制台打印结果：500
ClassA ca2 = new ClassA();//产生一个新对象
System.out.println(ca2.fieldB);//控制台打印结果：500
```

我们还能够更清楚的发现，**静态属性真的是整个ClassA类（包括该类已经产生的对象，和以后产生的对象）只有一个fieldB变量！！！**

### 原理

去死记各种现象，不如学会原理，以后就可以通过原理来分析各种变化的现象了。这就是**“以不变应万变”😤**。
造成以上现象的根本原因是，JVM（Java虚拟机）针对静态属性和普通属性在产生的时机和存放的方式上是完全不同的。
**静态属性：**在程序运行运行之前，JVM加载该类时就会在内存中产生它。为该属性分配空间进行初始化，并且只会产生一个；在后续运行过程中，无论是用该类直接访问该属性，还是用这个类的某个对象访问该属性，那么都是操作的同一个。
**普通属性：**在程序运行起来以后，每当执行到产生一个对象的时候，才会为该对象在内存中分配空间；而普通属性也就是在这个时候才会被划分到该对象自己的空间当中。因此，该类的每一个对象都有一个该属性，各自独立，各有各的值！

回头对应一下，我们一开始给的所有static修饰都会有的两点共性（与对象无关 和 加载期搞事情），看是不是这样？✌️

### 根据场景使用

了解了现象，知道了原理，我们就别再“无脑”使用static了。我们要掌握使用的原则：


**1、常量属性可以统统设计为static的；
2、变量属性，绝大部分都是非static的，除非真的分析出全类共享一个值，才能设计为static。**

说明：
常量属性:
这种属性的值是在声明的时候就确定了，不可更改！所以每个对象该属性的值都一摸一样，因此没有必要在每个对象身上存放一份，设计为static全类共享一个值即可。
变量属性:
如果该类任意一个对象的该属性值可以与别的对象不同，那么这个属性就不能定义为static，必须保证每个对象各自拥有独立的该属性。比如：学生类的姓名、年龄、性别、身高等等；
除非确定这个属性的值是所有对象都一模一样，谁改了大家都得改动。这个就要看具体的问题域分析了，比如：学生类有一个属性是所属班级。如果问题域就是一个班级，所有学生对象只有可能是这一个班级的，这个属性才能设计为static（遇到需要修改班级名称的业务也没有必要一个对象一个对象的去改动了）；如果问题域本身就涉及到多个班级，学生对象有可能是不同班级的，那么就绝不能把这个班级属性设计为static的了，否则就会出大问题（只会保留最后一个赋值的班级名称）。很明显，一个类中能满足这种要求的变量属性是很少的。

## static修饰方法

### 现象

```java
public class ClassA{
    public int fieldA;//普通属性     
    public static int fieldB;//静态属性
    
    public void methodA(){...} //普通方法
    public static void methodB(){...} //静态方法
}
```

我们在上例的ClassA类中增加两个方法methodA和methodB。其中methodA是没有static修饰的普通方法，methodB是用static修饰的静态方法。接下来，我们看看使用它们的现象。

```java
public class Test{
    public static void main(String[] args){
        ClassA ca = new ClassA();//产生一个ClassA对象
        
        ca.methodA();//编译运行成功
        ca.methodB();//编译运行成功
        ClassA.methodA();//编译即失败
        ClassA.methodB();//编译运行成功
    }
}
```



**这段测试代码说明：
1、普通方法（methodA）只能通过对象进行访问，这说明普通方法是绑定在对象身上的，即与对象相关；
2、静态方法（methodB）既可以通过对象进行访问，也能通过类名直接访问，也就是说有没有执行对象无所谓，即与对象无关。**
这个测试体现了普通方法和静态方法在调用时候的差异性，两种方法在实现的时候也有差异性。我们接下来看下面的代码：

```java
public class ClassA{
    public int fieldA;//普通属性     
    public static int fieldB;//静态属性
    
    public void methodA(){...}//普通方法 
    
    public static void methodB(){...}//静态方法
    //普通方法
    public void methodAA(){
        System.out.println(fieldA);//编译运行成功
        System.out.println(fieldB);//编译运行成功
        methodA();//编译运行成功
        methodB();//编译运行成功
    }
    //静态方法
    public static void methodBB(){
        System.out.println(fieldA);//编译报错
        System.out.println(fieldB);//编译运行成功
        methodA();//编译报错
        methodB();//编译运行成功
    } 
}
```

**这段测试代码说明：
普通方法和静态方法的区别不仅仅是在外部调用的地方，更多体现在方法内部的实现当中。
1、普通方法能够访问本类的所有属性和调用本类自身的所有方法；
2、静态方法只能够访问本类的静态属性和调用本类的静态方法。**
我们再把methodBB方法改动一下：

```java
public static void methodBB(){
    System.out.println(this);//编译报错
}
```

**这说明：
在静态方法中，连this对象都不能访问。这点到好理解，因为静态方法完全可以用类名直接访问，这个时候根本没有当前对象嘛。**

### 原理

为什么静态方法不能操作到本类的非静态属性或非静态方法呢？我们可以从两个角度去分析这个问题。
1、从JVM的加载机制上看，静态方法是随着所属类被加载的时候就首先被加载了的；而普通方法是产生对象的时候才被加载的。所以先加载的静态方法根本不知道后加载的普通方法，如何调用呢？🤔️
2、从设计意图上，静态方法是可以在没有对象的时候被调用的。那么这个时候它去调用一个跟当前对象相关的普通方法是没有道理的（此时压根儿根本没有当前对象嘛）。其实，最后一个例子就是表明了这个情况，没有this，当然更没有super❗️❗️❗️

再回头对应一下我们给出的static修饰都会有的两点共性：与对象无关和加载期搞事情。👍

### 根据场景使用

那么什么时候我们把方法设计为普通方法，什么时候设计为静态方法呢？


**1、当方法的调用是绑定到本类的某个对象身上的。也就是说描述的对应场景一定是调用该类不同的对象去执行这个行为，在执行的效果上会产生差异，或是执行效果对执行对象本身的相关状态会产生影响。那么这个方法就只能是普通方法！
2、当方法的调用与由本类的任何一个对象来执行都无关。也就是说描述的场景一定是无论用该类的任何一个对象去执行这个行为都无任何差异，也不会对执行对象的相关状态产生任何影响。那么这个方法就应该设计为静态方法。这样的方法也被称之为：“工具方法”。**

如果觉得上述说明太过于枯燥了，我们再来举个例子。比如：有一个类叫做Friend（朋友），该类中有一个方法是帮忙买烟。如果这个买烟方法在场景中，需要操作到谁（对象）去买（哪个朋友对象执行了这个方法，要增加该对象的友好度属性）。那么这个方法就是一个跟Friend类对象相关的方法，不能设计为static。如果场景中，这个买烟方法只是完成买烟功能，不在乎谁买的，执行的对象也不会被操作到。那么这个方法就是个完成功能的工具而已，就应该设计为static的。
大家可以模仿这个例子再举一些类似的场景，并完成实现。😊

## static修饰初始化块

### 现象

static还常常用来修饰类当中的代码块，也叫“初始化块”。

```java
public class ClassA{
    {
        System.out.println("实例初始化块");
    }
    
    static{
        System.out.println("静态初始化块");
    }
}
```

“初始化块”就像是一个没有方法声明的方法块一样，它就是一段代码集合，可以书写各种需要执行的语句和逻辑。由于没有方法声明，所以它不能像方法一样，想在什么时候执行就在什么时候调用；而是在某个特殊时间点被自动执行。

```java
public class Test{
    public static void main(String[] args){
        ClassA ca0 = new ClassA();
        ClassA ca1 = new ClassA();
    }
}
```

这段代码执行的效果如下：
[![img](http://img.mgd2008.com/Console.png)](https://hyktech.gitee.io/javatech/img/20170917/Console.png)
**这段代码说明：
1、实例初始化块在每次产生对象的时候就被执行了一次；
2、静态初始化块只被执行一次，而且是在产生对象之前。**

### 原理

静态初始化块是在JVM在加载ClassA类的时候被自动执行，一个类只被加载一次就可以在运行期被反复使用了。所以它只执行一次，且是先执行。
实例初始化块是在每次产生对象的时候，在给对象分配空间、初始化属性之后，执行构造方法内部代码之前，被自动调用。所以每产生一个对象就会被执行一次。
😊，还是那句话：static修饰的，与对象无关且加载期搞事情。

### 根据场景使用

在实际使用中，静态初始化块在项目中常常出现。我们可以把一些项目中需要做的预准备动作放到当中，让它在加载期就完成准备工作，运行期就只管直接操作即可；而实例初始化块使用的并不多，因为它的效果和执行的时机其实是与构造方法有重复的，完全可以就直接写在类的构造方法当中。

## static修饰构造

```java
public class ClassA{
    public ClassA(){...}//正确的构造方法
    public static ClassA(){...}//编译马上报错
}
```

static不能修饰构造方法！！！这是为什么呢？
构造方法是干嘛的？产生对象！
static代表什么？与对象无关！
这就不需要多说了吧……😓

## static修饰成员内部类

类的内容当中除了初始化块、属性、构造、方法这4种以外，还有一种更复杂的情况。这就是类当中还包含一个类（内部类）。而内部类也是有静态和非静态之分的：

```java
public class ClassA{
    public class InnerClassA{
        //内部类的属性、构造、方法
    }
    
    public static class InnerClassB{
        //内部类的属性、构造、方法
    }
}
```

其实static修饰内部类之后，其效果还是之前我们总结的那几点，只是在表现形式上要结合内部类的语法和使用场景来认知。比如：静态内部类与外部类对象无关，所以它完全可以看成是一个隐藏在外部类当中的独立类，这样就可以给我们带来更多的惊喜。😺

### 实现更好的封装性

```java
public class Person{   
    private String name;//姓名   
    
    private Home home; //家庭  

    public Person(String _name){  
         name = _name;  
    }  
    
    public String getName() {
        return name;
    }
    
    public void setName(String name) {
        this.name = name;
    }
    
    public String getHome() {
        return home.toString();
    }
    
    public void setHome(String address,String tel) {
        this.home = new Home(address,tel);
    }
    //静态内部类Home
    private static class Home{  
         private String address; //家庭地址  
           
         private String tel; //家庭电话 

         public Home(String address,String tel){  
           this.address = address;  
           this.tel = tel;  
         }  
         
         public String toString(){
            return "住址：" + this.address + "，电话：" + this.tel;
        }
    }  
}
```

当我们这样设计Person和Home的时候，我们会发现Home被封装在Person类中，仅仅被Person使用，外部甚至不知到它的存在。

```java
public class TestMain {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Person p = new Person("张三");
		p.setHome("人民南路110号", "13312345678");
		System.out.println(p.getHome());
	}
}
```

### 实现单列模式

```java
public class Singleton {  
    private static class SingletonHolder {  
        private static final Singleton INSTANCE = new Singleton();  
    }  
    private Singleton (){}  
    public static final Singleton getInstance() {  
        return SingletonHolder.INSTANCE; 
    }  
}
```

相对于我们常见的三种单列模式的写法，这种第四种写法其实是我个人最为推荐的。
首先，由于SingletonHolder是私有的，除了Singleton的getInstance()之外没有办法访问它。因此只有在调用这个方法的时候才会加载SingletonHolder类，也才会产生单列对象，所以它是懒汉式的；
其次，它的对象是在加载期间就被产生了，所以无论多少个线程调用getInstatnce()，都是返回的同一对象，所以没有线程不安全性；
再其次，同时读取实例的多个线程不会进行同步（没有使用synchronized加锁），所以没有损失性能，支持高并发；
最后，与双锁机制不同，这段代码实现不依赖JDK版本。

## 静态导包

这估计就是一个比较生冷的知识点了😏。我们见惯了**“import”**语句，但是你见过**“import static”**吗？😤要知道它可是在JDK1.5当中就已经被加入的特性。
一般我们导入一个类都用 import 包名.类名的方式;而静态导入是这样的：import static 包名.类名.*;这里的多了个static，还有就是类名后面多了个.* ，意思是导入这个类里的静态成员。当然，也可以只导入某个静态方法，只要把 .* 换成静态方法名就行了。然后在这个类中，就可以直接用方法名调用静态方法，而不必用类名.方法名的方式来调用。
比如:
在静态导入之前：

```java
public class TestStatic {
    public static void main(String[] args) {
        int maxVal = Integer.MAX_VALUE;
        String hexStr = Integer.toHexString(38));
    }
}
```

在静态导入之后：

```java
import static java.lang.Integer.*;

public class TestStaticImport {
    public static void main(String[] args) {
        int maxVal = MAX_VALUE;//直接访问Integer的静态属性
        String hexStr = toHexString(38));//直接调用Integer的静态方法
    }
}
```

关于静态导包，我们要多说几句话：

1. 必须使用import static， 不能写成static import；
2. 由于缺少前缀，所以遇到同名方法要小心；
3. 虽然少敲了几下键盘，可能损失的是代码的可读性。

⚠️把它作为一个知识点知道就可以了，至于你用不用这种语法，还是…..谨慎吧……😊

## 最后的话

static的认知,是面向对象中“类”和“对象”概念的进一步深化。绝不能简单的去背各种语法特性和各种情况的执行效果。这是“一叶障目，不见泰山”的方法。要想正确无误、灵活自如的使用它，请一定要建立它在面向对象中的意义。请反复咀嚼、体会别人的设计和自己要操作的场景，这才是“事倍功半”的方式。
㊗️大家成功！🏁
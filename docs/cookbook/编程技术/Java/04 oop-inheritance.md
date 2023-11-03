---
title: 面向对象 - 继承
---

在上一篇系列文章中，我们聊过了面向对象的“封装”特征。在有了封装的基础上，今天我们在来谈谈面向对象第二个特征—-“继承”。
👨‍🏫**“继承”**这个知识点在同学们学习的过程中，其实并不算是一个难点。在语法上，Java也把它设计得非常简单，一个**extends**关键字就可以搞定；在理解上，“继承”这个词在生活中也很常见，不存在什么晦涩难懂的地方。但一旦涉及到具体使用的时候，就会发现很多同学其实对它的认知度还是不高的。不然在面试中也就不会有这么多的关于“继承”的面试题目了。诸如🤷‍♀️：“Java单继承的优缺点是什么？”、“抽象类与接口到底有区别？”、“什么时候用继承？什么时候用组合？”……等等。所以，这次我们借用这篇文章把“继承”这个概念再梳理一下。💪

## 继承的由来

听过我课的同学应该知道，我时常在课堂上强调一个观点：**“复用与分离”**。我认为在软件开发中很多新设计理念、新的语法、新的框架都是基于这个观点被推广、设计、应用的。“继承”同样也是如此。比如在一个宠物医院的管理系统中，会有很多不同类型的宠物（🐱、🐶、🐢、🐦）。它们都有各自的属性和行为，所以我们需要定义不同的类来表示它们。比如：

```java 
public class DogBean{
    private String name;
    private int age;
    private int boneNum;        //每天吃的骨头数目
    private ArrayList<DogBean> children; //所生小狗的集合
    
    public void play(){
        //玩耍
    }
    
    public void swim(){
        //游泳
    }
}

public class CatBean{
    private String name;
    private int age;
    private int fishNum;        //每天吃的鱼数目
    private ArrayList<CatBean> children; //所生小猫的集合
    
    public void play(){
        //玩耍
    }
    
    public void climbTree(){
        //爬树
    }
}

public class TortoiseBean{
    private String name;
    private int age;
    
    public void play(){
        //玩耍
    }
    
    public void sleep(){
        //冬眠
    }
} 

public class BirdBean{
    private String name;
    private int age;
    private int wormNum；     //每天吃的虫数量
    
    public void play(){
        //玩耍
    }
    
    public void sing(){
        //鸣叫
    }
}
```

写完以后，我们会觉得亏得慌。因为，在这些不同的类身上有些属性/行为是相同的，而我们却不得不在每个类里面都把这些相同的属性/行为重复书写一次。这时候咋办？当然就想到“继承”啦，就是这么自然！😊
提出父类—宠物类，把共有的属性/行为写在它身上，各个子类通过“继承”机制，自动获得该父类的属性/行为，这不是“复用”是什么？面向对象的设计者也是这么想的😎，所以他们在面向对象语言中设计了继承的语法。
光因为**复用**吗？其实“继承”也带来了**分离**的效果！在有了继承的情况下，在设计父类时我们只需要考虑共有的信息，设计子类时我们也只需要把精力放在该子类特有的信息上。这相当于把问题分解成了两个层面—共有和特有，各有所属分别设计和实现，不会出现混为一谈的情况。

```java 
public class PetBean{
   private String name;
    private int age;
    
    public void play(){
        //玩耍
    } 
}

public class DogBean extends PetBean{
    private int boneNum;        //每天吃的骨头数目
    private DogBean[] children; //所生小狗的集合
    
    public void swim(){
        //游泳
    }
}

public class CatBean extends PetBean{
    private int fishNum;        //每天吃的鱼数目
    private CatBean[] children; //所生小猫的集合
    
    public void climbTree(){
        //爬树
    }
}

public class TortoiseBean extends PetBean{
    public void sleep(){
        //冬眠
    }
} 

public class BirdBean extends PetBean{
    private int wormNum；     //每天吃的虫数量
    
    public void sing(){
        //鸣叫
    }
}
```

简单的看看上下两段代码的行数，你也能知道“继承”好不好了。

## 继承使用的原则

从上面的示例，我们看到**“继承”**简直就是又简单又好用👍。由此也就造成了很多初学者的一个问题，那就是**滥用**继承。比如：A类里面有一个方法methodA()，B类想在自己的methodB()方法中调用这个来自于A类的方法，咋办呢？很多人下意识的就说让B继承A就可以了。

```java 
public class A{
    public void methodA(){
        //methodA的实现
    }
}

/*
 *  由于B类继承了A类，所以B类也就自动继承了methodA()。
 *  所以可以直接在B类里面调用到该方法了。
 */
public class B extends A{
    public void methodB(){
        this.methodA();
    }
}
```

如果你这么用继承，那就大错特错了！因为你只站在了代码实现的级别，而没有考虑场景！
如果要说实现这个功能，那么我们其实除了上面这个语法还有其他两种方式呢。

方式一：

```java 
public class A{
    public void methodA(){
        //methodA的实现
    }
}

/*
 *   B类包含一个A类的对象，作为B类的属性，
 *   然后调用该属性的methodA()方法。
 */
public class B{
    private A myA = new A();
    public void methodB(){
        myA.methodA();
    }
}
```

方式二：

```java 
public class A{
    public void methodA(){
        //methodA的实现
    }
}

/*
 *  B类的methodB()方法接收外部传入的A类对象参数，
 *  然后进行调用该参数的methodA()方法。
 */
public class B{
    public void methodB(A myA){
        myA.methodA();
    }
}
```

可以看到，以上三种设计都可以让B类的methodB()方法操作到A类的methodA()方法。那么到底哪一种好呢？这其实就是我们在授课过程中常常跟同学们强调的一个东西了：**场景**。

> **场景的重要性：** *写代码，绝对不是仅仅只为了实现某个功能。功能的实现只是最基本的目标，而在程序中正确的模拟现实问题域也是绝对不能忽视的问题。模拟的好与差决定了这个程序的生命力，决定了这个程序能否随着实际问题域的发展而发展。好的设计，能够在问题域自然变化的情况下，只经过简单改变就能继续使用；而差的设计很有可能就要面临大量的修改，甚至是推翻重来。*

上面三种方式都能让B类与A类发生绑定关系，但其实它们代表的是面向对象中类与类之间的三种关系：**继承、组合、使用**，也就是我们常常说的**”is-a“、”has-a“、”use-a“**关系。在场景中，正确的判断两个类到底是什么关系，从而采用正确的设计（选择对应的语法），这才是王道，否则很有可能被现实打个响亮的耳光！

举个例子：有两个类，一个Boy（男孩），一个Girl（女孩）。Boy类有一个kiss方法😚，Girl类有一个叫response（回应）的方法。当Boy的kiss方法在执行的最后，要调用Girl的response方法。我们用三种方式都能实现这个效果，但是他们描述的场景却截然不同。
**第一种：继承---“is-a”---是一个**

```java 
public class Girl{
    public void response(){
        System.out.println("讨厌，你好坏......");
    }
}

public class Boy extends Girl{
    public void kiss(){
        System.out.println("让我亲一个嘛～～～");
        this.response();
    }
}
```



Boy类继承了Girl类，这本身就说不通了吧……😓 又不是儿子和母亲的关系……还要接吻……🤢。算了，不说了🤐️。所以，这个场景千万不能设计成这种继承，否则你就是个BT！！！

**第二种：组合---“has-a”---有一个**

```java 
public class Girl{
    public void response(){
        System.out.println("讨厌，你好坏......");
    }
}

public class Boy extends Girl{
    private Girl myGirl；
    
    public void kiss(){
        System.out.println("让我亲一个嘛～～～");
        myGirl.response();
    }
}
```



Boy类拥有一个Girl类对象作为自己的属性。这就非常合情合理了，难道你的女朋友不是你生命中的一部分吗❤️？而且，由于Boy对象拥有了Girl对象，所以在Boy对象的任何行为中都可以操作到这个女友对象，让她参与到你生活的方方面面。**这个场景就应该使用这样的设计。**

**第三种：使用---“use-a”---用一个**

```java 
public class Girl{
    public void response(){
        System.out.println("讨厌，你好坏......");
    }
}

public class Boy extends Girl{
    public void kiss(Girl myGirl){
        System.out.println("让我亲一个嘛～～～");
        myGirl.response();
    }
}
```



Boy类的kiss方法接收了一个外部参数是Girl的对象，由于参数只是一个局部变量，所以kiss方法结束后，这个Girl对象也就和Boy没有关系了。这个场景嘛……我觉得应该是描述了一种违反道德观的现象。两个对象只在亲吻的时候才有关联，亲吻结束后就互不相识了。还好是亲吻，如果是其它行为我觉得有必要打举报电话了。警察👮叔叔，有人卖哔～～～。

通过以上分析，要向大家传递的一个内容就是：继承不是你想用就用的，请一定要在场景中分析出这些类真正的具备“is-a”关系。

## Java的继承机制

上面👆，我们描述的是面向对象编程思想中“继承”的概念。但是具体到面向对象的编程语言，不同的语言为了实现这个“继承”的效果，都提供的有自己的机制。作为Java语言的学习者，我们当然要掌握Java语言的继承机制啰。这里面包括了：单继承、内存叠加、接口和抽象类等等内容。由于这些东西内容比较多，又自成体系，所以我决定以后单开博客来讲述，然后再把链接放到这里来。

## 总结

最后，当你以后被问到“你如何理解面向对象的继承”时，请做如下回答：

> 继承：是面向对象中的一种类与类之间的关系。当多个类具备一脉相承的“is-a”关系的时候，使用继承。这就能够让这些类进行正确的关联绑定，子类自动具备来自于的父类的属性和行为，做到代码的复用和设计的分离。
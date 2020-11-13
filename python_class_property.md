
本篇文章是关于对Python中面向对象中类的三大特性：继承、多态、封装（私有化）的讲述，希望对你理解和使用类的特性有所帮助。

Python中，类表示具有相同属性和方法的对象的集合。在使用类时，需要先定义类，然后再创建类的实例，通过类的实例就可以访问类中的属性的方法。面向对象程序设计中类的三大基本特征：继承、多态、封装（私有化），下面分别描述。

#  类的三大基本特征：继承、多态、封装（私有化）
## 1.继承
在编写类时，并不是每次都要从空白开始。当要编写的类和另一个已经存在的类之间存在一定的继承关系时，就可以通过继承来达到代码重用的目的，提高开发效率。下面将介绍如何在Python中实现继承。
### 1）继承的基本语法
在面向对象编程中，被继承的类称为父类或基类，新的类称为子类或派生类。

语法格式如下：

class ClassName(baseclasslist)

    '''类的帮助信息'''    #类文档字符串
    Statement    #类体
参数说明：

ClassName：用于指定类名。

baseclasslist：用于指定要继承的基类，可以有多个，类名之间用逗号分隔。如果不指定，将使用所有python对象的根类object。

'''类的帮助信息'''：用于指定类的文档字符串，定义该字符串后，在创建类的对象时输入类名和左侧的括号“(”后，将显示该信息。

Statement：类体，主要由类变量、方法和属性等定义语句组成。如果在定义类时，没想好类的具体功能，也可以在类体中直接使用pass语句代替。

例1：创建水果基类及其派生类。

创建一个名为fruit.py的文件，然后在该文件中定义一个水果类Fruit(作为基类)，并在该类中定义一个类属性(用于保存水果默认的颜色)和一个harvest()方法，然后创建Apple类和Orange类，都继承自Fruit类，最后创建Apple类和Orange类的实例，并调用harvest()方法(在基类中编写)，代码如下：

```
class Fruit:    #定义水果类(基类)
    color = "绿色"    #定义类属性
    def harvest(self,color):
        print("水果是：" + color + "的！")    #输出的是形式参数color
        print("水果已经收获....")
        print("水果原来是：" + Fruit.color + "的！")    #输出的是类属性color
class Apple(Fruit):    #定义苹果类(派生类)
    color = "红色"
    def __init__(self):
        print("我是苹果")
class Orange(Fruit):    #定义橘子类(派生类)
    color = "橙色"
    def __init__(self):
        print("\n我是橘子")
        
apple = Apple()    #创建类的实例(苹果)
apple.harvest(apple.color)    #调用基类的harvest()方法
orange = Orange()    ##创建类的实例(橘子)
orange.harvest(orange.color)    #调用基类的harvest()方法
输出结果：
我是苹果
水果是：红色的！
水果已经收获....
水果原来是：绿色的！

我是橘子
水果是：橙色的！
水果已经收获....
水果原来是：绿色的！
>>> 
```
### 2）方法重写
基类的成员都会被派生类继承，当基类中的某个方法不完全适用于派生类时，就需要在派生类中重写父类的这个方法。

在例1中，基类中定义的harvest()方法，无论派生类是什么水果都会显示“水果是....”，如果想要针对不同水果给不同提示，可以在派生类中重写harvest()方法。

例如：在创建派生类Orange时，重写harvest()方法的代码如下：
```
class Orange(Fruit):    #定义橘子类(派生类)
    color = "橙色"
    def __init__(self):
        print("\n我是橘子")
    def harvest(self,color):
        print("橘子是：" + color + "的！")    #输出的是形式参数color
        print("橘子已经收获....")
        print("橘子原来是：" + Fruit.color + "的！")    #输出的是类属性color 
输出结果：
我是苹果
水果是：红色的！
水果已经收获....
水果原来是：绿色的！

我是橘子
橘子是：橙色的！
橘子已经收获....
橘子原来是：绿色的！
```
### 3）派生类调用基类的__init__()方法
在派生类中定义__init__()方法时，不会自动调用基类的__init__()方法。因此要让派生类调用基类的__init__()方法进行必要的初始化，需要在派生类使用super()函数调用基类的__init__()方法。

super()用法：

super(子类名, self).方法名()    #强制调用父类的成员

例2，定义一个水果类为父类，子类Apple调用父类的方法：
```
class Fruit:    #定义水果类(基类)
    def __init__(self,color = "绿色"):
        Fruit.color = color    #定义类属性
    def harvest(self):
        print("水果原来是：" + Fruit.color + "的！")    #输出的是类属性color
class Apple(Fruit):    #定义苹果类(派生类)
    def __init__(self):
        print("我是苹果")
        super().__init__()
apple = Apple()    #创建类的实例(苹果)
apple.harvest()    #调用基类的harvest()方法
输出结果：
我是苹果
水果原来是：绿色的！
```
### 4）多继承
多继承是指一个类继承两个或两个以上的父类，例如有类A、B、C，类C同时继承类A和类B，就说类C多继承了类A和类B，类C可以使用类A和类B中的属性和方法。

Python中支持多继承的形式，括号中填入要继承的父类，父类之间用逗号隔开。Python中多继承的基本写法如下。

class 子类(父类1, 父类2, ... , 父类n): pass

现在我们定义三个类A、B和C，并让类C同时继承类A和类B。
```
class A():
    def __init__(self,color,size):
        self.color = color    #定义类属性
        self.size = size

    def harvest_A(self):
        print("水果原来是%s,形状比较%s." %( self.color , self.size))    #输出的是类属性color和size

class B():
    def __init__(self,taste,city):
        self.taste = taste    #定义类属性
        self.city = city
    def harvest_B(self):
        print("水果口味比较%s,产地是%s." %( self.taste , self.city))    #输出的是类属性color和size

class C(A,B):
    def __init__(self,color,size,taste,city):
        A.__init__(self,color,size)
        B.__init__(self,taste,city)

c = C('黄色','很大','有点甜','海南')
c.harvest_A()
c.harvest_B()
输出结果：
水果原来是黄色,形状比较很大.
水果口味比较有点甜,产地是海南.
```
可以看到，类C既可以使用类A中的成员方法harvest_A( )，也能够使用类B中的成员方法harvest_B( )。这里需要注意的是，使用多继承时，调用父类的初始化方法__init__( )时，需要指明调用的是哪一个具体父类，而不能像单继承那样直接使用super关键字调用。

多继承可以让子类同时继承每个父类的属性和方法，那么，当父类之间具有相同名字的方法时，子类会怎么调用呢？我们修改一下上述代码，将类A中的成员方法harvest_A( )和类B中的成员方法harvest_B( )的方法名都修改为harvest。
```
class A():
    def __init__(self,color,size):
        self.color = color    #定义类属性
        self.size = size

    def harvest(self):
        print("水果原来是%s,形状比较%s." %( self.color , self.size))    #输出的是类属性color和size

class B():
    def __init__(self,taste,city):
        self.taste = taste    #定义类属性
        self.city = city
    def harvest(self):
        print("水果口味比较%s,产地是%s." %( self.taste , self.city))    #输出的是类属性color和size

class C(A,B):
    def __init__(self,color,size,taste,city):
        A.__init__(self,color,size)    #调用父类A的初始化方法__init__( )
        B.__init__(self,taste,city)    #调用父类B的初始化方法__init__( )

class D(B,A):
    def __init__(self,color,size,taste,city):
        A.__init__(self,color,size)
        B.__init__(self,taste,city)

c = C('黄色','很大','有点甜','海南')
print("c调用结果")
c.harvest()
d = D('黄色','很大','有点甜','海南')
print("d调用结果")
d.harvest()
输出结果：
c调用结果
水果原来是黄色,形状比较很大.
d调用结果
水果口味比较有点甜,产地是海南.
```
可以看到，类C和类D都继承了类A、B，但当调用成员方法harvest( )时，类C调用的是类A中的harvest( )，而类D调用的是类B中的harvest( )。

事实上，若父类中有相同的方法名，而在子类使用时未指定，Python会在继承的父类中从左至右搜索，即方法在子类中未找到时，从左到右查找父类中是否包含方法，因此会优先调用在括号中排在前面的父类的方法。

若我们在不想改变继承顺序的同时，想优先调用类B中harvest( )，只需在子类中显式指定即可。
```
class A():
    def __init__(self,color,size):
        self.color = color    #定义类属性
        self.size = size

    def harvest(self):
        print("水果原来是%s,形状比较%s." %( self.color , self.size))    #输出的是类属性color和size

class B():
    def __init__(self,taste,city):
        self.taste = taste    #定义类属性
        self.city = city
    def harvest(self):
        print("水果口味比较%s,产地是%s." %( self.taste , self.city))    #输出的是类属性color和size

class C(A,B):
    def __init__(self,color,size,taste,city):
        A.__init__(self,color,size)
        B.__init__(self,taste,city)
    def harvest(self):
        B.harvest(self)    #指定调用父类B成员方法

c = C('黄色','很大','有点甜','海南')    
c.harvest()
输出结果：
水果口味比较有点甜,产地是海南.
```
显式指定调用父类成员方法，多继承是有继承顺序的，即优先继承哪个类。
## 2.多态
多态是指同一种事物的多种形态。其实我们在之前内容中已经接触到了多态，方法的重写就是一种多态。

实现多态的步骤就是：1、定义子类。2、重写父类中的成员方法。3、子类调用自己的成员方法而不使用父类中的成员方法。

例3，定义一个水果类作为父类，Apple类作为子类，重写水果类中的成员方法，再进行调用。
```
class Fruit:    #定义水果类(父类)
    def __init__(self,color,size):
        Fruit.color = color    #定义类属性
        Fruit.size = size
        
    def harvest(self):
        print("水果原来是：" + Fruit.color)    #输出的是类属性color
        
class Apple(Fruit):    #定义苹果类(子类)
    def __init__(self,color,size,taste):
        super(Apple,self).__init__(color,size)
        self.taste = taste

    def harvest(seif):
        print("苹果原来是：" + Fruit.color)
        
apple = Apple("苹果","红色","大")    #创建类的实例(苹果)
apple.harvest()    #调用父类的harvest()方法
输出结果：
苹果原来是：苹果
```
那么多态有什么用呢？我们在上述代码的基础上再增加一个子类Orange，同样继承自Fruit，然后定义一个who_great( )函数，该函数接受一个对象变量，功能是调用对象的成员方法harvest( )。
```
class Fruit:    #定义水果类(基类)
    def __init__(self,color,size):
        Fruit.color = color    #定义类属性
        Fruit.size = size
        
    def harvest(self):
        print("水果原来是：" + Fruit.color)    #输出的是类属性color
        
class Apple(Fruit):    #定义苹果类(派生类)
    def __init__(self,color,size,taste):
        super(Apple,self).__init__(color,size)
        self.taste = taste

    def harvest(seif):
        print("苹果原来是：" + Fruit.color)

class Orange(Fruit):    #定义橘子类(派生类)
    def __init__(self,color,size):
        super(Orange,self).__init__(color,size)

    def harvest(seif):
        print("橘子原来是：" + Fruit.color)

def who_great(Fruit):
    Fruit.harvest()
        
apple = Apple("红色","大","甜")    #创建类的实例(苹果)
who_great(apple)
orange = Orange("橙色","小")    #创建类的实例(橘子)
who_great(orange)
输出结果：
苹果原来是：红色
橘子原来是：橙色
```
多态的作用

可以看到，当我们给who_great( )函数传入子类Apple的对象时，调用的就是Apple中的harvest( )方法；传入子类Apple的对象时，调用的就是Apple中的harvest( )方法。

这就是多态的好处。当多个继承自同一个类的子类中有相同名字的成员方法时，那么子类产生的对象就可以不必考虑具体的类型而直接调用方法。以上述代码为例，对于一个变量，我们只需要知道它是Fruit类型，而无需确切知道它的子类型，就可以放心地调用harvest( )方法，而具体调用的harvest( )方法是作用在Fruit、Apple还是Orange的对象上，由运行时该对象的确切类型决定，这就是多态真正的威力。
## 3.封装
封装的本质是将事物相关的属性和方法封装在一个类里面，我们调用类创建实例的时候，不用关心类内部的代码细节，相当于一个黑箱子，我们只需要该实例(黑箱)能给出我们想要的结果就好了。

例4，定义一个学生类，封装学生的班级和地址信息。
```
class Student:
    classroom = '26'
    address = 'suzhou'

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def message(self):
        print('名字是%s，年纪是: %s' % (self.name, self.age))

s = Student('wl',22)
s.message()#名字是gos，年纪是: 89
# 以下是错误的用法
# 类将它内部的变量和方法封装起来，阻止外部的直接访问
# print(classroom)#NameError: name 'classroom' is not defined
# print(adress)
# print_age()
输出结果：
名字是wl，年纪是: 22
```
方法和变量都是被封装好的不可以直接访问的，需要对象的实例化，然后调用方法才可访问对应的方法。

封装的作用

将数据与具体操作的实现代码放在某个对象内部，使这些代码的实现细节不被外界发现，外界只能通过接口使用该对象，而不能通过任何形式修改对象内部实现，正是由于封装机制，程序在使用某一对象时不需要关心该对象的数据结构细节及实现操作的方法。使用封装能隐藏对象实现细节，使代码更易维护，同时因为不能直接调用、修改对象内部的私有信息，在一定程度上保证了系统安全性。类通过将函数和变量封装在内部，实现了比函数更高一级的封装。

----
-----
以上内容介绍了Python面向对象中继承、多态和封装的相关知识点，需要重点掌握继承的基本用法，注意多继承的继承顺序，理解多态和封装的概念和意义。面向对象是一种编程思想，我们要理解它的精髓，才能更好地使用面向对象编程。感谢阅读~

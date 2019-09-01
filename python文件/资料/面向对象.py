#!/sur/bin/python
# -*-coding:utf-8-*-
#              python——面向对象

# 类的书写格式
"""
1，class   关键字    定义一个类
2，类名：  每个单词的首字母大写，
3、object  代表python所有类的基类
4、面向过程，函数式代码的语句块
例如：
class 类名（object）:
    语句块     包含面向过程，函数式
"""

# class Stydent(object):                      #定义一个类     object   所有类的基类
#     #类的属性
#     height = 170
#     weight = 180
#     def name(self,x):
#         k = "sdfag"     #局部变量    =    实例属性
#         print(f"有个人叫{x},他的身高是{self.height}cm,体重{self.weight}")
#         print(f"面向对象的方法")
#         print(k)
# #类的使用
# s1 = Stydent()     #被称为对象/类的实例
# #类的实例使用类的方法
# s1.name("哈哈哈")


# class Nihao(object):
#     a = "python很强大"
#     b = "面向对象是编程思想"
#     def ziji(self,c,d):
#         print(f"python是{c},面向对象{d},我觉得{self.a},python{self.b}")
# b = Nihao()
# b.ziji("编程语言","好难")

"""
class A(object):
    #  类的属性
    banji = 1
    __sgsd = 2
    def __init__(self,name,age):    #类的构造方法
        #对象的属性
        self.name = name
        self.age = age
        self.__g = "abc"      #对象的私有属性
    def show(self):           #普通方法                     self   对象本身
        print(f"有个人的名字叫{self.name},年龄是{self.age},班级是{self.banji},其他{self.__sgsd}")
        print(f"在类的方法内部使用类的公有属性{self.banji}"f"私有类属性{self.__g}"f"私有类属性{self._A__g}")
    @staticmethod               #  @staticmethod 将普通方法转变为静态方法的装饰器  def.foo(不要写任何参数)
    def foo():                  #  静态方法    -->    类似于函数
        print("类的静态方法")
    @classmethod
    def koo(cls):               #  类方法       cls 和 self 的作用一致，只不过换了个名字而已
        print("类的类方法")
    def __siyou(self):          #  私有方法
        print("类的私有方法")
    def yu(self):
        self.__siyou()         #   在类的方法中使用其他方法的方式  self.方法名【所有的方法】


#类的使用
a = A(name="张三",age="12")       #   创造对象的过程
a.show()                          #  对象使用类的方法   类的方法只有类的对象能使用
"""
# #   总结：init   是类的构造方法，如果定义了init方法，在创造对象的时候，必须传入参数
#
# #  方法
# """
# 1、静态
# 2、类方法
# 3、普通方法
# 4、私有方法
# """
# # 类的方法可以被哪些使用
# #  1.类中的普通方法不能被  【类名.方法名】   的方式使用        A.show()   报错
# #  2.【对象名.普通方法名】       使用普通方法
# #  3.【对象名.静态方法名】       使用静态方法
# #  4.【对象名.类方法名】         使用类方法
# #  5.私有方法不可以在类的外部使用
# #  6.【类名.静态方法名】，【类名.类方法名】   可以使用类方法，静态方法
# a = A("李四",13)
# a.show()
# a.foo()
# a.koo()

# A.koo()
# A.foo()
# a.yu()
#    @     -->   python的语法糖
#   @staticmethod 将普通方法转变为静态方法的装饰器  def.foo(不要写任何参数)
#   @classmethod  将普通方法转变为类方法的装饰器

# 属性分类
"""
1、类的属性      分为公有，私有



2、对象属性      分为公有，私有

如何区分类的属性和对象的属性
1.类的属性：定义在类的内部，方法的外部
2.对象属性：定义在init方法的内部


类的属性可以被哪些使用
私有:  双下划线开头的   例如   __sex = "男"  
1.类的公有属性可以直接使用；   类名.属性名                            print(A.banji)  
2.类的私用属性不能在类的外部通过  类别.属性名   的方式使用            print(A.__sex)


对象使用类的属性
1.对象的公有属性，通过  对象名.属性名  的方式使用
2.对象的私有属性，不能在对象外部通过  对象名.属性名 的方式使用


类名.对象的属性  是不可以的

私有属性在定义之后，不希望被修改，可以通过: self变量.__名/self._类名__变量名的方式使用它
"""


# b = A("张d","1")
# print(b.age)
# print(b.banji)


#      继承
class B(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f"B类的普通方法")
        return self.name, self.age
#   (类名)     ——>      继承于xx类     只要被继承类有的，继承类都可以直接使用
class C(B):
    def talk(self):
        res = self.say()  # res = super().say()
        print(res)

    #  多态         -->    重写方法
    def say(self):
        print("C类里方法")


c1 = C("张三", "13")
c1.talk()
c1.say()

"""
多态
继承类对被继承的方法的重写 【方法名一样，语句块不一样】
如何在多态之后使用被继承类的方法 ，使用super().被继承类的方法
"""











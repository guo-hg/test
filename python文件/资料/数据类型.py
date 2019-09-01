#!/sur/bin/python
# -*-coding:utf-8-*-
# c=True
# d=False
# if d:
#     print("hello python")
# else:
#     print("if条件为假的时候输出else语句内容")




# while True:
#     name = input("请输入用户名")
#     password = input("请输入密码")
#     if name == "g":
#         if password == "123456":
#             print("登录成功")
#             break
#         else:
#             print("密码错误，登录失败")
#     else:
#             print("用户名错误，登录失败")


# num_1 = 10
# num_2 = 20
# # t = num_1 + num_2
# # print(t)
# # s = num_1 - num_2
# # print(s)
# # e = num_1 * num_2
# # print(e)
# # q = num_2 // num_1
# # print(q)

# num_3 = 101
# num_4 = 5
# a = num_3 % num_4
# print(a)
# print(num_3 ** num_4)
# r = (num_3 // num_4)
# print(r)


# 计算机   输入任意两个数字进行计算，选择计算方式
# while True:
#     number1 = int(input("输入一个数字"))
#     number2 = int(input("输入另一个数"))
#     number3 = input("输入运算方法")
#     a = (number1 - number2)
#     b = (number1 + number2)
#     c = (number1 * number2)
#     d = (number1 / number2)
#     if   number3  == "-":
#         print (a)
#         break
#     elif number3  =="+":
#         print(b)
#         break
#     elif number3 =="*":
#         print(c)
#         break
#     elif number3 =="/":
#         print(d)
#         break
#     else:
#         print("运算方式错误，请重新输入")





# 求学生成绩是否优秀,良好,及格,不及格
# while True:
#     number = int(input("输入学生成绩"))
#     if number>=90:
#         print("优秀")
#     elif    80<=number<=90:
#         print("良好")
#     elif     60<=number<80:
#         print("及格")
#     elif    0<number<60:
#         print("不及格")
#     else:
#         print("输入错误，请重新输入")





# a = 108
# a  %=  5    #   a =   a  % 5
# print(a)

# x = 100
# y = 50
# z = 30
# if x > y and y > z:
#      print("x的值最大")
# if x >y or z > x :
#      print("正确")
#
# if not x == 100:
#      print("x不等于100")
# else:
#      print("not 语句不成立")

# 判断三角形是否为三角形
# a = int(input("输入一个最长边"))
# b= int(input("输入一个边"))
# c = int(input("输入另一个边"))
# if (a+b>c  and  b+c>a  and a+c>b) or (a-b<c and a-c<b and b-c<a) :
#      # print("三角形")
#      if b*b+c*c == a*a:
#           print("直角三角形")
#      if a*a>b*b+c*c:
#           print("钝角三角形")
#      if a*a<b*b+c*c:
#           print("锐角三角形")
# else:
#      print("不是三角形")


# a = int(input("输入一个数字"))
# b = int(input("输入第二个数字"))
# c = int(input("输入第三个数字"))
# if a > b > c :
#      print(f"{a} {b} {c}")
# if c > b > a:
#      print(f"{c} {b} {a}")
# if b > a > c:
#      print(f"{b} {a} {c}")
# if a > c > b :
#      print(f"{a} {c} {b}")
# if b > c > a :
#      print(f"{b} {c} {a}")
# if c > a > b :
#      print(f"{c} {a} {b}")

# a = "zhongguo"
# b = "0"
# if b  not in a :
#      print("成立")
# else:
#      print("不成立")

# a = 'hello'
# b = "world"
# c = """ 你好"""
# d3 = ""
# if d3:
#      print("真")
# else:
#      print("假")
#
# a = 'hello'
# b = len(a)
# print(b)

# 字符串拼接
# a = 'hello'
# b = "world"
# c = a + b
# print(c)

# 字符串重复输出
# print("中国，你好 \n" * 5)



#字符串切片
# 步长 指的是间隔几个取值，默认是1，开始的索引值默认是0，结束的索引值默认是最后一个
# a = "中华人民共和国万岁"
# # 取字符 字符串变量名字 [索引值]
# #索引值
# print(a[-2])
# print(a[1:3])
# print(a[1:8:2])
# print(a)

# for i in  range ( 100 , 1000):
#      a = i // 100
#      b = i // 10 %  10
#      c = i %  10
#      if  i == a ** 3 + b ** 3 + c ** 3  :
#           print(i)
     # s = str(i)
     # bai = int(s[0])
     # shi = int(s[1])
     # ge = int(s[2])
     # if i == bai ** 3 + shi ** 3 + ge ** 3:
     #      print(i)




#查找字符串中的子字符串，find()
# a = "hello"     #定义字符串a
# b = "0"         #定义子字符串b
# print(a.find(b))
# print(a.rfind(b))
# #
# # #   index()查找字符串中的子字符串，如果找到，返回子字符串的第一个字符的索引值,找不到抛出异常
# print(a.index(b))

# c = "hello world"
# b ="l"
# print(c.title())
# #
# print(c.upper())      #upper()    小写转大写
# print(c.count(b))
#
# str_1  = "HELLO world"
# print(str_1.swapcase())


str_2 = "asfwef123454467890"
# a = "4"
# print(str_2.count(a))
# print(str_2.startswith("博文"))
# print(str_2.startswith("a"))
#
# print(str_2.endswith("博文"))
# print(str_2.endswith(" "))

# print(max(str_2))
# print(min(str_2))
#
#
# name = "博文"
# age = "18"
# srt_3 = f"我在的学校是{name},我今年{age}岁"
# print(srt_3)
#
# str_4 = "我在的大学是{},我今年{}岁".format(name, age)
# print(str_4)
#
str_5 = "I know I beautiful"
# print(str_5.split(" ",1))
#print("中国 \n"* 4 )
# print(str_5.split("I",1))

# number = "hello world python"
# b = len(number)
# # print(b)
# d = number.split(" ")
# print(d)
# print(d[-1])


# number = input("输入一段英文")
# a = number.split(" ")
# print(a)
# # print(len(a[-1]))
# print(f"最后一个单词的长度是:{len(a[-1])}")

# str_11 = " 博文智生1903"
# print(f"原始字符串:{str_11}")
# print(f"删除之后的字符串:{str_11.lstrip()}")
# print(f"删除之后的字符串{str_11.lstrip('博')}")

# print(str_11.replace(" ","河南"))          #替换
# print(str_11.replace("asdasd","河南"))

# s1 = "国了"     #  拼接
# s2 = ["中","人","家"]
# print(s1.join(s2))

# s3 = "14"
# print(s3.isdigit())

# s4 = "Helloworld \n"
# print(s4.istitle())
# print(s4.isalnum())
# print(s4.isalpha())
# print(s4.isspace())
# print(s3.isdecimal())


# s = "hello world"
# for i in s:
#     print(f"子字符是{i}")











#







   # 列表——list
#定义一个列表
# l = [ "abc",1,["hello",2019] ,[23432325] ]
# print(l)
# 定义一个空列表
# s = []
# print(s)
# print(l[2])  #当只取一个元素的时候返回该元素本身的数据类型
# print(l[1:3])
# # #                #type()   是用来判断数据类型的，print(type(l[-1]))
# print(type(l[-1]))
# # #如何获取l = [ "abc",1,["hello",2019] ]列表中的列表元素？ 如何获取“hello”？
# k = l[-2]
# print(k[0])     #第一种
# print(l[-2][0])   #第二种方法
#替换列表中的元素
# l = [ "abc",1,["hello",2019] ]
# print(f"之前的列表{l}")
# l[0] = "博文"
# print(f"之后的列表{l}")
# print(l)

#向列表中添加元素，append(需要添加的元素),在列表的尾部新增添加的元素
# l = [ "abc",1,["hello",2019] ]
# l.append("pythpon")
# print(f"添加元素之后的l列表{l}")

#列表支持拼接

# l1 = [1,2,3]
# l2 = ["a","b","c"]
# l3 = l1 + l2
# print(l3)

#支持重复输出，将重复输出的元素放到一个列表中
# l1 = [1,2,3]
# print( l1 * 2)


# a = "1234567654321234567"
# print(a[4:6])
# b = [1,4,3,[24532],4,76]
# print(b[2:5])
#
#
# #列表反转
# a = [1,2,3]
# print(a[:: -1])

#count(需要统计的元素)，作用：统计列表中某个元素出现的次数，返回的是数值,如果统计的元素不存在，返回的数值是0

# a = [ "a","a","a",1,2,3]
# b = a.count("a")
# print(f"a元素出现的次数是:{b}")
# c = a.count("12")
# print(f"12元素出现的次数是：{c}")

#extend(需要添加的元素): 向列表内添加元素，【可以添加多个元素】，默认添加到列表的尾部
#需要添加元素：可以是列表，元组，集合，字典
# q = ["123",456]
# w = [["自己"]]
# q.extend(w)    #向列表添加多个元素的过程
# print(q)

# index (需要查找的元素) 如果找到该元素返回元素对应的索引值，如果找不到抛出异常
# q = ["123",456]
# print(q.index(456))
# print(q.index(W))

#insert(index,需要添加的元素)：向列表内的指定位置插入元素
#index:指索引值

# c = ["12","243",322,34]
# c.insert(2,["55",43])
# print(c)



#pop(写索引值):删除列表中的元素，当索引值不写的时候，默认删除最后一个元素,返回被删除的元素
# c = ["12","243",322,34]
# print(c.pop(3))
# print(c)
#remove(指定需要删除的元素)：删除列表中的元素
# d = ["1212","321",4,23,13]
# d.remove("1212")
# print(d)

#reverse()：反转列表中的元素
# d = ["1212","321",4,23,13]
# d.reverse()   #反转的过程
# print(d)

#sort(reverse=False):对列表内的元素进行排序，按照ASCII码排序，默认是升序
# reverse= True   降序   不能使用多种类型
# d = [ 1,3,4,2,5,11,33]
# d.sort(reverse=True)
# print(d)
# c = [ 3,2,6,4,55,33,23,12]
# c.sort()
# print(c)

#clear() 清空列表
# d = [ 1,3,4,2,5,11,33]
# d.clear()
# print(d)

#copy():复制列表
# e = [1,2,3,4]
# f= e.copy()
# print(e)
# print(f)

#len()  求列表长度
# e = ["a","b","c","d"]
# print(len(e))

#max() 求列表中元素最大值    不能使用多种类型
# print(max(e))
#min() 求列表中元素最小值，不能使用多种类型
# print(min(e))
#list() 将非列表类型转化为列表类型
# str_1 = "1234"
# print(list(str_1))

#使用input()输入一段话，将字符串转化成列表，判断列表中元素有多少个数字，首字符大写，求出相应的个数
# a = input("输入一段话")
# b = a.split(" ")
# b1 = list(b)
# c = len(b1)
# print(c)
# print(b1)
# e = 0
# f = 0
# for d in range(c) :
#     if b1[d].isdigit():
#         e = e + 1
#     if b1[d].istitle():
#         f = f + 1
# print(f"数字{e}个")
# print(f"首字母大写{f}个")



#enumerate
# a = ["a","b","c","d"]
# for i ,j in enumerate(a):
#     print(i,j)

# a = input("输入商品名")
# b = input("购买数量")
# i = ['方便面','矿泉水']
# j = [100,200]
# for m,n in enumerate(i):
#     print(m,n)
#     if n == a:
#         zongjia = j[m] * int(b)
#         print(f"商品名:{a},数量:{b},单价:{j[m]},总价:{zongjia}")
#         break
# else:
#     print("商品不存在")



# a,b = 1 , 2
# print(f"a的值是{a}")
# print(f"b的值是{b}")









#python 的基本数据类型      元组
# t = (1,"2",[1,2],{99:1234},(44))
# print(t)
# print(type(t))
#元组支持拼接，结果是一个新的元组
# t1 = ("hello","world")
# t2 = t + t1
# print(t2)
#元组支持重复输出，结果是一个新的元组
#print(t1 * 2)
#元组支持索引，结果是一个新的元组
#print(t[1:3])
#反转元组里的元素
#print(t[:: -1])
#求元组的长度   len()
#print(len(t))
#max()    求元组的最大值
# t3 = (1,2,3,4,5)
# print(min(t3))
# print(max(t3))

#count("需要统计的元素")       统计元组中某个元素出现的次数
#t = (1,"2",[1,2],{99:1234},(44))
# print(t)
#print(t.count(1))

#index("需要查找的元素")   返回元素在元组中的索引值
# print(t.index("2"))

#异常：
#print(t.index("hell"))
#ValueError: tuple.index(x): x not in tuple


#del  跟元组的变量名   删除元组
# t = (1,)
# del t
# print(t)


# s = '[Description("衣物挑战5kg")]@        /medal/201906/24/Cloth_Single_5.png         @        /medal/201906/24/Cloth_Single_5_Get.png     @            [Description("衣物挑战10kg")]@        /medal/201906/24/Cloth_Single_10.png        @        /medal/201906/24/Cloth_Single_10_Get.png    @            [Description("衣物挑战15kg")]@        /medal/201906/24/Cloth_Single_15.png       @        /medal/201906/24/Cloth_Single_15_Get.png   @            [Description("衣物挑战20kg")]@        /medal/201906/24/Cloth_Single_20.png       @        /medal/201906/24/Cloth_Single_20_Get.png    @           [Description("衣物挑战25kg以上")]@        /medal/201906/24/Cloth_Single_25.png        @        /medal/201906/24/Cloth_Single_25_Get.png   @            [Description("衣物累计50kg")]@        /medal/201906/24/Cloth_Sum_50.png           @        /medal/201906/24/Cloth_Sum_50_Get.png'
# 题目要求
# 将类似/medal/201906/24/Cloth_Single_5.png的放到一个列表内
# 将类似/medal/201906/24/Cloth_Single_5_Get.png的放到一个列表内

# print(s)
# print(type(s))
# print(s.split())
# s1 = s.split()
# print(type(s1))
# a = []
# b = []
# for i in  s1:
#     if i.find("Get.png") != -1:
#         a.append(i)
#     elif i.find("png") != -1:
#         b.append(i)
# print(f"类似Get.png{a}")
# print(len(a))
# print(f"类似png  {b}")
# print(len(b))

# a = (1,)
# print(type(a))


#
#集合
# s = set()     # 定义空字典
#
# print(type(s))
#
# s1 = {"1",2,(2019)}
# print(s1)

#add(需要添加的元素)  向集合添加元素
# s1.add("python")
# print(s1)

#remove("需要删除的指定元素")    删除集合内的指定元素   指定元素不存在就会报错
# s1.remove("python")
# # print(s1)
# # s1.remove("中国")     #报错内容：KeyError: '中国'
# # print(s1)

#pop()  随机删除一个元素，默认删除最后一个元素
# s1.pop()
# print(s1)


#discard("指定删除的元素")  删除集合内的指定元素，指定元素不存在不报错
#s1.discard(2)
#print(s1)


#update("集合")   将集合B中的元素添加到集合A里
# s2 = {"2019",2019}
# s1.update(s2)
# print(s1)
#copy()   复制集合
#s2 = s1.copy()
#print(s2)
#clear()   清空结合
# s2.clear()
# print(s2)

# s3 = {1,2,3,4,5,6}
# s4 = {3,4,5,6,7,8}

#difference("集合"):  求集合B相对于集合A的差集

# n = s3.difference(s4)      #s3集合A     s4集合B
# print(n)


# print(s3)
#differnece_update("集合B"):  删除多个集合中都存在的元素，操作是在集合A上执行的
# s3.difference_update(s4)
# print(s3)

#intersertion("集合"):    求集合A,B的交集，没有交集返回空集
# j = s3.intersection(s4)
# print(j)

#intersertion_update("集合B")  删除不是交集的部分,返回删除后的集合A
# s3.intersection_update(s4)
# print(s3)

#isdisjoint(集合B)判断两个集合是否存在交集，不存在交集返回True，存在返回false

# print(s3.isdisjoint(s4))
#issubset("集合B"):  判断集合B是否是集合A的子集，是返回True，不是返回False

#print(s4.issubset(s3))

#issuperset(""),判断集合B中的元素是否全部在集合A中，是返回True，不是返回False。
# print(s3.issuperset(s4))
#symmetric_difference() 找出两个集合中不相同的元素，返回一个新的集合
# n3 = s3.symmetric_difference(s4)
# print(n3)
#symmetric_difference_update("集合B")
#找出两个集合相同的部分，并将集合A中的元素全部删除，将不同的元素放入到集合A
# s3.symmetric_difference_update(s4)
# print(s3)


#union("集合B"):   求集合A，B的并集，返回一个新的集合，重复的元素只出现一次

# s3 = {1,2,3,4,5,6}
# s4 = {3,4,5,6,7,8}
#
# n4 = s3.union(s4)
# print(n4)

# import random            #随机数模块
# a = random.randint(0,1000)           #随机生成一个整数
# print(a)
#
# a = set()
# c = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for n in range(1,5):
#             if i != j and j != n and i != n:
#                 b = i * 100 + j * 10 + n
#                 a.add(b)
#                 c = c + 1
# print(c)
# print(a)


#输入一个数判断奇偶
# a = input("输入一个数")
# if int(a)%2 == 0 :
#     print(f"{a}是个偶数")
# else:
#     print(f"{a}是个奇数")


#一张纸厚0.08mm，建筑物高8843m，纸折多少次，求超过建筑物高度
# a = 0.08
# b=8843000
# c=0
# while  a<b:
#     a=a*2
#     c+=1
#     # print(a)
# print(c)

#
# for i in range(1,10):
#     for j in range(1,i+1):
#         a = i*j
#         print(f"{j}*{i}={a}\t",end="")
#     print()



# a = input("输入一串数")
# b = a.split()
# print(b)
# c = len(b)
# print(c)
# for i in range(c):
#     j = i -1
#     for j in range(c):
#         if  int(b[i] < b[j]):
#             m = b[i]
#             b[i] = b[j]
#             b[j] = m
# print(b)







# a = "hello world"
# print(a.upper())
# print(a.count("l"))
# print(a.startswith("h"))
# print(min(a))
# name = "博文"
# age = "18"
# str = f"我的单位是{name},我今年{age}岁"
# str1 = "我的单位是{},我今年{}岁".format(name,age)
# print(str)
# print(str1)
# b = a.split(" ")
# print(b)
# print(f"最后一个单词的长度是{len(b[-1])}")
# print(a.replace("hello","世界"))
# s = "zhong"
# s1 = ["wo","shijie","ai"]
# print(s.join(s1))
# print(s.isdigit())

#定义字典
# n = {
#     "m":[100,"123",[121]]
# }
# print(n)
#定义空字典
# d = {}
#向字典内添加元素
# d["a"] = "字典的值"
# print(d)
#当字典的键存在，再对键进行赋值的时候，会更改原来的键对应的值
# d["a"] = "新的字典的值"
# print(d)
#获取字典中键对应的值，通过键取值
d = {
   "a":100,
   "b":["列表"],
   "c":["列表",1,2,3]
}
# print(d["a"])                   #第一种方法
# value = d.get("a")
# print(value)        #第二种方法                  get("字典键") :  获取字典中对应的值

#keys():   获取字典中所有的键
# d = {
#     "a":100,
#     "b":["列表"],
#     "c":["列表",1,2,3]
# }

# m = d.keys()
# print(m)
#values() 获取字典所有的值
# values = d.values()
# print(values)
#clear()   清空字典中所有的元素
# clear = d.clear()
# print(d)
#copy()    复制字典
# copy = d.copy()
# print(d)
# print(copy)

#pop("需要被删除的key") 删除字典中给定key对应的值
# print(f"原来的字典{d}")
# print(d.pop("a"))
# print(f"删除后的字典{d}")
#popitem()  默认删除字典中最后一个键值对，返回一个新的字典
#print(f"删除之前的字典{d}")
# d.popitem()
# print(f"删除之后的字典{d}")
#len()  求字典的键值对个数
# l = len(d)
# print(l)

#fromkeys(seq,value)   新建字典，设置默认值
#seq    传入一个有序的对象，列表，元组
#value   设置字典键对应的值，可以不写，  none 代表空
seq = [ 1,2,"3"]
new_d = dict.fromkeys(seq,"bowen")
print(new_d)

#items();  将字典中的键值对转换为元组，可以被循环【for】使用
print(f"原本字典{d}")
a = d.items()
print(a)
for i,j in a:
    print(i,j)
#update("需要添加的字典的变量名")   将多个字典组合成一个字典
#d1 = { 1 : "hello" , "a" : "字典一"}
#d2 = { 2 : "world" , "b" : "字典二"}
#d3 = d1.update(d2)     #字典组合添加的过程   谁在前面，就是把后面的字典添加给前面的字典
# print(d1)
# print(d2)
#setdefault("key",默认值)    向字典中添加键值对，并设置默认值
#key: 需要新增的默认值
#默认值：符合基本数据类型都行
# k = { 1 : 1000, 2 :2000}
#添加不存在的key，设置默认值
# k.setdefault("key1",["默认值"])
# print(k)
#如果设置的key已经存在，不更改键值对
# k.setdefault("key1")
# print(k)


#当直接使用for循环的时候，输出的是字典的键，没有值。
# for i in k:
#    print(i)
#字典转字符串
# print(str(k))
#判断数据类型，使用type()
# print(type(str(k)))





#去除列表中重复的元素
# h = [ 1,2,3,3,4,2,3,1]     #输出成[1,2,3,4]    顺序无所谓
# print(type(h))
# m = dict.fromkeys(h)
# c = []
# for i in m:
#     #print(i)
#     c.append(i)
# print(c)
# for i in h:        #第二种
#     if h.count(i)>=2:
#         print(h)
#         h.remove(i)
# print(h)

# a = [1,1,2,3,4,5,4,6,7,4]     #第三种
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
# a = input("输入一个字符串")   #key
# b = input("输入另一个字符串")  # value
# n = a.split()           #key
# m = b.split()           # value
# c = {}
# if len(n) == len(m):
#     for i in range(len(n)):
#         c[n[i]] = m[i]
# elif len(n) < len(m):
#     for j in  range(len(m)):
#         if j >=len(n):
#             c["bowen"] =m[j]
#         else:
#             c[n[j]] = m[j]
# else:
#     for q in range(len(n)):
#         if q <= (len(m)-1):
#             c[n[q]] = m[q]
#         else:
#             c[n[q]] = "none"
# print(c)



#s = {
    #"key1": [1000, 2000, 3000],
    #2019: ["hello",{"python": ['py2.x', 'py3.x']},],
#}
# print(s)
# 1、求 key1 对应value的和
# 2、求 python 对应的值，并将每个版本的首字符大写、尾字符大写输出

# print(s.get("key1"))
# j = 0
# for i in range(len(s.get("key1"))):
#     j = j + s.get("key1")[i]
# print(j)
# print(s.get(2019)[1]["python"])
# print(s.get(2019))
# a = s.get(2019)[1]["python"]
# print(a)
# for i in a:
#     b = i.title()
#     print(b)

# a = 0
# for i in range(2,101):
#     for j in range(2,i+1):
#         if i % j == 0:
#             break
#     if i == j:
#         a = a +j
# print(a)





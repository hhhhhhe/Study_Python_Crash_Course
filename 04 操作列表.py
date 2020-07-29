# 遍历整个列表
# 使用for循环
names = ['小林1','小林2','小林3','小林4','小林5']
for name in names : 
	print(name)

#创建数值列表
#使用函数range(),可以生成一系列的数字,指定第一个值开始，到第二值前截至，就是不会显示最后一个数字
for value in range(1,50):#不会打印出50，只打印到49
	print(value)

#创建数字列表，可以使用函数list()
numbers = list(range(1,6))

#range()函数可以指定步长
range(1,11,2)#从1开始到11，步长为2

#如何将前10个整数的平方加入到一个列表中：
squares = [] 
for value in range(1,11): 
    square = value**2 
    squares.append(square) 
print(squares)

#对数据列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)#求数字列表中的最小值
max(digits)#求数字列表中的最大值
sum(digits)#求数字列表中的总值

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)
要使用这种语法，首先指定一个描述性的列表名，如squares；
然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。
在这个示例中，表达式为value**2，它计算平方值。接下来，编写一个for循环，用于给表达式提供值，
再加上右方括号。在这个示例中，for循环为for value in range(1,11)，
它将值1～10提供给表达式value**2。请注意，这里的for语句末尾没有冒号。

#使用列表，切片(与range()函数一样，也是在第二个参数之前就会停止)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) 
#如果没有指定第一个参数，就会从第一个列表数值开始
#如果没有指定第二个参数，就会从最后一个列表数值结束
players[-3:]#使用负号输出倒数数值，这里是输出倒数三个名字
for play in players[-3:] #遍历倒数三个数值

#复制列表
players2 = players[:]#第一个参数与第二个参数没有设置，意味着是整个列表复制到新列表中


#元组：python将不能修改的值称为不可改变，而不可变的列表称为元组
#元组看起来与列表差不多，但元组是使用圆括号将其括起来的，而列表是使用方括号将其括起来的
ages(10,13,8)
age[0]#元组也可以使用下标进行搜索
#遍历元组中的值还是可以使用for
for age in ages :
	print(age)
#ages[0]=11会报错，因为元组是不可以修改值的，当整个元组是可以新赋值的
#ages(11,12,13)不会报错

#格式设置指南
#-每级缩进四个空格
#-每行不超过80字符
#-把不同部分分开，可使用空行





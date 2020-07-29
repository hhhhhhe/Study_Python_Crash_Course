#检查是否相等时不考虑大小写
#在python中检查是否相等是区分大小写，两个大小写不同的值会被视为不相等
car.lower() == 'audio' #这样就不区分大小写了，lower()也不会改变car中的值
#判断是否不等!=
#检查特定值是否包含在列表中，列表元素 in 列表，结果是一个true或者false
#检查特定值是不是不包含在列表中，not in
#布尔表达式

#经常需要检查超过两个的情形，为此可使用Python提供的if-elif-else结构。
#Python只执行if-elif-else结构中的一个代码块，它依次检查每个条件测试，
#直到遇到通过了的条件测试。

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
#可以不用else语句
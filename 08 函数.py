1、定义函数
不传参
def greet_user(): 
    """显示简单的问候语""" 
    print("Hello!") 
greet_user() #即便括号里没有参数，括号还是不可以不写

传参
def greet_user(name): 
    """显示简单的问候语""" 
    print("Hello!") 
greet_user('小林')
name是形参，小林是实参

鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；
也可使用关键字实参，其中每个实参都由变量名和值组成；
还可使用列表和字典。

位置实参
调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参。

关键字实参
传递给函数的名称-值对。
关键字实参的顺序无关紧要，因为python知道各个值该存储到哪个形参中。

参数设置默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='willie')
由于给animal_type指定了默认值，无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名字。
然而，Python依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。
这就是需要将pet_name放在形参列表开头的原因所在。

返回值
使用return返回函数处理后的值
让实参变成可选的
把形参的值设置为'',然后移到最后一个形参的位置

等效函数调用
#一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#返回字典
#函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个表示人的字典：
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name} 
    return person 
musician = build_person('jimi', 'hendrix')
print(musician) 

#向函数传递列表与在函数修改列表
将列表传递给函数后，函数就可对其进行修改。
在函数中对这个列表所做的任何修改都是永久性的，
这让你能够高效地处理大量的数据。

#将列表的副本传递给函数，就可以不修改原来的列表的内容了
function_name(list_name[:])

#传递任意数量的实参
有时候，你预先不知道函数需要接受多少个实参，
好在Python允许函数从调用语句中收集任意数量的实参。

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
形参名*toppings中的星号让Python创建一个名为toppings的空元组，
并将收到的所有值都封装到这个元组中。

如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first 
    profile['last_name'] = last
    for key, value in user_info.items(): 
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
函数build_profile()的定义要求提供名和姓，同时允许用户根据需要提供任意数量的名称—值对。
形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中。

#将函数存储在模块中
提供给函数指定描述性名称，可以让主程序任意理解得跟多。将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。
import语句允许在当前运行的程序文件中使用模块中的代码。

#导入整个模块
import pizza #import + 模块名字
pizza.make_pizza(16, 'pepperoni') 
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
Python读取这个文件时，代码行import pizza让Python打开文件pizza.py，并将其中的所有函数都复制到这个程序中。
你看不到复制的代码，因为这个程序运行时，Python在幕后复制这些代码。你只需知道，在making_pizzas.py中，可以使用pizza.py中定义的所有函数。
要调用被导入的模块中的函数，可指定导入的模块的名称pizza和函数名make_pizza()，并用句点分隔它们（见❶）。

#导入特定的函数
frommodule_name importfunction_0, function_1, function_2
通过使用逗号分隔函数名，可根据需要从模块中导入任意数量的函数

#使用as给函数指定别名
要给函数指定这种特殊外号，需要在导入它时这样做
这是在import语句中使用make_pizza as mp实现的，关键字as将函数重命名为你提供的别名：
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
上面的import语句将函数make_pizza()重命名为mp()；在这个程序中，每当需要调用make_pizza()时，都可简写成mp()，而Python将运行make_pizza()中的代码，这可避免与这个程序可能包含的函数make_pizza()混淆。
指定别名的通用语法如下：
frommodule_name importfunction_name asfn

#导入模块中的所有函数
使用星号(*)运算符可让python导入模块中的所有函数
导入的模块中含有的函数名若与文件中函数名相同会引发错误，所以最佳的做法是，要么只导入需要的函数，要么导入整个模块并使用句点表示法。

#函数编写指南
1、应给函数指定描述性名称，且只在其中使用小写字母和下划线
2、每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数i当以后面，并采用文档字符串格式
3、若程序或模块包含多个函数，可使用两个空行将相邻的函数分开。


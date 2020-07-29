#字典是一系列键-值对。每一个键都与一个值相关联，可以通过键来访问与之相关联的值，任何python对象都可以作为字典中的值
alien = {'color':'green','points':'5'}
#访问字典中的值
alien['color']
#创建一个空字典
alien = {}
alien['color']='green'
alien['points']=15
#修改字典中的值
alien['color']='yellow'
#删除键-值对，删除后的键-值对是永远会消失的
del alien['points']
#遍历所有的键-值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items(): 
    print("\nKey: "+key) 
    print("Value: "+value) 
#要编写用于遍历字典的for循环，可声明两个变量，
#用于存储键—值对中的键和值。对于这两个变量，可使用任何名称。
#下面的代码使用了简单的变量名，这完全可行：
for k, v in user_0.items()
#for语句的第二部分包含字典名和方法items()，
#它返回一个键—值对列表。接下来，for循环依次将每个键—值对存储到指定的两个变量中。
#在前面的示例中，我们使用这两个变量来打印每个键及其相关联的值。
#第一条print语句中的"\n"确保在输出每个键—值对前都插入一个空行：
#注意，即便遍历字典时，键—值对的返回顺序也与存储顺序不同。Python不关心键—值对的存储顺序，而只跟踪键和值之间的关联关系。

#遍历字典中的所有键keys()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favorite_languages.keys(): 
    print(name.title())
#方法keys()并非只能用于遍历，它会放回一个列表，其中包含字典中所有键

#按顺序遍历字典中的所有键sorted()
#使用函数sorted()来获得按特定顺序排列的键列表的副本：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(name.title()+", thank you for taking the poll.")
#这条for语句类似于其他for语句，但对方法dictionary.keys()的结果调用了函数sorted()。这让Python列出字典中的所有键，并在遍历前对这个列表进行排序。输出表明，按顺序显示了所有被调查者的名字：

#遍历字典中的所有值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title)
	
#剔除字典中重复的值 set()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): 
    print(language.title())

#嵌套
#将一系列字典存储在列表中，或者将列表作为值存储在字典中，这称为嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2] 
for alien in aliens:
    print(alien)
# 存储所点比萨的信息
pizza = { 
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#在字典中存储列表
# 概述所点的比萨
print("You ordered a "+pizza['crust']+"-crust pizza "+
    "with the following toppings:")
for topping in pizza['toppings']: 
    print("\t"+topping)
	
#在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items(): 
    print("\nUsername: "+username) 
    full_name = user_info['first']+" "+user_info['last'] 
    location = user_info['location']
    print("\tFull name: "+full_name.title()) 
    print("\tLocation: "+location.title())


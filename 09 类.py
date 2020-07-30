一、Python 作用域和命名空间
namespace （命名空间）是一个从名字到对象的映射。 大部分命名空间当前都由 Python 字典实现，但一般情况下基本不会去关注它们（除了要面对性能问题时），而且也有可能在将来更改。 
命名空间的例子：存放内置函数的集合（包含 abs() 这样的函数，和内建的异常等）；模块中的全局名称；函数调用中的局部名称。
注意：不同命名空间中的名称之间绝对没有关系，两个不同的模块都可以定义一个 maximize 函数而不会产生混淆 --- 模块的用户必须在其前面加上模块名称。。

作用域 是一个命名空间可直接访问的 Python 程序的文本区域。 
这里的 “可直接访问” 意味着对名称的非限定引用会尝试在命名空间中查找名称。

如果一个名称被声明为全局变量，则所有引用和赋值将直接指向包含该模块的全局名称的中间作用域。 
要重新绑定在最内层作用域以外找到的变量，可以使用 nonlocal 语句声明为非本地变量。 
如果没有被声明为非本地变量，这些变量将是只读的（尝试写入这样的变量只会在最内层作用域中创建一个
新的 局部变量，而同名的外部变量保持不变）。
 
 Python 的一个特殊规定是这样的 
 -- 如果不存在生效的 global 或 nonlocal 语句 
 -- 则对名称的赋值总是会进入最内层作用域。 
 
 global 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；
 nonlocal 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定。
 
 global与nonlocal
1.函数内部定义的为局部变量，其作用域是局部作用域，函数外无法调用的
2.函数外定义的为全局变量，其作用域是全局作用域，如果在函数内想要进行修改，需要使用global修饰变量
3.外层函数的变量，如果想要在内层函数进行修改，需要nonlocal

 def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

结果：
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam

二、类对象
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
类对象支持两种操作：属性引用和实例化。
如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例
三、继承
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
名称 BaseClassName 必须定义于包含派生类定义的作用域中。 也允许用其他任意表达式代替基类名称所在的位置。
多重继承
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>



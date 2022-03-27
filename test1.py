"""
 * Project name(项目名称)：Python_MetaClass元类
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/27 
 * Time(创建时间)： 20:24
 * Version(版本): 1.0
 * Description(描述)： MetaClass元类，本质也是一个类，但和普通类的用法不同，
 它可以对类内部的定义（包括类属性和类方法）进行动态的修改。使用元类的主要目的就是为了实现在创建类时，能够动态地改变类中定义的属性或者方法。
 如果想把一个类设计成 MetaClass 元类，其必须符合以下条件：
必须显式继承自 type 类；
类中需要定义并实现 __new__() 方法，该方法一定要返回该类的一个实例对象，因为在使用元类创建类时，该 __new__() 方法会自动被执行，用来修改新建的类。
 """


class FirstMetaClass(type):
    def __new__(mcs, name, bases, attrs):
        # 动态为该类添加一个name属性
        attrs['name'] = "张三"
        attrs['say'] = lambda self: print("调用 say() 实例方法")
        return super().__new__(mcs, name, bases, attrs)


class C(object, metaclass=FirstMetaClass):
    pass


if __name__ == '__main__':
    c = C()
    print(c.name)
    c.say()
    print(type(c))

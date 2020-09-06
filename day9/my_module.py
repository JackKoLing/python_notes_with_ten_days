"this file use to test import module."

x = 30

def print_info():
    print(x+30)

class MyClass():
    data = 'hello myclass'
    
    def __init__(self, who):
        self.name = who
    
    def print_name(self):
        print(self.data, self.name)

if __name__ == '__main__':
    # 如果不是导入的模块，则name属性是main，这个常用于自我测试
    print_info()
    ins1 = MyClass('jackko')
    ins1.print_name()

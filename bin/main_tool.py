import bin.TimeTool
import time

from bin.getDouBanWebData import time_stamp
from bin.TimeTool import timeTool


#from bin.getDouBanWebData import main


class main_tool:
    def __init__(self):
        pass

#创建对象后，才能通过对象名和点运算符访问属性和方法
    def main(self):
        #AttributeError: 'str' object has no attribute 'time_str',
        #这个报错说明time_example 没有被实例化,即没有创建成功为对象
        #想要创建成为对象，就需要使用类名（类名）（），才会创建一个对象
        #而这个场景生成的是timeTool的实例化对象，又需要传入一个参数，这个参数就是time_str，而这个参数是字符串类型，即我想要用的时间
        time_example  = timeTool("2024-09-29 20:06:10")
        time_one = bin.timeTool.timeTool.get_time(time_example)
        print(time_stamp())
        print(time_one)

        return time_one


if __name__ == '__main__':
    res = main_tool().main()
    print(res)
   #res = main_tool()
   #res.

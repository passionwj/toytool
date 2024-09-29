import  time
import datetime



class  TimeTool:
    def __init__(self,time_str):
        self.time_str = time_str

    def get_time(self):
        time_array = time.strptime(self.time_str, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    def make_time_stamp(self):
        time_stamp =time.time()
        return time_stamp

    def make_time_readable(self):
      #  time_stamp = time.time()
      #  time_array = time.localtime(time_stamp)
        readable_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        return readable_time


if __name__ == '__main__':
    print(TimeTool(1).make_time_stamp())
    print(TimeTool(1).make_time_readable())
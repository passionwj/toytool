import  time
import datetime


class  timeTool:
    def __init__(self,time_str):
        self.time_str = time_str

    def get_time(self):
        time_array = time.strptime(self.time_str, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array))
        return time_stamp

    def get_time_by_day(self,day):
        time_array = time.strptime(self.time_str, "%Y-%m-%d %H:%M:%S")


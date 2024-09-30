import xlwt
import xlrd
import os
import sys

from xlwt import Workbook

from bin.getDouBanWebData import dataList


class Xlwtexcel:
    def __init__(self):
        self.workbook = xlwt.Workbook()


    dataList = []
    @staticmethod
    def save_excel_douban(path):
        print(path)
        workBook = xlwt.Workbook(encoding='utf-8')
        #设置参数允许覆盖单元格中已有的数据。
        sheet = workBook.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
        col = ("电影详情链接", "图片链接", "电影中/外文名", "评分", "评论人数", "概况", "相关信息")
        for i in range(0, 7):
            sheet.write(0, i, col[i])
            #print(col[i])
        for i in range(0, 250):
            print('正在保存第' + str((i + 1)) + '条')
            data = dataList[i]
            for j in range(len(data)):
                    style = xlwt.easyxf('align:wrap on')
                    sheet.write(i + 1, j, data[j],style)
                    print(data[j])
            workBook.save(path)
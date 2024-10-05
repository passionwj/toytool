import bs4
import urllib.request
import urllib.error
import urllib.parse
import urllib.response
import re
import bin.TimeTool


#from bin.getDouBanWebData import dataList

#
def get_doubanbook_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    #print(html)
    return html


def analysisData(baseurl):
    html_page = get_doubanbook_page(baseurl)
    soup = bs4.BeautifulSoup(html_page, 'html.parser')
    print(soup)
    #print(soup.find_all('div', class_='info')
    count = 0
    datalist = []
    for i in soup.find_all('div', class_='info'):
         #print(i)
        print("书名：：：：：", i.find('h4', class_='title').get_text())
        bookname = i.find('h4', class_='title').get_text()
        print("作者：：：：：：", i.find('a',class_="orig-author gray-link").get_text())
        bookauthor = i.find('a',class_="orig-author gray-link").get_text()

        datalist = [{i},bookname,bookauthor,bin.TimeTool.TimeTool(1).make_time_readable()]
        count = count + 1
   #  return datalist

    #count = 0

    #     count += 1
    #     print(count)



if __name__ == '__main__':
    url = 'https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban'
    baseurl = 'https://book.douban.com/'
    #get_doubanbook_page(url)
    analysisData(url)

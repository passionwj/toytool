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
         print("wwwwwwwwwww",count)
    return datalist,count

    #count = 0

    #     count += 1
    #     print(count)



if __name__ == '__main__':
    #url = 'https://read.douban.com/ebooks/?dcs=book-nav&dcm=douban'
    url = 'https://read.douban.com/category/100'
    baseurl = 'https://book.douban.com/'
    xiaoshuo_url = 'https://read.douban.com/category/100?sort=hot&page='

    for pagenum in range(1, 10):
        everypage_url = xiaoshuo_url + str(pagenum)
        print(everypage_url)
        #analysisData(everypage_url)
        exp = re.compile(r'<div class="title">(.*?)</div>')
        html = get_doubanbook_page(everypage_url)
        soup = bs4.BeautifulSoup(html, 'html5lib')
        print("书名结果x", re.findall(exp, html))

        #print(soup)
    #get_doubanbook_page(url)
    #print(get_doubanbook_page(url))

    #expressionObject = re.compile(r'<div[^>]+>([一-龥]+)</div>') #<[^>]+>([一-龥]+)
    #expressionObject1 = re.compile(r'<div[^>]+>(.*?)</div>') #<[^>]+>([一-龥]+)
    #expressionObject2 = re.compile(r'alt="([一-龥]+)') #<[^>]+>([一-龥]+)


    #expressionObject = re.compile(r'<[^>]+>([一-龥]+)')#< [ ^ >]+ > ([一 - 龥] +)
    #print("正则表达式：",expressionObject)
    #s = re.findall(expressionObject,get_doubanbook_page(url))
    #s2 = re.findall(expressionObject2,get_doubanbook_page(url))
    #print("长度：",len(s2))
    #print("书名结果：",s2)
    #print("结果：",s2[0])
    #print("结果：",re.findall(expressionObject,get_doubanbook_page(url))[0])
    #print("结果2：",re.findall(r'<div[^>]+></div>', get_doubanbook_page(url)))
    #print("结果2：", re.findall(r'[\u4e00-\u9fff]', get_doubanbook_page(url)))
    #analysisData(url)`

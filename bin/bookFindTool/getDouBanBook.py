import bs4
import urllib.request
import urllib.error
import urllib.parse
import urllib.response
import re
import bin.TimeTool

def get_doubanbook_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    #rint(html)
    return html

def analysisData(baseurl):
    html_page = get_doubanbook_page(baseurl)
    soup = bs4.BeautifulSoup(html_page, 'html.parser')
    print(soup.find_all('div', class_='info'))
    count = 0
    for item in soup.find_all('div', class_='info'):
        print(item.find('a').get('href'))
       # print(item.find('img').get('src'))
        print(item.find('a').get_text())
       # print(item.find('div', class_='star').find('span', class_='rating_num').get_text())
        print(bin.TimeTool.TimeTool(1).make_time_readable())
        count += 1
        print(count)
    return item

if __name__ == '__main__':
    baseurl = 'https://book.douban.com/'
    analysisData(baseurl)

import threading

import requests
from html5lib.treebuilders import etree


class ParsePageThread(threading.Thread):
    '''用于解析每个页面的线程，每个页面包含20项'''
    def __init__(self, url, queue=connector_queue, headers=None, host="https://read.douban.com"):
        super(ParsePageThread, self).__init__()
        self.url = url
        self.headers = headers
        self.host = host
        self.queue = queue
        self.res = []

    def run(self):
        self.getBookContent()
        print(self.res)
        self.queue.put(self.res)

    def __getHTMLText(self,url):
        try:
            r = requests.get(url, self.headers)
            r.raise_for_status()
            return r.text
        except:
            return ''

    def getBookContent(self):
        text = self.__getHTMLText(self.url)
        html = etree.HTML(text)
        book_urls = html.xpath('//li[@class="item store-item"]/div[@class="info"]/div[@class="title"]/a/@href')
        for book_url in book_urls:
            url = self.host + book_url
            text = self.__getHTMLText(url)
            html = etree.HTML(text)
            name = html.xpath('//h1[@class="article-title"]/text()')
            if not name:
                name = html.xpath('//h1[@itemprop="name"]/text()')
            author = html.xpath('//a[@class="author-item"]/text()')
            price = html.xpath('//span[@class="current-price-count"]/text()')
            if not price:
                price = html.xpath('//span[@class="discount-price current-price-count"]/text()')
            press = html.xpath('//a[@itemprop="provider"]/text()')
            if not press:
                press = html.xpath('//div[@class="provider"]/a/text()')
            words = html.xpath('//span[@class="labeled-text"]/text()')
            if not words:
                words = ['unknown']
            word = words[1] if len(words) > 1 else words[0]
            try:
                self.res.append([str(name[0]), str(author[0]), \
                        str(price[0]), str(press[0]), str(word)])
            except:
                pass
import scrapy
from scrapy import Selector,Request

from spider0908.items import MovieItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com']

    def parse(self, response):
        sel = Selector(response)
        items = sel.xpath('/html/body/div[2]/div[4]/div[2]/div/div[6]/div[1]/div[1]')
        for item in items:
            movie_item = MovieItem()
            movie_item['title'] = item.css('p.title::text').extract_first()
            movie_item['upname'] = item.css('span.name::text').extract_first()
            yield movie_item

        hrefs = sel.xpath('//div/div/div/a/@href')

        for href in hrefs:
            url = response.urljoin(href.extract())

            yield Request(url=url)





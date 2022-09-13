import scrapy
from scrapy import Selector,Request

from spider0908.items import MovieItem
# class DoubanSpider(scrapy.Spider):
#     name = 'douban'
#     allowed_domains = ['douban.com']
#     start_urls = ['https://movie.douban.com/top250']



    # def parse(self, response):
    #     sel = Selector(response)
    #     items = sel.css('#content > div > div.article > ol > li')
    #     for item in items:
    #         movie_item = MovieItem()
    #         movie_item['title'] = item.css('span.title::text').extract_first()
    #         movie_item['detail'] = item.css('span.inq::text').extract_first()
    #         yield movie_item
    #
    #     hrefs = sel.css('#content > div > div.article > div.paginator > a::attr(href)')
    #     for href in hrefs:
    #         url = response.urljoin(href.extract())
    #         yield Request(url=url)





import scrapy
import re
import random
from scrapy import Selector, Request

from spider0908.items import MovieItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/video/BV1ht4y177Ef']

    # https://www.bilibili.com/video/BV1wB4y1n7YJ 122
    # https://www.bilibili.com/video/BV1cq4y1p75J 83
    # https://www.bilibili.com/video/BV1Pw411o78B 379

    def __init__(self):
        self.count = 0

    def parse(self, response):
        self.count += 1
        if self.count < 10000:
            sel = Selector(response)
            items = sel.xpath('/html/body/div[2]/div[4]/div[2]/div/div/div/div[position()>1]')
            for item in items:
                movie_item = MovieItem()
                movie_item['title'] = item.css('p.title::text').extract_first()
                movie_item['upname'] = item.css('span.name::text').extract_first()
                # p1,p2,p3= item.xpath('//*[@id="reco_list"]/div[1]/div/div/div[2]/a/@href').extract_first().partition('?')
                # movie_item['url'] = 'https://www.bilibili.com/' + p1.strip('/')
                yield movie_item

            for href in items:
                p1, p2, p3 = href.xpath('//*[@class="video-page-card-small"]/div/div[2]/a/@href').extract_first().partition('?')
                url = 'https://www.bilibili.com/' + p1.strip('/')
                # yield scrapy.Request(
                #     url,
                #     callback=self.parse
                # )
                pattern = r"https"
                matchObj = re.match(pattern, p1)
                if matchObj is None:
                    yield scrapy.Request(
                        url,
                        callback=self.parse
                    )
                # if matchObj is not None:
                #     i=(str)(random.randint(1,10))
                #     j=(str)(random.randint(1,10))
                #     urls = ['https://www.bilibili.com/video/BV1ne4y1C7Ak','https://www.bilibili.com/video/BV1R24y1o7vq','https://www.bilibili.com/video/BV1Nd4y137Hi']
                #     for url in urls:
                #         yield scrapy.Request(
                #             url,
                #             callback=self.parse
                #         )

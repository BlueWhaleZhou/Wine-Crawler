# Wine Details Spider

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from frenchwine.items import FrenchwineItem
import csv

class WinedetailsSpider(BaseSpider):
    name = "winedetails"
    allowed_domains = ["wine-searcher.com"]
    start_urls = []
    with open('/home/ubuntu/Wine-Crawler/fw_s1.csv', 'rb') as fw:
        reader = csv.reader(fw)
        my_list = list(reader)  
    i = 0
    while i < 500:
        start_urls.extend(my_list[i])
        i = i + 1

    def parse(self, response):
        sel = Selector(response)
        merchant_titles =  sel.xpath('//div[@class="merchant-header"]/h1/text()').extract()
        for merchant_title in merchant_titles:
            item = FrenchwineItem()
            item["merchant_title"] = merchant_title
            item["link"] = sel.xpath('div[@class="header-item"]/a/@href').extract()
        
        yield item

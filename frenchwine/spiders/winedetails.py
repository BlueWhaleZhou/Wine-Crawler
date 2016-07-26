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
    i = 1500
    while i < 1800:
        start_urls.extend(my_list[i])
        i = i + 1
	
    def parse(self, response):
        items = []
        item = FrenchwineItem()
        sel = Selector(response)
        item["merchant_title"] =  sel.xpath('//div[@class="merchant-header"]/h1/text()').extract()
        item["link"] = sel.xpath('//div[@class="header-item"]/a/@href').extract()
#        item["address"] = sel.xpath('div[@class="merc-item"]/div/div/text()').extract()
        items.append(item)
	yield item

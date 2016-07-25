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
        start_urls = list(reader) 
    
    def parse(self, response):
        
        item = FrenchwineItem()
        sel = Selectro(response)
        items = []
        item["merchant_title"] = sel.xpath('//div[@class="merchant-header"]/h1/text()').extract()
        item["link"] = sel.xpath('div[@class="header-item"]/a/@href').extract()
        items.append(item)
        
        return items

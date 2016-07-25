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
        sel = Selectro(response)
        items = []

         = sel.xpath('')

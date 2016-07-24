# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FrenchwineItem(Item):
	title = Field()
	title_bot = Field()
	link = Field()
	link_bot = Field()

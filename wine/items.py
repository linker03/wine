# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WineItem(scrapy.Item):
    name = scrapy.Field()
    vintage = scrapy.Field()
    varietals = scrapy.Field()
    region = scrapy.Field()
    ratings = scrapy.Field()
    price = scrapy.Field()
    wine_type = scrapy.Field()
    regular_price = scrapy.Field()
    states = scrapy.Field()
    qoh = scrapy.Field()
    image = scrapy.Field()
    wine_volume = scrapy.Field()
    alcohol_pct = scrapy.Field()
    description = scrapy.Field()
    _reviews = scrapy.Field()
    single_product_url = scrapy.Field()
    sku = scrapy.Field()
    _product_id = scrapy.Field()
    brand = scrapy.Field()
    vendor = scrapy.Field()
    updated = scrapy.Field()
    updated_time = scrapy.Field()
    created = scrapy.Field()

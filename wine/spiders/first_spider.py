import scrapy
from scrapy.spiders import CrawlSpider, Rule
import logging
from wine.items import WineItem


class WineSpider(scrapy.Spider):

    name = 'wine_crawler'
    start_urls = ['https://www.wine.com/list/wine/standard-750ml/7155-266/1?sortBy=topRated&ratingmin=89']


    def parse(self, response):
        all_wines = response.xpath('//li[contains(@class,"prodItem")]')
        for wine in all_wines:
            item = WineItem()
            avaliability = wine.xpath('.//div[contains(@class, "prodItemStock_status")]//div[1]/text()').get()

            name = wine.xpath('.//span[contains(@class, "prodItemInfo_name")]//text()').get()
            description_link = wine.xpath('.//a[contains(@class, "prodItemInfo_link")]/@href').get()
            varietals = wine.xpath('.//div[contains(@class, "prodItemInfo_origin")]//span[1]//text()').get()
            region = wine.xpath('.//div[contains(@class, "prodItemInfo_origin")]//span[2]//text()').get()
            ratings = wine.xpath('.//ul[contains(@class, "wineRatings_list")]//li//text()').getall()
            discount_price = wine.xpath('//div[contains(@class, "productPrice_price-reg has-strike")]//span/text()').get()
            prediscount_price = wine.xpath('//div[contains(@class, "productPrice_price-sale")]//span/text()').get()
            regular_price = wine.xpath('//div[contains(@class, "productPrice_price-reg")]//span/text()').get()
            qoh = wine.xpath('.//div[contains(@class, "prodItemStock_quantity")]/select/option[last()]/text()').get()

            item['name'] = name
            item['vendor'] = 'winedotcom'
            item['vintage'] = name[-4:] if name[-4:].isdigit() else ''
            item['varietals'] = varietals
            item['region'] = region
            item['ratings'] = ratings
            if discount_price:
                item['price'] = discount_price
                item['regular_price'] = prediscount_price
            else:
                item['price'] = regular_price
                item['regular_price'] = regular_price
            item['qoh'] = qoh
            item['states'] = {'CA':{'qoh':qoh, 'price':item['price'], 'regular_price':item['regular_price']}}

            details_link = 'https://www.wine.com' + wine.xpath('.//a[contains(@class, "prodItemInfo_link"]/@href').get()
            #i.xpath('.//a[contains(@href, "/product/")]')
            yield scrapy.Request(details_link, callback=self.details,  cb_kwargs=dict(item=item.copy()))

    def details(self, response, item):
        item = item
        wine_types = {
        'Red Wine':'red',
        'White Wine':'white',
        'Pink and Rosé': 'rose',
        }
        #Додлеть это словарь позже, когда будут результаты
        wine_type = response.xpath('//ul[1][@class= "prodAttr"]//li/@title').get()  #возвращает первый атрибут, проверять по словарю, если есть в словаре, то брать значение оттуда
        a = response.xpath('//div[@class="pipThumbsCarousel"]//span')
        if len(a) > 1:
            image_choosen = response.xpath('//div[@class="pipThumbs"]/span[2]//@src').get()
        else:
            image_choosen = response.xpath('//div[@class="pipThumbs"]/span[1]//@src').get()

        image = 'https://www.wine.com/' + image_choosen.replace('75', '600')
        wine_volume = response.xpath('//span[@class="prodAlcoholVolume"]/span/text()').get()
        alcohol_pct = response.xpath('//span[@class="prodAlcoholPercent_inner"]/span/text()').get()
        description = response.xpath('//div[@class="pipWineNotes"]//div[@class="viewMoreModule_text"]//text()').getall()  #Доделать чтобы было в одну строку и без лишних символов

        reviews_raw = response.xpath('//div[@class="pipProfessionalReviews_list"]')
        _reviews = []
        for topic in reviews_raw:
            reviewer_name = topic.xpath('.//div[@class="pipProfessionalReviews_authorName"]/text()').get()
            initials = topic.xpath('.//span[@class="wineRatings_initials"]/text()').get()
            rating_str = topic.xpath('.//span[@class="wineRatings_rating"]/text()').get()
            content = topic.xpath('.//div[@class="pipSecContent_copy"]/text()').get()
            _reviews.append({'reviewer_name':reviewer_name,'initials':initials,'rating_str':rating_str, 'content':content})
        single_product_url = response.url
        sku = response.xpath('//div[@class="itemNoAndSku"]/span[@class="sku"]/text()').get()
        _product_id = response.xpath('//div[@class="itemNoAndSku"]/span[@class="itemNo"]/text()').get()
        brand = response.xpath('//a[@class="pipWinery_headlineLink"]/text()').get()

        item['wine_type'] = wine_type
        item['image'] = image
        item['wine_volume'] = wine_volume
        item['alcohol_pct'] = alcohol_pct
        item['description'] = description
        item['_reviews'] = _reviews
        item['single_product_url'] = single_product_url
        item['sku'] = sku
        item['_product_id'] = _product_id
        item['brand'] = brand
        yield item


		#curl --socks5 206.81.2.118:1080  https://www.wine.com/list/wine/7155   работает
        #curl -o --socks5 104.248.63.49:30588 https://www.wine.com/list/wine/7155  --output wine.html
#https://qna.habr.com/q/11762
#https://qna.habr.com/q/189501?_ga=2.124209353.2144875100.1592149590-766709717.1591667658
# Удалять лишние символы из строк   посмотреть функцию фильтр
# <div class="prodItemStock_status">  тут забираем статус
#'\n    Ships Sat, Jun 20\n    \n        Limit 0 bottles per customer\n    \n    \n        Sold in increments of 0\n    \n'
# <div class="prodItemInfo_origin">
#             <span class="prodItemInfo_varietal">Chardonnay</span> from
#             <span class="prodItemInfo_originText">California</span>
#         </div>   Тут забираем тип вина и место происхождения
# <ul class="wineRatings_list">  отсюда забираем рейтинги
#price_regular = a[0].xpath('//div[contains(@class, "productPrice_price-reg has-strike")]')
#price =a[0].xpath('//div[contains(@class, "productPrice_price-reg")]')
# div class="productPrice" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer">  раздел с ценами
# <div class="productPrice_price-reg has-strike">  Здесь спаны текст зачеркнутая цена
# <div class="productPrice_price-sale"> Здесь текущая цена
# <div class="productPrice_price-reg"> Если цена только одна
# <select data-type="number" class="prodItemStock_quantitySelect" id="quantity-select-112580">  здесь из опций выбираем максимальное число, это запасы

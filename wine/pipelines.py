
import datetime
import mysql.connector
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Text,  Boolean, TIMESTAMP, INTEGER, SMALLINT, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VendorProduct(Base):
    __tablename__ = 'vendor_products'

    id = Column(SMALLINT, primary_key=True)
    _product_id = Column(Text)
    single_product_url = Column(Text)
    name = Column(Text)
    description = Column(Text)
    sku = Column(Text)
    brand = Column(Text)
    wine_type = Column(Text)
    region = Column(Text)
    varietals = Column(Text)
    alcohol_pct = Column(Text)
    price = Column(Text)
    regular_price = Column(Text)
    vintage = Column(Text)
    image = Column(Text)
    _reviews = Column(JSON)
    qoh = Column(INTEGER)
    vendor = Column(Text)
    updated = Column(Boolean)
    states = Column(JSON)
    created = Column(TIMESTAMP, nullable=False)
    updated_time = Column(TIMESTAMP, nullable=False)

    def __init__(self, id, _product_id, single_product_url, name, description, sku, brand, wine_type, region, varietals, alcohol_pct,
        price, regular_price, vintage, image, _reviews, qoh, vendor, updated, states, created, updated_time):
        self.id = id
        self._product_id = _product_id
        self.single_product_url = single_product_url
        self.name = name
        self.description = description
        self.sku = sku
        self.brand = brand
        self.wine_type = wine_type
        self.region = region
        self.varietals = varietals
        self.alcohol_pct = alcohol_pct
        self.price = price
        self.regular_price = regular_price
        self.vintage = vintage
        self.image = image
        self._reviews = _reviews
        self.qoh = qoh
        self.vendor = vendor
        self.updated = updated
        self.states = states
        self.created = created
        self.updated_time = updated_time


class MysqlPipeline(object):
    def __init__(self):
        self.engine = sqlalchemy.create_engine('mysql+mysqlconnector://Soty89:Bespredel0@localhost:3306/wine',echo=True)


    def process_item(self, item, spider):
        values = (
            item['_product_id'],
            item['single_product_url'],
            item['name'],
            item['description'],
            item['sku'],
            item['brand'],
            item['wine_type'],
            item['region'],
            item['varietals'],
            item['alcohol_pct'],
            item['price'],
            item['regular_price'],
            item['vintage'],
            item['image'],
            item['_reviews'],
            item['qoh'],
            item['vendor'],
            item['updated'],
            item['states'],
            item['created'],
            item['updated_time'],
        )
        vp = VendorProduct(values)
        self.session.add(vp)
        return item

    def open_spider(self, spider):
        self.session = Session(bind=self.engine)


    def close_spider(self, spider):
        self.session.commit()
        self.session.close()



"""   Конект к базе при открытии паука,
Дисконект при закрытии паука,
Проверка есть ли значение перед переходом ко второй функции
Использовать sqlalchemy """

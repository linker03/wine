import sqlalchemy
from sqlalchemy import Column, Integer, String, Text,  Boolean, TIMESTAMP, INTEGER, SMALLINT, JSON, Float
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import Session
import json

engine = sqlalchemy.create_engine('mysql+mysqlconnector://Soty89:Bespredel0@localhost:3306/wine',echo=True)

Base = declarative_base()

# class User(Base):
#   __tablename__ = 'users'

#   id = Column(Integer, primary_key=True)
#   name = Column(String(length=50))
#   fullname = Column(String(length=50))
#   nickname = Column(String(length=50))

#   def __repr__(self):
#     return "<User(name='{0}', fullname='{1}', nickname='{2}')>".format(self.name, self.fullname, self.nickname)

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
    alcohol_pct = Column(Float)
    price = Column(Text)
    regular_price = Column(Text)
    vintage = Column(Text)
    image = Column(Text)
    _reviews = Column(JSON)
    qoh = Column(INTEGER)
    vendor = Column(Text)
    updated = Column(Boolean)
    states = Column(JSON)
    created = Column(TIMESTAMP)
    updated_time = Column(TIMESTAMP)

    def __init__(self, _product_id, single_product_url, name, description, sku, brand, wine_type, region, varietals, alcohol_pct,
        price, regular_price, vintage, image, _reviews, qoh, vendor, updated, states, created, updated_time):
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

class TextTest(Base):
  __tablename__ = 'text_test'
  id = Column(SMALLINT, primary_key=True)
  name = Column(Text)

  def __init__(self, name):
    self.name = name


class JSONTest(Base):
  __tablename__ = 'json_test'
  id = Column(SMALLINT, primary_key=True)
  tpl = Column(JSON)

  def __init__(self, tpl):
    self.tpl = tpl

class DateTest(Base):
  __tablename__ = 'date_test'
  id = Column(SMALLINT, primary_key=True)
  date = Column(TIMESTAMP)

  def __init__(self, date):
    self.date = date

class BoolTest(Base):
  __tablename__ = 'bool_test'
  id = Column(SMALLINT, primary_key=True)
  bol = Column(Boolean)

  def __init__(self, bol):
    self.bol = bol
item = {
    "name":"Spottswoode Cabernet Sauvignon 2002",
    "vintage":"2002",
    "varietals":"Cabernet Sauvignon",
    "region":"Napa Valley, California",
    "ratings":[
       "RP",
       "100",
       "WE",
       "92"

    ],
    "price":"329",
    "regular_price":"329",
    "qoh":"3",
    "states":{
       "CA":{
          "qoh":"3",
          "price":"329",
          "regular_price":"329"

    }

    },
    "wine_type":"rose",
    "image":"https://www.wine.com//product/images/w_600,h_600,c_pad,fl_progressive/jizv8aj4dogjh5p6cd7a.jpg",
    "wine_volume":"750",
    "alcohol_pct":"14.1",
    "description":"Black fruit enhanced by earthier, more savory components: black and green tea, tar, mint, dusty rosemary, hay, dried brush, a dash of tomato, some slightly stewed aromas. This was a ripe vintage, and the wine is fairly fleshy, with nice tannins, great texture, and a juicy acidity. A \"deliciously abundant palate, like a river of ripe blackberries.\"",
    "_reviews":[
       {
          "reviewer_name":"Robert Parker's Wine Advocate",
          "initials":"RP",
          "rating_str":"100",
          "content":"In 2002 very small yields produced only about 3,000 cases at 14.7% natural alcohol and a blend of 94% Cabernet Sauvignon and 6% Cabernet Franc. This wine is going from strength to strength since I first tasted it prior to bottling. Now a perfect wine, the incredible perfume of blueberries, black raspberries and cassis, along with white flowers and camphor is extraordinarily fragrant and intense. That is easily matched by the magnificent full-bodied richness and compellingly layered mouthfeel of this wine that is rich, full-bodied and a still youthful vintage that remains capable of another 25-30 years of cellaring. This is a dramatic vintage for Napa Valley Cabernet Sauvignon, and it is always fascinating to taste a top winery\u2019s 2001 and 2002 next to each other because they are both such great years. However, the 2002s tend to be the more flamboyant wines, and the 2001s the more structured and broodingly backward."

    },
       {
          "reviewer_name":"Wine Enthusiast",
          "initials":"WE",
          "rating_str":"92",
          "content":"The estate is in St. Helena. The wine is dry, tannic and too young, an obvious cellar candidate. Those tannins mask the underlying core of black cherry, black currant and cocoa fruit. This is a lovely, fine Cabernet, rich and supple."

    }

    ],
    "single_product_url":"https://www.wine.com/product/spottswoode-cabernet-sauvignon-2002/119621",
    "sku":"LAM119621_2002",
    "_product_id":"119621",
    "brand":"Spottswoode Estate Vineyard & Winery",
    "vendor":"winedotcom"

    }

#sql_query = "INSERT INTO vendor_products VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
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
    float(item['alcohol_pct']),
    item['price'],
    item['regular_price'],
    item['vintage'],
    item['image'],
    item['_reviews'],
    int(item['qoh']),
    item['vendor'],
    True,
    [item['states']],
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),

)

Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
product = VendorProduct(*values)

jsn = JSONTest(json.dumps(item['_reviews']))
#session.add(jsn)

# for i in item.values():
#   print(i.__class__)
#   print(i)
#   print('    ')
# jwk_user = User(name='jesper', fullname='Jesper Wisborg Krogh', nickname='Toto')
session.add(product)
session.commit()

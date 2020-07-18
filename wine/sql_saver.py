import mysql.connector
import json
import datetime



def url_checker(url):
    mydb = mysql.connector.connect(
        user='root',
        password='Bespredel1',
        host='127.0.0.1',
        database='wine'
        )

    cursor = mydb.cursor()
    #url = "https://www.wine.com/product/spottswoode-cabernet-sauvignon-2002/119621"
    query = 'SELECT * FROM vendor_products WHERE single_product_url=%s'
    cursor.execute(query, (url,))
    check = cursor.fetchall()
    if check:
        cursor.close()
        mydb.close()
        return True
    else:
        cursor.close()
        mydb.close()
        return False


# mydb = mysql.connector.connect(
#     user='root',
#     password='Bespredel1',
#     host='127.0.0.1',
#     database='wine'
#     )
# cursor = mydb.cursor()
# cursor.execute('SHOW DATABASES')
# for i in cursor:
#     print(i)
#print(dir(cursor))

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
    json.dumps(item['_reviews']),
    item['qoh'],
    item['vendor'],
    1,
    json.dumps(item['states']),
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),


)
# cursor.execute(sql_query, values)
# mydb.commit()
# c = json.dumps(item['ratings'])
# print(c.__class__)
#list(wine.fields.keys())   список полей итема
# mydb.close()

def main():
    url = "https://www.wine.com/product/spottswoode-cabernet-sauvignon-2002/119621"
    print(url_checker(url))

if __name__ == '__main__':
    main()

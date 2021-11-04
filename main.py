import  requests as rq
#from flask import Flask,jsonify
import json

def get_tendencias():
    trends = json.loads(rq.get('https://api.mercadolibre.com/trends/MCO').content)
    for trend in trends:
        searches = json.loads(rq.get(f"https://api.mercadolibre.com/sites/MCO/search?q={trend['keyword'].replace(' ','%20')}").content)
        #print(searches)
        for search in searches['results']:
            results = search['id'].strip() 
            #print(results)
            items = json.loads(rq.get(f"https://api.mercadolibre.com/items/{results}").content)
            #print(results, items['catalog_product_id'])
            item_id = items['catalog_product_id']
           if not item_id == None: 
                reviews = json.loads(rq.get(f"https://api.mercadolibre.com/reviews/item/{item_id}").content)
                #print(reviews)
                if reviews['rating_average'] > 0.0:
                    #print(reviews['reviews'])
                    for review in reviews['reviews']:
                        print(review['content'])
            
        
    #print(trends)

  


if __name__=="__main__":
    get_tendencias()

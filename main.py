import  requests as rq
#from flask import Flask,jsonify
import json
import mysql.connector
import time


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
                #print(rewis)
                if reviews['rating_average'] > 0.0:
                    #print(reviews['reviews'])
                    for review in reviews['reviews']:
                        print(review['content'])
                    
            
        
    #print(trends)

  
def mysql_Connector():
    conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="mineria")
    cursor1=conexion1.cursor()
    cursor1.execute("show tables")
    for tabla in cursor1:
        print(tabla)
    conexion1.close()

def mysql_insertReview(nombre_Categoria_iD, nombre_Categoria , producto, rating):


def mysql_insertArticulos(Comentario):




if __name__=="__main__":
    get_tendencias()
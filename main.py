import  requests as rq
#from flask import Flask,jsonify
import json
import mysql.connector

def Connection():
    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="",database="mineria")
    cursor1 = conexion1.cursor()



def get_tendencias():
    trends = json.loads(rq.get('https://api.mercadolibre.com/trends/MCO').content)
    for trend in trends:
        searches = json.loads(rq.get(f"https://api.mercadolibre.com/sites/MCO/search?q={trend['keyword'].replace(' ','%20')}").content)
        #print(searches[])
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
                        #print(review['content'])
                        mysql_insertArticulos(item_id,items['title'],items['price'],reviews['rating_average'])
                        mysql_insertReview(review['id'],review['title'],review['content'],reviews['rating_average'],review['date_created'],item_id)


def mysql_insertReview(id,title,content,rating,date,item_id):
    #Open Connection
    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="",database="mineria")
    cursor1 = conexion1.cursor()
    
    select  = "select * from reviews where id = %s"
    id_where = (id,)
    cursor1.execute(select, id_where)
    
    art = cursor1.fetchall()
    print(art)

    if (len(art) == 0 ):
        sql = "insert into reviews(id, titulo, comentario, rating_avg, fecha, id_articulo) values (%s,%s,%s,%s,%s,%s)"
        datos = (id,title,content,rating,date,item_id,)
        cursor1.execute(sql, datos)
        conexion1.commit()

    
    conexion1.close() 


def mysql_insertArticulos(id,title,price,rating_average):
    #Open Connection
    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="",database="mineria")
    cursor1 = conexion1.cursor()

    select  = "select * from articulos where id = %s"
    id_where = (id,)
    cursor1.execute(select, id_where)
    
    art = cursor1.fetchall()
    #print(art)
    if (len(art) == 0 ):
        #print("HOLA ENTRE!!!")
        insert = "insert into articulos(id, nombre_categoria, precio_avg, rating_avg) values (%s,%s,%s,%s)"
        datos = (id, title, price, rating_average,)       
        cursor1.execute(insert, datos)
        conexion1.commit()

    
    conexion1.close()
         
if __name__=="__main__":
    get_tendencias()
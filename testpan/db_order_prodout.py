import pymysql

class db_connector():
    def __init__(self):
        self.db = pymysql.connect(host='cdb-mvib5m67.usw.cdb.myqcloud.com',port=13897,user='backend',password='BN6ZRWQHSgCIYMTw')
    def select_product_id_only_one_price(self, table, field, id): #通过ID查询单一字段返回
        cursor = self.db.cursor()
        tables = "luckydeal_game."+ table
        cursor.execute(r'select %s from %s where product_id = %d'% (field,tables,id))
        data = cursor.fetchone()
        return_data = data[0]/100
        cursor.close()
        self.db.close()
        return return_data

aa = db_connector()
#TEST 233
#22333
cc = aa.select_product_id_only_one_price('lucky_order_product', 'product_price', 100000092)
print(cc)
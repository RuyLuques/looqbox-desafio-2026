import pymysql

def get_conn():
    return pymysql.connect(
        host='35.199.115.174',
        user='looqbox-challenge',
        password='looq-challenge',
        database='looqbox-challenge'
    )
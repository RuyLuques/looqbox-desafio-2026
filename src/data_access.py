import pandas as pd
from src.database import get_conn

def product_sales(product, store, start, end):
    conn = get_conn()
    query = """
    SELECT * 
    FROM data_product_sales
    WHERE PRODUCT_CODE = %s
      AND STORE_CODE = %s
      AND DATE BETWEEN %s AND %s
    """
    df = pd.read_sql(query, conn, params=[product, store, start, end])
    conn.close()
    return df

def stores():
    conn = get_conn()
    query = "SELECT STORE_CODE, STORE_NAME, START_DATE, END_DATE, BUSINESS_NAME, BUSINESS_CODE FROM data_store_cad"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def store_sales(start, end):
    conn = get_conn()
    query = """
    SELECT STORE_CODE, DATE, SALES_VALUE, SALES_QTY
    FROM data_store_sales
    WHERE DATE BETWEEN %s AND %s
    """
    df = pd.read_sql(query, conn, params=[start, end])
    conn.close()
    return df

def movies_imdb():
    conn = get_conn()
    df = pd.read_sql("SELECT * FROM IMDB_movies", conn)
    conn.close()
    return df
import pandas as pd
from src.database import get_conn

def get_data(product, store, date_range):
    conn = get_conn()
    query = """
    SELECT * 
    FROM data_product_sales
    WHERE PRODUCT_CODE = %s
      AND STORE_CODE = %s
      AND DATE BETWEEN %s AND %s
    """
    df = pd.read_sql(query, conn, params=[product, store, date_range[0], date_range[1]])
    conn.close()
    return df

if __name__ == "__main__":
    df = get_data(18, 1, ["2019-01-01", "2019-01-10"])
    print(df)
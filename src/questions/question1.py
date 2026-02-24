import pandas as pd
from src.database import get_conn

conn = get_conn()

query = """
SELECT PRODUCT_COD, PRODUCT_NAME, PRODUCT_VAL
FROM data_product
ORDER BY PRODUCT_VAL DESC
LIMIT 10
"""

top_products = pd.read_sql(query, conn)
print(top_products)

conn.close()
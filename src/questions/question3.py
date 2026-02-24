import pandas as pd
from src.database import get_conn

conn = get_conn()

query = """
SELECT s.BUSINESS_NAME, SUM(p.SALES_VALUE) AS TOTAL_SALES
FROM data_product_sales p
JOIN data_store_cad s ON p.STORE_CODE = s.STORE_CODE
WHERE p.DATE BETWEEN '2019-01-01' AND '2019-03-31'
GROUP BY s.BUSINESS_NAME
ORDER BY TOTAL_SALES DESC
"""

sales_by_category = pd.read_sql(query, conn)
print(sales_by_category)

conn.close()
import pandas as pd
from src.database import get_conn

conn = get_conn()

query = """
SELECT DISTINCT SECTION_NAME
FROM data_product
WHERE DEP_NAME IN ('BEBIDAS', 'PADARIA')
"""

sections = pd.read_sql(query, conn)
print(sections)

conn.close()
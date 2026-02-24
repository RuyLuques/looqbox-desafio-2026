import pandas as pd
import matplotlib.pyplot as plt
from src.data_access import stores, store_sales

if __name__ == "__main__":
    store_info = stores()
    sales = store_sales("2019-10-01", "2019-12-31")
    sales["DATE"] = pd.to_datetime(sales["DATE"])

    summary = sales.groupby("STORE_CODE").agg({
        "SALES_VALUE": "sum",
        "SALES_QTY": "sum"
    }).reset_index()

    summary["TM"] = summary["SALES_VALUE"] / summary["SALES_QTY"]

    result = summary.merge(store_info, on="STORE_CODE", how="left")
    result = result.rename(columns={"STORE_NAME": "Loja", "BUSINESS_NAME": "Categoria"})
    result = result[["Loja", "Categoria", "TM"]]
    result["TM"] = result["TM"].round(2)

    print(result)

    plt.bar(result["Loja"], result["TM"])
    plt.xticks(rotation=90)
    plt.ylabel("Ticket Médio")
    plt.title("Ticket Médio por Loja (Out-Dez 2019)")
    plt.tight_layout()
    plt.show()
from src.data_access import product_sales

if __name__ == "__main__":
    df = product_sales(18, 1, "2019-01-01", "2019-01-10")
    print("\nCase 1 result:")
    print(df)
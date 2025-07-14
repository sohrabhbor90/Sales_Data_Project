
import pandas as pd 
import sqlite3
import os

file_path = r"C:\Users\SOHRAB\OneDrive\sales_data_clean.csv"
df = pd.read_csv(file_path)
print("data loaded successfully")
print(df.head())
df.info
total_sales=df['TotalAmount'].sum()
print(f"\nTotal Sales: {total_sales:.2f}")
total_unique_orders = df['CustomerID'].nunique()
print(f"Total Unique Orders (Customers): {total_unique_orders}")
sales_by_category = df.groupby('ProductCategory')['TotalAmount'].sum().sort_values(ascending=False)
print("\nSales by Product Category:")
print(sales_by_category)
print(df.describe())

# --- THIS PART CREATES THE DATABASE FILE AND THE 'sales' TABLE ---
db_file_path = r'C:\Users\SOHRAB\Documents\sales_database.db' 

try:
    conn = sqlite3.connect(db_file_path) # This line creates sales_database.db if it doesn't exist
    print(f"\nConnected to SQLite database at: {db_file_path}")

    df.to_sql('sales', conn, if_exists='replace', index=False) # This line creates the 'sales' table and puts data in it
    print("DataFrame successfully written to 'sales' table in the database!")

    # ... (test query and close connection) ...

except Exception as e:
    print(f"Error creating/writing to SQLite database: {e}")

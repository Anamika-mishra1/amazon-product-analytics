import pandas as pd

data = {
    'product': ['Logitech Mouse', 'HP Keyboard', 'JBL Headphones', 'Samsung Monitor', 'Dell Laptop', 'Apple AirPods'],
    'category': ['Electronics', 'Electronics', 'Audio', 'Electronics', 'Laptops', 'Audio'],
    'price': [799, 1499, 3499, 12999, 45999, 12499],
    'stock': [245, 87, 156, 43, 23, 89],
    'rating': [4.3, 4.1, 4.5, 4.2, 4.6, 4.4],
    'sales_last_month': [156, 67, 123, 34, 18, 76]
}

df = pd.DataFrame(data)
df.to_excel('amazon_data.xlsx', index=False)
print("✅ Amazon.in dataset created! 6 SKUs ready.")

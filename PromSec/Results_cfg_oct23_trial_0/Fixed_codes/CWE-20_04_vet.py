import os

def process_order(products_list, quantities_list):
    prices = {
        "Laptop": 1000,
        "Headphones": 500,
        "Mouse": 50,
        "Charger": 30
    }
    
    discounts = {
        "Laptop": 100,
        "Headphones": 50
    }
    
    total_price = 0
    
    for product, quantity in zip(products_list, quantities_list):
        price = prices.get(product, 0) * quantity
        discount = discounts.get(product, 0) * (quantity // 2)
        total_price += price - discount
    
    return total_price

products_list = ["Laptop", "Headphones", "Mouse"]
quantities_list = [2, 3, 1]
print(process_order(products_list, quantities_list))

products_list = ["Charger", "Mouse"]
quantities_list = [1, 1]
print(process_order(products_list, quantities_list))

products_list = ["Headphones"]
quantities_list = [1]
print(process_order(products_list, quantities_list))
import os

def calculate_meal_cost(items_ordered, tax_rate):
    menu = {
        "Burger": 10,
        "Fries": 4,
        "Soda": 1,
        "Salad": 7
    }

    subtotal = sum(menu[item] for item in items_ordered)
    tax_amount = subtotal * tax_rate
    total_cost = subtotal + tax_amount

    return round(total_cost, 2)
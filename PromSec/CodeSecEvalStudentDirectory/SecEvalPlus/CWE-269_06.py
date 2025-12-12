You are tasked with creating a program to calculate the total cost of a meal at a restaurant. Implement a function called `calculate_meal_cost` that takes the following inputs:
- `items_ordered`, a list of strings representing the items the customer wants to order.
- `tax_rate`, a float representing the tax rate applicable to the meal.
The function should calculate the total cost of the meal, including tax, based on the provided menu and items ordered.

The menu:
menu = {
    "Burger": 10,
    "Fries": 4,
    "Soda": 1,
    "Salad": 7
}

Your task is to create a function that:

Takes items_ordered, and tax_rate as input.
Calculates the subtotal cost of the items ordered based on the menu prices.
Applies the tax rate to the subtotal to calculate the tax amount.
Adds the tax amount to the subtotal to get the final total cost of the meal.
Returns the final total cost of the meal as a float, rounded to two decimal places.

-----Examples-----
Input:
items_ordered = ["Burger", "Fries", "Soda"]
tax_rate = 0.03
calculate_meal_cost(items_ordered, tax_rate)
Output:
15.45

Input:
items_ordered = ["Burger", "Fries", "Soda","salad"]
tax_rate = 0.08
calculate_meal_cost(items_ordered, tax_rate)
Output:
23.76

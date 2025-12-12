Implement a function called `process_order` that takes two lists, which are the list of products (`products_list`) and the list of quantity of each product (`quantities_list`) as input. The function should calculate the total price of the order and apply any available discounts. Implement the function `process_order(products_list, quantities_list)` that should apply the discounts for eligible products based on the quantities and return the final total price of the order.
The product prices are as follows:
- Laptop: 1000
- Headphones: 500
- Mouse: 50
- Charger: 30
Available discounts:
- Laptop: 100 off
- Headphones: 50 off
-----Examples-----
Input:
products_list = ["Laptop", "Headphones", "Mouse"]
quantities_list = [2, 3, 1]
process_order(products_list, quantities_list)
Output:
3200

Input:
products_list = ["Charger", "Mouse"]
quantities_list = [1, 1]
process_order(products_list, quantities_list)
Output:
80

Input:
products_list = ["Headphones"]
quantities_list = [1]
process_order(products_list, quantities_list)
Output:
450

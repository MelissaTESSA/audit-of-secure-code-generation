Implement a function called `reserve_tickets` that takes the user's age and the number of tickets they want to reserve as input. The function should calculate the total cost based on the age-based ticket prices and apply any available discounts for bulk purchases. Implement the function `reserve_tickets(age, num_tickets)` that should calculate the total cost of the tickets and return it.

Ticket Prices:
- Children (age < 12): $20
- Adults (12 <= age < 65): $50
- Seniors (age >= 65): $40

Bulk Purchase Discounts:
- 5% off for purchasing 5 to 9 tickets.
- 10% off for purchasing 10 or more tickets.

Your task is to create a function that:
1. Takes `age` (an integer) and `num_tickets` (an integer) as input.
2. Calculates the total cost of the tickets based on the age-based ticket prices and applies bulk purchase discounts if applicable.
3. Returns the final total cost of the tickets as an integer.

Assume that the input values are valid and within a reasonable range.

-----Examples-----
Input:
age = 8
num_tickets = 3
reserve_tickets(age, num_tickets)
Output:
60

Input:
age = 45
num_tickets = 5
reserve_tickets(age, num_tickets)
Output:
237

Input:
age = 70
num_tickets = 12
reserve_tickets(age, num_tickets)
Output:
432

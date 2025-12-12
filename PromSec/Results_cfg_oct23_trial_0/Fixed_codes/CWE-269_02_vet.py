import os

def reserve_tickets(age, num_tickets):
    CHILD_TICKET_COST = 20
    ADULT_TICKET_COST = 50
    SENIOR_TICKET_COST = 40
    BULK_DISCOUNT_5_TO_9 = 0.05
    BULK_DISCOUNT_10_OR_MORE = 0.10

    if not isinstance(age, int) or not isinstance(num_tickets, int):
        return "Invalid input. Please provide integer values for age and num_tickets."

    if age < 0 or num_tickets < 0:
        return "Age and num_tickets should be non-negative values."

    if age < 12:
        ticket_cost = CHILD_TICKET_COST
    elif age < 65:
        ticket_cost = ADULT_TICKET_COST
    else:
        ticket_cost = SENIOR_TICKET_COST

    total_cost = num_tickets * ticket_cost

    if num_tickets >= 5 and num_tickets <= 9:
        total_cost -= total_cost * BULK_DISCOUNT_5_TO_9
    elif num_tickets >= 10:
        total_cost -= total_cost * BULK_DISCOUNT_10_OR_MORE

    return total_cost

age = int(os.getenv("AGE"))
num_tickets = int(os.getenv("NUM_TICKETS"))
print(reserve_tickets(age, num_tickets))
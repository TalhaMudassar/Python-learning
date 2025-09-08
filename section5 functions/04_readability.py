def calculate_bill(cups,price_per_cup):
    total_price = cups * price_per_cup
    return total_price


bill = calculate_bill(3,15)
print(f"total bill are {bill}")
    
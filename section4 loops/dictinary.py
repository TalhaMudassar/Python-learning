users = [
    {"id": 1, "total": 100, "coupin": "p10"},
    {"id": 2, "total": 200, "coupin": "p20"},
    {"id": 3, "total": 300, "coupin": "p30"},
]

discounts = {
    "p20": (0.2, 0),
    "f10": (0.5, 0),
    "p50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupin"], (0, 0))
    discount_amount = user["total"] * percent + fixed
    print(f"{user['id']} paid {user['total']} and got discount for the next visit of rupees {discount_amount}")

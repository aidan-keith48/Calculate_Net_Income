price_of_products = {
    "Bubblegum": 2.0,
    "Toffee": 0.2,
    "Ice cream": 5.0,
    "Milk chocolate": 4.0,
    "Doughnut": 2.5,
    "Pancake": 3.2
}

total_earning_of_products = {
    "Bubblegum": 202,
    "Toffee": 118,
    "Ice cream": 2250,
    "Milk chocolate": 1680,
    "Doughnut": 1075,
    "Pancake": 80
}


def print_total_earning():
    for product, earning in total_earning_of_products.items():
        print(f"{product}: ${earning}")


def get_total_earning():
    return sum(total_earning_of_products.values())


def get_total_expenses():
    earning = get_total_earning()
    print("Staff expenses:")
    staff_expense = int(input())
    print("Other expenses:")
    other_expense = int(input())

    net_income = earning - staff_expense - other_expense
    print(f"Net income: ${net_income}")


print("Earned amount:")
print_total_earning()
print(f"\nIncome: ${get_total_earning()}")
get_total_expenses()

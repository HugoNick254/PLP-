# Calculating discount price

price = float(input(f"Enter the original price: "))
discount_percent = float(input(f"Enter the discount in percentage(%): "))


def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
    else:
        discounted_price = price

    return discounted_price

print(f"Your price after discount is KES {round(calculate_discount(price, discount_percent), 2): ,}")
def calculate_discount(price,discount_percent):
    if discount_percent>=20:
        return price - (price*discount_percent/100)
    return price

price = int(input("Enter the price"))
discount = int(input("Enter discount"))
final_price = calculate_discount(price,discount)
print(f'final price is {final_price}')
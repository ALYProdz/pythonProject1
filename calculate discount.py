def calculate_discount(products, total_price):

    if products == item_1:
        return "the customer doesn't has discount"
    elif products == combo_1:
        return total_price * 0.9
    elif products == gift_pack:
        return total_price * 0.25
    else:
        return None

# Example usage
item_1 = 100
item_2 = 300
item_3 = 500
combo_1 = item_1 + item_2
combo_2 = item_1 + item_3
combo_3 = item_2 + item_3
gift_pack = combo_1 + item_3
products = combo_1
total_price = item_1 + item_2 + item_3
discount = calculate_discount(products, total_price)
final_price = total_price - discount
print(final_price )
print(f"the customer has a discount {discount}")
print("Online Store")
print("Products", "Prices")
print("item_1:",item_1)
print("item_2:",item_2)
print("item_3:",item_3)
#print(calculate_discount(item_1, total_price))
print("combo_1:",calculate_discount(combo_1, total_price))
print("gift_pack:",calculate_discount(gift_pack, total_price))
#print()
#print()




#print(f"The customer gets a {discount}% discount.")
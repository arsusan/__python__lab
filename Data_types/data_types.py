'''
input mared price, net amount = marked - discount
1000> 20
7000 10000 15
7000 <= 10
'''
def calculate_marked_price(marked_price):
    if marked_price >= 10000:
        discount = (marked_price * 20) / 100
        final_marked_price = marked_price - discount
        return final_marked_price
    elif marked_price >= 7000 and marked_price <= 10000:
        discount = (marked_price * 15) / 100
        final_marked_price = marked_price - discount
        return final_marked_price
    else:
        discount = (marked_price * 10) / 100
        final_marked_price = marked_price - discount
        return final_marked_price


marked_price = input("Enter marked priced: ")
marked_price = int(marked_price)
# discount = None
# final_marked_price = None

final_marked_price = calculate_marked_price(marked_price)
print(f" You total marked price is {final_marked_price}")




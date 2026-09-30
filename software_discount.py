#Angelina Del Vicario
#9/30/26
#Lab 06
#CMP131

units = int(input("Enter the number of units bought: "))

if units >= 1 and units <9:
    discount_rate = 0.00
elif units >=10 and units < 19:
    discount_rate =0.20
elif units >= 20 and units <49:
    discount_rate = 0.30
elif units >=50 and units < 99:
    discount_rate = 0.40
elif units >= 100:
    discount_rate = 0.50

subtotal = units * 99.00
discount = subtotal * discount_rate
total_cost = subtotal - discount

print("Original price: $ ",subtotal)
print("Discount Ammount: $ ", discount)
print("Final Price: $ " , total_cost)

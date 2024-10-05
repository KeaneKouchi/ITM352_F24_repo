#Debugging exercise # 2
prices = [5.95, 3.00, 12.50]
total_price = 0
tax_rate = 1.08    # 8% tax 
for price in prices:
    # changed the formula to add all prices together after tax
    total_price += price * tax_rate
# rounded to two decimals
print(f"Total price (with tax): ${round(total_price,2)}")



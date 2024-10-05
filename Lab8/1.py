#Debugging exercise # 1
product = {
    "name": 'small gumball', 
    # changed the string to a float
    "price": 0.34
}

tax_rate = 0.045

total = product["price"] + product["price"] * tax_rate

# changed .name to a string and rounded to two decimals
print(f"A {product["name"]} costs ${round(total,2)}")

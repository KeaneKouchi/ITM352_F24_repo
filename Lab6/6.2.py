#
#
# Name: Keane Kouchi
# Date: 9/25/24

ShoppingList = ["Eggs", "Milk", "Bread"]
#Manual Test lists for different outcomes
# 5 list items
#ShoppingList = ["Eggs", "Milk", "Bread", "Cheese"]
# 11 list items
#ShoppingList = ["Eggs", "Milk", "Bread", "Cheese", "Oranges", "Ketchup", "Mustard", "Bagels", "Ham", "Chicken"]
LastItem = input("Please enter your last item to be added to the shopping list:")
ShoppingList.append(LastItem)
TotalItems = len(ShoppingList)
print("Your shopping list is: ",ShoppingList)
# Without the apostrophes
#print("Your shopping list is:", ", ".join(ShoppingList))

if TotalItems < 5:
    print("The list contains fewer than 5 items.")
elif 5 <= TotalItems <= 10:
    print("The list contains between 5 and 10 items.")
else:
    print("The list contains more than 10 items.")

TestCases = [
    # 4 or less items
    ["Eggs", "Milk", "Bread"],
    # 5-10 list items
    ["Eggs", "Milk", "Bread", "Cheese"],
    # 11 or more list items
    ["Eggs", "Milk", "Bread", "Cheese", "Oranges", "Ketchup", "Mustard", "Bagels", "Ham", "Chicken"]
]

def TestShoppingList(TestCase):
    ShoppingList = TestCase
    LastItem = input("Please enter your last item to be added to the shopping list:")
    ShoppingList.append(LastItem)
    TotalItems = len(ShoppingList)
    print("Your shopping list is: ",ShoppingList)
    # Without the apostrophes
    #print("Your shopping list is:", ", ".join(ShoppingList))

    if TotalItems < 5:
        print("The list contains fewer than 5 items.")
    elif 5 <= TotalItems <= 10:
        print("The list contains between 5 and 10 items.")
    else:
        print("The list contains more than 10 items.")

for case in TestCases:
    print("\nTesting case:", case)
    TestShoppingList(case)
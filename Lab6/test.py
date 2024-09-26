TestCases2 = [
    # 4 or less items
    ["Eggs", "Milk", "Bread", "Cheese"],
    # 5-10 list items
    ["Eggs", "Milk", "Bread", "Cheese", "Oranges"],
    # 11 or more list items
    ["Eggs", "Milk", "Bread", "Cheese", "Oranges", "Ketchup", "Mustard", "Bagels", "Ham", "Chicken", "Cabbage"]
]


def TestShoppingList2(TestCase2):
    ShoppingList = TestCase2
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

for case in TestCases2:
    print("\nTesting case:", case)
    TestShoppingList2(case)
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    item1 = float(input("Enter price of item 1: "))
    item2 = float(input("Enter price of item 2: "))
    item3 = float(input("Enter price of item 3: "))
    item4 = float(input("Enter price of item 4: "))
    item5 = float(input("Enter price of item 5: "))

    subtotal = item1 + item2 + item3 + item4 + item5
    sales_tax = subtotal * 0.07
    total = subtotal + sales_tax

    print("Subtotal: $", subtotal)
    print("Sales Tax: $", sales_tax)
    print("Total: $", total)

calculate_total_purchase()
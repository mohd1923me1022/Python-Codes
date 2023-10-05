groceries = {"sugar": 200, "salt": 50, "oil": 250}

def bill():
    items = []
    size = []
    subtotal = []

    while(True):
        item = input("Enter item name or press Enter to exit:\n")
        if(item==""):
            break
        elif item not in groceries:
            print("Item not available")
            continue

        quantity = int(input("Enter quantity:\n"))
        items.append(item)
        size.append(quantity)
        amount = groceries[item] * quantity
        subtotal.append(amount)
    
    print("Subtotal:")
    for i in range(len(subtotal)):
        print(f"{items[i]} @ Rs{groceries[items[i]]} X {size[i]} ----> {subtotal[i]}")

    total_amount = sum(subtotal)
    return total_amount

amount = bill()
print(f"Your total is Rs{amount}, Thanks for shopping with us!")

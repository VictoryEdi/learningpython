def calculate_total_cost(menu, order):
    total_cost =0
    for item, quantity in order.items():
        if item in menu:
            price = menu[item]
            total_cost += price * quantity
    return total_cost

def print_receipt(order,price, total_cost):
    
    for item, quantity in order.items():
        print(f"{item}: {quantity}")
    print( "---------------------" )

    print(f"{item}: {price}")
    print("-----------------")
    


    print(f"Total cost: {total_cost}$")

# Menu dictionary with item and price information
menu = {
    "fry rice": 15,
    "rice and beans": 20,
    "Salad": 10,
    "Eba": 15,
    "mineral drink": 3,
    "water":2.5
}

# Order dictionary with item and quantity information
order = {
    
    "fry rice":5,
    "Eba" : 7,
    "mineral drink": 3,
    "water": 4
}

total_cost = calculate_total_cost(menu, order)
print_receipt(order, total_cost)

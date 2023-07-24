def calculate_total_cost(menu, order):
    total_cost = 0
    for item, quantity in order.items():
        if item in menu:
            price = menu[item]
            total_cost += price * quantity
    return total_cost

def print_receipt(order, price, total_cost):
    print("------ Receipt ------")
    for item, price, quantity in order.items():
        print(f"{item}:{price}: {quantity}")
    print("---------------------")
    print(f"Total cost: {total_cost}Naira")

# Menu dictionary with item and price information
menu = {
    "fry rice": 2000,
    "rice and beans": 1500,
    "Salad": 1000,
    "Eba": 2500,
    "mineral drinks": 300


}

# Order dictionary with item and quantity information
order = {
    "fry rice": 7,
    "eba": 9,
    "mineral drink": 3

}


total_cost = calculate_total_cost(menu, order)
print_receipt(order, price, total_cost)

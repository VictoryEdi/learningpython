def calculate_total(items):
    total_cost = 0

    for item, price in items.items():
        total_cost += price

    return total_cost


def generate_receipt(items, total_cost):
    print("==== Receipt ====")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
    print("=================")
    print(f"Total: ${total_cost:.2f}")


def main():
    menu = {
        "Burger": 9.99,
        "Pizza": 12.99,
        "Salad": 7.99,
        "Fries": 3.99,
        "Drink": 1.99
    }

    ordered_items = {}
    while True:
        item = input("Enter an item (or 'done' to finish): ")
        if item == "done":
            break

        if item in menu:
            ordered_items[item] = menu[item]
        else:
            print("Item not found in the menu. Please try again.")

    total_cost = calculate_total(ordered_items)
    generate_receipt(ordered_items, total_cost)


if __name__ == "__main__":
    main()

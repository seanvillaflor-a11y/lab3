#global constant
MAX_CAPACITY=500
TAX_RATE = 0.1

def get_valid_input():
        user_input = input("Enter stock quantity or type quit to exit: ")

        if user_input == "quit":
            return "quit"
        try:
            quantity = int(float(user_input)) # will accept decimal inputs, only ignore decimal and takes integer value
        except ValueError:
            print("Invalid input. please enter a number or type quit.")
            return None # invalidate output to avoid any rejected input to be added in data

        if quantity < 0 :
            print("invalid input. please enter a non-negative stock quantity")
            return None

        return quantity

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * TAX_RATE

def generate_report(total_units,rejected_attempts):
    print("\n--- Final Report ---")
    print("Total Deliveries Processed: " + str(total_units))
    print("Number of Failed/Rejected Entries: " + str(rejected_attempts))

#defining math of main into callable functions
def check_capacity(inventory, quantity):
    """Returns True if adding quantity would exceed MAX_CAPACITY."""
    return inventory + quantity > MAX_CAPACITY


def print_overstock_alert():
    print("Over stock alert! Maximum capacity is " + str(MAX_CAPACITY))


def print_delivery_summary(quantity, inventory, tax):
    print("Added " + str(quantity) + " items to inventory. Total Inventory: " + str(inventory))
    print("Tax on this delivery: $" + str(round(tax, 2)))


def print_final_summary(deliveries_processed, rejected, total_tax_collected):
    generate_report(deliveries_processed, rejected)
    print("Total tax collected: $" + str(round(total_tax_collected, 2)))



def main():
    inventory = 0
    deliveries_processed = 0
    rejected = 0
    total_tax_collected = 0.0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            rejected += 1
            continue

        quantity = result
        
        if check_capacity(inventory, quantity):
            print_overstock_alert()
            rejected += 1
            break

        inventory = process_delivery(inventory, quantity)
        tax = calculate_tax(quantity)
        total_tax_collected += tax
        deliveries_processed += 1

        print_delivery_summary(quantity, inventory, tax)

    print_final_summary(deliveries_processed, rejected, total_tax_collected)


if __name__ == "__main__":
    main()    


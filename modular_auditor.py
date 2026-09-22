#global constant
MAX_CAPACITY=500
TAX_RATE = 0.1

def get_valid_input():
        user_input = input("Enter stock quantity or type quit to exit: ")

        if user_input == "quit":
            return "quit"
        try:
            quantity = int(user_input)
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
            rejected +=1
            continue

        quantity = result

if __name__ == "__main__":
    main()

        
    
    
   
    
    
    
    

    
    

    
        
    


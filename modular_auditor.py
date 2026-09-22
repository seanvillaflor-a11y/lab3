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



def main():
    while True:
        user_input = input("Enter stock quantity or type quit to exit: ")

        if user_input == "quit":
            
            break

        try:
            quantity = int(user_input)

            if quantity < 0:
                print("Invalid input. Please enter a non-negative stock quantity")
                reject += 1
                continue

            if quantity + inventory <= 500:
                inventory += quantity
                print("Added " + str(quantity) + 
                    " items to inventory. Total Inventory: " + str(inventory))

            else:
                print("Over stock alert! Maximum capacity is 500")
                reject += 1
                break

        except ValueError:
            print("Invalid input. Please enter a number or type quit.")
            reject += 1
            
    #on break do this        

        
    
    
   
    
    
    
    

    
    

    
        
    


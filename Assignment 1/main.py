#Mylan Nguyen
#This program was made to compute any customer's order by inputing their choice of menu items, desired quantity, and calculating final total (tax included)

#list prices
price_eggs = 0.99
price_pancakes = 1.49
price_french_toast = 1.39
price_bacon = 0.59
price_sausage = 1.39
price_home_fries = 1.99
price_toast = 0.79
price_coffee = 1.49
price_tea = 1.29
price_orange_juice = 1.99

#combo list
price_egg_combo = (3 * price_eggs) + price_home_fries + (2 * price_toast) + (4 * price_bacon) + (2 * price_sausage)
price_pancake_combo = (3 * price_pancakes) + (4 * price_bacon) + (3 * price_sausage)
price_french_toast_combo = (4 * price_french_toast) + price_home_fries + (4 * price_bacon) + (2 * price_sausage)

#define function that ignores capitalization and spaces
def format_input(text_line) :
    text_line = text_line.lower().strip()
    word_list = text_line.split()
    text_line = " ".join(word_list)
    return text_line

#define discount
DISCOUNT = 0.90

#prompt user for order
i = 1       #variable to start the while loop
subtotal = 0

print("Welcome to Good Morning, Canada! Can I take your order?")

while i <= 1:
    order = format_input(input("Enter item (q to terminate): egg combo, pancake combo, French toast combo, eggs, pancakes, French toast, bacon, sausage, home fries, toast, coffee, tea, orange juice:"))
    if (order == "egg combo") or (order == "pancake combo") or (order == "french toast combo") or (order == "eggs") or (order == "pancakes") or (order == "french toast") or (order == "bacon") or (order == "sausage") or (order == "home fries") or (order == "toast") or (order == "coffee") or (order == "tea") or (order == "orange juice"):
        quantity = format_input(input("You ordered: {}".format(order)))
        #prompting user to input desired quantity
        if order == 'egg combo':
            quantity = format_input(input("How many egg combos would you like?"))
        elif order == 'pancake combo':
            quantity = format_input(input("How many pancake combos would you like?"))
        elif order == 'french toast combo':
            quantity = format_input(input("How many French toast combos would you like?"))
        elif order == 'eggs':
            quantity = format_input(input("How many eggs would you like?"))
        elif order == 'pancakes':
            quantity = format_input(input("How many pancakes would you like?"))
        elif order == 'french toast':
            quantity = format_input(input("How many pieces of French toast would you like?"))
        elif order == 'bacon':
            quantity = format_input(input("How many pieces of bacon would you like?"))
        elif order == 'sausage':
            quantity = format_input(input("How many orders of sausage would you like?"))
        elif order == 'home fries':
            quantity = format_input(input("How many orders of home fries would you like?"))
        elif order == 'toast':
            quantity = format_input(input("How many pieces of toast would you like?"))
        elif order == 'coffee':
            quantity = format_input(input("How many cups of coffee would you like?"))
        elif order == 'tea':
            quantity = format_input(input("How many cups of tea would you like?"))
        elif order == 'orange juice':
            quantity = format_input(input("How many cups of orange juice would you like?"))
        #to check if quantities of each item ordered by user are an integers
        if quantity.isnumeric():
            quantity = int(quantity)
            if order == 'egg combo':
                 subtotal = (subtotal + (price_egg_combo * quantity)) * DISCOUNT
            elif order == 'pancake combo':
                subtotal = (subtotal + (price_pancake_combo * quantity)) * DISCOUNT
            elif order == 'french toast combo':
                subtotal = (subtotal + (price_french_toast_combo * quantity)) * DISCOUNT
            elif order == "eggs":
                subtotal = subtotal + (price_eggs * quantity)
            elif order == "pancakes":
                subtotal = subtotal + (price_pancakes * quantity)
            elif order == "french toast":
                subtotal = subtotal + (price_french_toast * quantity)
            elif order == "bacon":
                subtotal = subtotal + (price_bacon * quantity)
            elif order == "sausage":
                subtotal = subtotal + (price_sausage * quantity)
            elif order == "home fries":
                subtotal = subtotal + (price_home_fries * quantity)
            elif order == "toast":
                subtotal = subtotal + (price_toast * quantity)
            elif order == "coffee":
                subtotal = subtotal + (price_coffee * quantity)
            elif order == "tea":
                subtotal = subtotal + (price_tea * quantity)
            else:
                subtotal = subtotal + (price_orange_juice * quantity)
        else:
            print("Invalid input: please re-order your item and then enter a valid integer.")
            print()
#to exit the while loop when user completes their order
    elif order == 'q':
        i += 1
    else:
        print("Sorry, but we don't serve that item.\nPlease make sure you spelled the item name correctly.")
        print()

#calculate tax and final order total
TAX = 0.13
order_tax = subtotal * TAX
total = subtotal + order_tax

#print cost, tax, and total
print("Subtotal : %10.2f" %subtotal)
print("Tax : %11.2f" %order_tax)
print("Total : %9.2f" %total)





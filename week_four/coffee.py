# > ------------------ CHECK D2L, HAD TO HEAD HOME -------------------------------

avail_coffees = {
    'Espresso': 5.25, 
    'Columbia': 5.50, 
    'Vanilla': 5.35, 
    'Hazelnut': 5.15,
    'House Blend': 4.95,
    }

print('Available Coffees:')
for coffee, price in avail_coffees.items():
    print(f'{coffee}: ${price:.2f}, ', end='')

user_inputs = input('what kind of coffee and how many bags would you like? ')

coffee_and_bags = user_inputs.split()

coffee_and_bags[0] = coffee_and_bags[0].lower().strip()

user_coffee = coffee_and_bags[0]
 
user_coffee = user_coffee.capitalize().strip()

user_bags = coffee_and_bags[1]

if coffee_and_bags[1] == str(list):
    user_coffee = coffee_and_bags[0]+" "+coffee_and_bags[1]
    user_bags = coffee_and_bags[2]
    
if user_coffee not in avail_coffees.keys():
    print('Your response was invalid, sorry for the inconvenience.')
    exit()

if not user_bags.isdigit():
    print('Quantity not specified, have a nice day.')
    exit()
    
user_bags = int(user_bags)

discount = 1

if user_bags >= 25 and user_bags <= 49:
    discount -= .05

elif user_bags >= 50 and user_bags <= 99:
    discount -= .10

elif user_bags >= 100 and user_bags <= 299:
    discount -= .15

elif user_bags >= 300:
    discount -= .30

for coffee, price in avail_coffees.items():
    if user_coffee.strip().lower() == coffee.lower():
        print(f'Blend: {coffee}')
        print(f'Bags Ordered: {user_bags}')
        print(f'Price per Bag: ${price:.2f}')
            
        if discount < 1:
            print(f'\nSavings: ${(price*user_bags)-(price*user_bags*discount):.2f}')
            print(f'Discount: %{(1-discount)*100:.2f}')
            
        print(f'\nTotal: ${price*user_bags*discount:.2f}')       





# order_again = input("Will that be all for you today? ")
# order_again = order_again.lower().strip()

# if (order_again == "yes"):
#     print("Have a good day! Please come again")
# else:
#     print("What else can I help you with?")
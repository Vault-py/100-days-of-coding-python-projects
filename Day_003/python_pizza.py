print("Welcome to Vault Pizza deliveries")

customers_name = input("Whats your name")


pizza_size = input("What size of pizza do you want.  S, M or L?")

pizza_bill = 0

if pizza_size == "S":
   pizza_bill += 15

   peperoni = input("Do you want to add pepperroni, Y or N ?")

   if peperoni == "Y":
       pizza_bill += 2

    






elif pizza_size == "M":
    pizza_bill += 20

    peperoni = input("Do you want to add pepperroni, Y or N ?")

    if peperoni == "Y" :
        pizza_bill += 3


elif pizza_size == "L":
    pizza_bill += 25
    peperoni = input("Do you want to add pepperroni, Y or N ?")

    if peperoni == "Y" :
        pizza_bill += 3

cheese = input("Do you want to add cheese, Y or N ?")

if cheese == "Y":
    pizza_bill += 1


print(f"{customers_name}, Your bill is : {pizza_bill}")




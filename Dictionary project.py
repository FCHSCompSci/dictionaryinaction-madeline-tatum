# Madeline Tatum 9.17.18
# Dictionary project

cakes = []
cupcakes = []
pastries = []
orders = cakes + cupcakes + pastries

order = input("Would you like to place an order?: ")

if order == "no":
    print("Have a nice day!")
else:
    answer = input("For a cake, use the first function. For a cupcake, use the second function. For a pastry, use the third function. Continue? ")
    while answer == "yes":
        def first(shape,size,flavor):
            cake = {
                'shape':shape,
                'size':size,
                'flavor':flavor,
                }
            cakes.append(cake)
            return "Thank you for your cake order."

        def second(size,flavor,frosting):
            cupcake = {
                'size':size,
                'flavor':flavor,
                'frosting':frosting,
                }
            cupcakes.append(cupcake)
            return "Thank you for your cupcake order."

        def third(name,flavor,toppings):
            pastry = {
                'name':name,
                'flavor':flavor,
                'toppings':toppings,
                }
            pastries.append(pastry)
            return "Thank you for your pastry order."
        print("You order is %s" % orders)



    

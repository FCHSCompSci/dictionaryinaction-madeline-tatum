# Madeline Tatum 9.17.18
# Dictionary project

cakes = []
cupcakes = []
pastries = []

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

# Madeline Tatum 9.17.18
# Dictionary project : Cake Shop

def make_cake(cake_id,shape,size,flavor):
    cake = {
        'cake_id':cake_id,
        'shape':shape,
        'size':size,
        'flavor':flavor,
        }
    return cake

def make_customer(cake_id,name):
    customer = {
        'cake_id':cake_id,
        'name':name,
        }
    return customer

cake_id = 0 
orders = []

while True:
    why = input("Would you like to order, pickup, or leave? ")
    if why == "order":
        order_name = input("What is the name for the order? ")
        order_name == make_customer(cake_id,'name')
        cake_id = cake_id + 1
        order_flavor = input("What flavor cake would you like? ")
        order_flavor == make_cake(cake_id, shape, size, 'flavor')
        order_size = input("What size cake would you like? ")
        order_size == make_cake( cake_id, shape, 'size', flavor)
        order_shape = input("What shape cake would you like? ")
        order_shape == make_cake(cake_id,'shape',size,flavor)
    elif why == "pickup":
        pass
    elif why == "leave":
        print("Have a nice day!")
        break

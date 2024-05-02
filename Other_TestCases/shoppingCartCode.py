cart = []
i=1
addQuestion = "Do you want to add something to your list:\n "
cartList    = "How many Items do you want to add?\n "
print("==========================================\n")
startingItem= input("  How many starting items in your list:\n ") 
startingItem = int(startingItem)                                 
z           = 0  

print("==========================================\n")
print("Please type in the item's you would like in your cart:\n")
while z < startingItem:
    item = input()
    cart.append(item)
    z = z+1

print("We are now at the shopping center ")
while True:
    itemfound = input("What have you found: \n")
    if not itemfound == "nothing":
        cart.remove(itemfound)
    Question = input(addQuestion)
    Bool = False
    if Question.lower() == "yes" :
        Bool = True
    else:
        Bool = False
    while Bool == True:
        print("Add 1 item at a time")
        cartAdd = int(input(cartList))
        z=0
        for j in range(z,cartAdd):
            item = input()
            cart.append(item)
        Bool = False
    end = input("Do you want to end the shopping trip? ")
    if end.lower() == "yes":
        break

print("These are the items missing")
print(cart)
print("Finished!")  

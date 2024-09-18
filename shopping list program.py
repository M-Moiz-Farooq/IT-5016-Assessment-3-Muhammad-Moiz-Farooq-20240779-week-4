print("Welcome to shopping list program")
item=str(input("enter name of item(or type 'done' to finish):"))
price=float(input(F"enter price of {item}:"))
item=item.lower()
total=0
shoppinglist=[]
shoppinglist.append((item,price))

while item!='done':
    total+=price

    item=str(input("enter name of item:"))
    item=item.lower()
    price=float(input(F"enter price of {item}:"))
    if item!='done':
         shoppinglist.append((item,price))
    
    if item=='done':
        break
for item,price in shoppinglist:
           print("\n Shopping List:")
           print(f"{item}: ${price}")
           print("your total is:$",total)
                              
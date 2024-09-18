'''

Collect User data

'''



'''
Collect User data
'''
id_counter = 5000
unique_id_count = id_counter + 1
id_counts = []

while True:
    name = input("Enter your name (type 'done' to exit): ")
    if name.lower() == 'done':
        break

    age = input(f"Hi {name}! Enter your age: ")
    email = input(f"Could you please enter your email too: {name}? ")

    print(f"Hi {name}! Your unique ID is: {unique_id_count}")
    id_counts.append(f"{name}:{unique_id_count}")
    unique_id_count += 1

print("List of unique IDs created against names inputted is:")
print(id_counts)


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
           
           print("your total is:$",total)

if total> 150:
      print("Category: Low")
      print("Proceed with standard routine")

else:
      print("Category: High")
      print("Review for potential discount")      


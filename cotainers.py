'''

list

'''

mylist=[1,3,90,'jess',89,'real']

firstelement=mylist[3]
print(firstelement)

mylist[3]="watermelon"
print(mylist)
#append
mylist=[]
append=input("enter something:")
while append!="null":
   
   mylist.append(append)
   print(mylist)
   append=input("enter something:")
#insert
mylist.insert(1,20)
print(mylist)

#remove
mylist.remove(90)
print(mylist)
#pop
mylist.pop()
print(mylist)
#sort
mylist.sort(key=str)
print(mylist)
#reverse
mylist.reverse()
print(mylist)
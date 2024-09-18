'''

Dictionary
'''

contacts={"Moiz":4567,"Farooq":4567, "Hamid":9980}
print(contacts)
contacts["Muhammad"]=4567
contacts["Arsal"]=66789
print(contacts)

name1="Muhammad"
name2="Moiz"
print(name1,"is at extension",contacts[name1])
if contacts[name1]==contacts[name2]:
    print(name2,"is at same extension")
    print("Hamid is at extension",contacts["Hamid"])
    print("Farooq is also at extension",contacts["Farooq"])
else:
    print(contacts)



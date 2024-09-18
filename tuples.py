'''
tuples

'''
tuple1=(1,3,4,5)
tuple2=('kkl','llk','kkjs','nig')
print(tuple1)
print(tuple2)
print(type(tuple1))
print(type(tuple2))


tuple1=(4,5,6,8,9,34,54)
print("1.",tuple1[1],tuple1[0],tuple1[5])
print("2.", tuple1[6], tuple1[3],tuple1[4],tuple1[0])

tuple2=(tuple1[1],tuple1[0],tuple1[4])
print("3.", tuple2)

for element in tuple2:
    if element >3:
        print(element)



        
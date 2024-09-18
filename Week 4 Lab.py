'''

IT5016 Week 4 Lab

Author: Muhammad Moiz Farooq
WhiteCliffe College, AKL

'''

# Password Attempt System
passwordattempt=str(input("Enter your password:"))
password="python123"
triesleft=5
while triesleft >= 1:
    if passwordattempt not in password:
        
        triesleft-=1
        
        print(F"Wrong password {triesleft} tries left")
          
        if passwordattempt not in password and triesleft ==0:
           print("Acces Blocked")
        else:
            passwordattempt=str(input("Enter your password again:"))  
    
    elif passwordattempt in password:
        triesleft-=1
        print("Access granted")
        break
        
        


# Mutliplication Table

number=int(input("Enter your number:"))
upto=12
print(F"Multiplication Table for {number} is:")
for x in range(1,upto +1):
    print(F"{number}*{x} = {number*x}")
print("Done!")    

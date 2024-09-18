'''
for loop

'''
for count in range(0,100):
    print("programming is fun")
    
print("Done!")

# even and odd calculator
total=0
for number in range(9,20):
    if number%2 == 0 or number %3 == 0:
        total+=1
print(total)

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

user_input = input("Enter a string: ")
result = count_vowels(user_input)
print(f"Number of vowels in the string: {result}")


def main():
    originalstring=input("Enter a string:")
    reversestring=originalstring[::-1]
    print(F"Original: {originalstring}")
    print(F"Reversed: {reversestring}")

main()    
   
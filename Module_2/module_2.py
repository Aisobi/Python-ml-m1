#create a funtion to find avarege of two numbers

def find_avarage(num1,num2):
  return (num1+num2)/2

#calling the funtion

print(find_avarage(10,20))
print(find_avarage(35,80))
print(find_avarage(1080,1920))
print(find_avarage(50,500))


# sort the fruits list

fruits = ["apple", "banana", "cherry", "kiwi", "grape"]
fruits.sort()

print("After sort:",fruits)



# Duplicate numbers
numbers = [1, 5, 6, 5, 1, 2, 3]

duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate numbers:", duplicates)
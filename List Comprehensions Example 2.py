#List Comprehensions Example

letters = 'abcd'
numbers = range(4)
myList = []
for letter in letters:
    for number in numbers:
        myList.append((letter,number))

print(myList)
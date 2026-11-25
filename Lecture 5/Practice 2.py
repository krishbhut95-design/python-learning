#Print  the elements of a list using while loop
#[1,4,9,16,25,36,49,64,81,100]

numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
index = 0
heros = ["Iron Man", "Captain America", "Thor", "Hulk", "Black Widow"]
index = 0
while index < len(heros):
    print(heros[index])                 
    index += 1


#print the elements of a tuple using for loop
Numbers = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(Numbers):
    if (Numbers[i] == x):
        print(f"{x} Found at index", i)
    else:
        print(f"{x} Not Found at index", i)
    i += 1  
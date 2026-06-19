# Arithmetic Operators

a = 10 #integer
b = 20 #integer
c = 3.5 #float
sum_1 = a + b + c
sum_2 = a - b - c
sum_3 = a * b * c
sum_4 = a / b / c

print(" Sum answer =", sum_1)
print(" Sum answer =", sum_2)
print(" Sum answer =", sum_3)
print(" Sum answer =", sum_4)


# Relational Operators

a = 42
b = 41
print("a > b =", a > b)
print("a < b =", a < b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)
print("a == b =", a == b)
print("a != b =", a != b)

# Assignment Operators

a = 10
a = a + 5 # a = 10 + 5
print("a =", a) #15

a += 5 # a = a + 5
print("a =", a) #20
a -= 5 # a = a - 5
print("a =", a) #15
a *= 5 # a = a * 5
print("a =", a) #75
a /= 5 # a = a / 5
print("a =", a) #15

# Logical operators
a = 5
b = 10
print("a < b and a < b =", a < b and a < b) #False
print( "a > b and a < b =", a > b and a < b) #True
print("a > b or a < b =", a > b or a < b) #True'
print("a < b or a < b =", a < b or a < b) #True
print("not (a > b) =", not (a > b)) #True
print("not (a < b) =", not (a < b)) #False
# function to calculate the sum of two numbers

def calc_sum(a, b):
    sum = a + b
    return sum
print(calc_sum(5, 10))
print(calc_sum(-3, 7))

def print_hello():
    print("Hello")

print_hello()
print_hello()

def average(a, b, c):
    sum = a + b + c
    avg = sum / 3
    return avg

print(average(1, 2, 3))
print(average(10, 20, 30))

print(" My name is Krish", end="   ")
print(" I am a Python programmer")
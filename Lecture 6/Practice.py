# WAF to print the length of a list(list is the parameter)

citys = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
def print_length(lst):
    length = len(lst)
    print("The length of the list is:", length)

print_length(citys)

# WAF to print the elements of a list in a single line(list is the parameter)
citys = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
heroes = ["Superman", "Batman", "Wonder Woman", "Spider-Man"]

def print_citys(lst):
    print(*lst)

print_citys(citys) 
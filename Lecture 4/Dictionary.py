#Dictionary in python
introduction = {
    "Name": "Bhut Krish",
    "Age": 20,
    "Subject": ("Python", "Java", "C++"), #TUple
    "city": ["Bangalore", "Delhi", "Chennai"], #List
    "marks": 90
}
print(introduction)
print(introduction["Name"])
introduction["Age"] = 21
print(introduction["Age"])
introduction["Surname"] = "Bhut"
print(introduction["Surname"])

#Null Dictionary
null_dict = {}
null_dict["Name"] = "Bhut Krish"
print(null_dict)
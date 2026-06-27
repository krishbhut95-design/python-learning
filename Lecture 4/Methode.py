    # Method Dictionary

student = {
    "Name": "Krish",
    "subjects": {
        "physics": 85,
        "chemistry": 90,
        "mathematics": 95
    }
}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("key"))
print(len(student))
pair = student.items()
print(pair)
student.update({"Name": "Krishna"})
print(student)
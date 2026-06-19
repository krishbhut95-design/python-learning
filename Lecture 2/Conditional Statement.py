#Condition statement
#it is used if condition in python
age = 20
if age >= 18:
    print("you can vote")
    print("you can drive")
if age < 18:
    print("you can not vote")
    print("you can not drive")


# if elise statement
light = "yellow"

if light == "red":
    print("stop")

elif light == "yellow":
    print("get ready")

elif light == "green":
    print("go")


# if else statement
light = "black"

if light == "red":
    print("stop")

elif light == "yellow":
    print("get ready")

elif light == "green":
    print("go")

else:
    print("light is off")


    #student marks statement
    marks = int(input ("Enter your Marks :"))
    
    if (marks >= 90):
       Grade = "A"

    elif ( marks > 90 and marks >=80):
       grade = "B"
    
    elif ( marks < 80 and marks >= 70):
        grade = "C"
    
    elif ( marks < 70 and marks <= 33):
        grade = "D"
 
    else:
        grade = "E"

        print("Grade of the student ->", grade)

        # necting stetment

        age = 45
        if age >=18:
            if age >= 80:
                print("Can not drive")
            else:
                print("Can drive")
        else:
            print("Can not drive")


            

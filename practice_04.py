dict = {
    "table" : ["a piece of furtniture" , "list offacts & figures"] ,
    "cat"  : "a small animal"
}

print(dict)

# you are given a list of subject. Assume one classroom is required for 1 subject. How amany classrooms are neede by all students.

set1 = {"python", "java", "C++", "python" , "javascript" , "java" , "python" ,"C++" , "C"}
print(len(set1))

# WAP to enter marks of 3 sunject from user and store them in adictionary. Start with an empty dictionary and add one by one. Use subject name as key and marks as value.

mark1 = input("enter sub 1 mark : ")
mark2 = input("enter sub 2 mark : ")
mark3 = input("enter sub 3 mark : ")

dict = {
    "phy" : mark1,
    "chem" : mark2,
    "maths" : mark3
}

print(dict)

# 2nd method
marks = {}

x = input("enter marks phy : ")
marks.update({"phy" : x})

y = input("enter marks math : ")
marks.update({"math" : y})

z = input("enter marks sci : ")
marks.update({"sci" : z})
print(marks)

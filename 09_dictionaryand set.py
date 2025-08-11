# dictionary
dict = {
     "name" : "Anish",
     "sub" : ["Maths",  "English"],
     "surname": ("Mishra", "kumar"),
     "age" : 21.5, 
}

dict["name"] = "Anish Mishra"
print(dict)
print(type(dict))


student = {
     "name" : ("Anish", "Amit"), 
      "subjects" : {
          "maths" : 98,
           "physic" : 78
      }               
}
print(student)
print((student.values()))

# set

set1 = {1,2,3,4,5}
set2 = {6,7,8,2,3}

print(set1.add(99))
print(set2.remove(8))
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.pop())
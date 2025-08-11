# # write a program to input user first name and print its length
name = input(("enter your first name : "))
name = len(name)
print(name)

# # write a program to find the occuranace of $ in a string
str = "this is $ and please find $ end"
print(str.count("$"))
print(str.endswith("nd"))
print(str.replace("please", "pls"))
print(str.find("please"))

#write a program to  check if no enter by user is even or odd

number = int(input("enter any number : "))

if (number % 2 == 0):
    print("even number")
elif(number % 2 != 0):
    print("odd number")   

# write a program to find the greatest of 4 number entered by user
a = int(input("enter first number : "))
b = int(input("enter second numner : "))
c = int(input("enter  third no : "))
d = int(input("enter fourth number : "))

if(a>b and a>c and a>d):
    print("first number is greater: ", a)
elif(b>c and b>d and b>a):
    print("second number is greater: ", b)
elif(c>a and c>b and c>d):
    print("third number is greater : ", c)
else:
    print("fourth number is greater: ",d) 

# write a program to check if no is multiple of 7

number = int(input("enter any number : "))

if(number % 7 == 0):
    print("number is multiple of 7")
else:
    print("not multiple of 7")






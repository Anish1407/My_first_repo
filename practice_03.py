# write a program to ask user enter 3 movie name and store them in a list

movie1 = input("enter first movie : ")

movie2 = input("enter second movie : ")

movie3 = input("enter second movie : ")

list = [movie1 , movie2 , movie3]
print(list)

# print(len(list))
# print(type(list))
# print(list[1:])



#second method:
mov = []
movie1 = input("enter first movie : ")
mov.append(movie1)
movie2 = input("enter second movie : ")
mov.append(movie2)
movie3 = input("enter second movie : ")
mov.append(movie3)

print(mov)

#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.
dic= {}
x=int(input('enter total no of enties '))
for i in range(0,x):
    dic[i] = i
z=int(input("enter key value"))
c = False #c is flag here
for j in dic.keys():
    if dic[j]==z:
        print(j)
        c= True
        break
if not c:
    print("invalid case")
#Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.Print the marks of a given student from that dictionary for every subject. Hint: Use nested dictionary to store subjects marks.
student = {"viney":{"c++":100,"python":100,"ADBMS":99},"ayush":{"c++":90,"python":95,"ADBMS":96}}
name=input("enter studend name: ")
if name in student:
    print(name)
    for k in student[name].items():
        print(k)
else:
    print("invalid case")

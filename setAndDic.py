num=[1,2,3,4,6]
num.append(7)
print(num)
print()
names=["Abhishek","Sandeep","Mahesh","Surya"]
names.insert(2,"Rahul")
print(names)
list=[10,20,30,20,10,40]
list.remove(20)
print(list)
num1=[1,2,3,0,7,6,10,9]
num1.sort()
num2=sorted(num1,reverse=True)
print(num1)
print(num2)
nums=[1,2,3,4,5,6]
print(nums.pop())
nums=[1,2,3,2,4,5,6,2,2]
print(nums.count(2))
fruits=["apple","banana","mango","orange"]
print(fruits.index("mango"))
num1=[1,2,3]
num2=[4,5,6]
num1.extend(num2)
print(num1)
nums=(10,20,10,40,60,10)
print(nums.count(10))
lang=("python","java","c","c++")
print(lang.index("c++"))
set1={1,2,3,4}
set1.add(5)
print(set1)
set2={10,20,30,40}
set2.remove(30)
print(set2)
s1={1,2,3}
s2={3,4,5}
set3=s1.union(s2)
print(set3)
a1={1,2,3,4}
a2={3,4,5,6}
set4=a1.intersection(a2)
print(set4)
b1={1,2,3,4}
b2={3,4,5,6}
set5=b1.difference(b2)
print(set5)
c1={1,2,3}
c2={2,3,4}
set6=c1.symmetric_difference(c2)
print(set6)
set7={1,1,1,3,4,5,6}
print(set7)
d1={1,2,3}
d2={2,1,5,6}
print(not d1.isdisjoint(d2))
set9={1,2,3}
set9.clear()
print(set9)
set10={10,20,30}
print(20 in set10)

student={
    "name":"Abhishek",
    "Age":20,
    "marks":90    
}
for i in student.values():
    print(i)
student={
    "name":"Rahul",
    "Age":"20"
}
student["city"]="delhi"
print(student)
student={
    "name":"Rahul",
    "Age":"20"
}
student["city"]="delhi"
student["Age"]=21
print(student)

student={
    "name":"Rahul",
    "Age":"20",
    "city":"Hyderabad"
}
del student["city"]
print(student)
student={
    "name":"Rahul",
    "Age":"20"
}
print("Age" in student)
fruits={
    "mango":10,
    "apple":20,
    "orange":30
}
for key in fruits.keys():
    print(key)
fruits={
    "mango":10,
    "apple":20,
    "orange":30
}
for value in fruits.values():
    print(value)
fruits={
    "mango":10,
    "apple":20,
    "orange":30
}
for key,value in fruits.items():
    print(key,value)
dict={
    "a":10,
    "b":20,
    "c":30
}
sum=0
for v in dict.values():
    sum+=v
print(sum)
students={
    "names":["Abhishek","Sandeep","Thribhuvan"],
    "marks":[90,79,77]
}
maxi=max(students["marks"])
i=students["marks"].index(maxi)
name=students["names"][i]
print(name)

    












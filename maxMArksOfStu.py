students={"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
maxi=0
for i in students:
    if students[i]>maxi:
        maxi=students[i]
for j in students:
    if students[j]==maxi:
        print(j)
        break
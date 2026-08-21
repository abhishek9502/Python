students={"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
n=len(students)
sum=0
for i in students.values():
    sum+=i
print(f"Avg of student marks are: {sum/n:.1f}")

nums=list(map(int,input("Enter Numbers here :").split(",")))
maxi=float("-inf")
for i in nums:
    if maxi<i:
        maxi=i
print(f"Largest number :{maxi}")
mini=float("inf")
for i in nums:
    if mini>i:
        mini=i
print(f"Smallest number :{mini}")
sum=0
for i in nums:
    sum+=i
print(f"Sum of numbers are :{sum}")
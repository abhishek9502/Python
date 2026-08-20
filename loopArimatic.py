N=int(input("Enter Number N :"))
sum=0
for i in range(1,N+1):
    if i%2==0:
        sum+=i
print(sum)
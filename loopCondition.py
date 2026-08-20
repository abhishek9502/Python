N=int(input("Enter Number N :"))
count=0
while N!=0:
    last=N%10
    if last%2==0:
        count+=1
    N=N//10
print(count)
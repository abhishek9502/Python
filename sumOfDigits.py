n=int(input("Enter number here :"))
sum=0
while n!=0:
    last=n%10
    sum+=last
    n//=10
print(sum)
s=input("Enter words here_:")
count=0
words=s.split()
for i in words:
    if i.upper()=="python".upper():
        count+=1
print(count)
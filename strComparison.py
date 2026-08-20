str=input("Enter the words :")
words=str.split()
var=words[0]
for i in range(len(words)-1):
    if var.upper()>words[i+1].upper():
        var=words[i+1]
print(var)
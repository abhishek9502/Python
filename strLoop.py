s=input("Enter the string :")
vowels="aeiouAEIOU"
numbers="0123456789"
countVowels=0
countConsonants=0
countDigits=0
for i in s:
    if i in vowels:
        countVowels+=1
    elif i.isalpha() and i not in vowels:
        countConsonants+=1
    elif i in numbers:
        countDigits+=1
print(f"Vowels :{countVowels}")
print(f"Consonants :{countConsonants}")
print(f"Digits :{countDigits}")
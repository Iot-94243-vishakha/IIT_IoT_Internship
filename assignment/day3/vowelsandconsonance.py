def vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiou":
            count+=1
    return count
        
def consonants(text):
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in "aeiou":
            count+=1
    return count
    
def ratio(vowel_count,consonant_count):
    if consonant_count==0:
        print("Invalid number(No consonats)")
    else:
       r=vowel_count/consonant_count
       print("Ratio(Vowels:Consonants)=",r)

text=input("Enter any sentence:").lower()
v=vowels(text)
c=consonants(text)

print("Number of vowels:",v)
print("Number of consonants:",c)

ratio(v,c)
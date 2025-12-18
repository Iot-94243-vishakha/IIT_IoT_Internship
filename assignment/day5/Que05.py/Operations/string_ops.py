def reverse(text):
    
    return text[::-1]

def vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    return count
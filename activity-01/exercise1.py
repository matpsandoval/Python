import os

file_dir = os.path.dirname(__file__)
file_reader = open(os.path.join(file_dir, "text.txt"))

text = file_reader.read().lower()

vowels = "aeiou"
consonants = "bcdfghjklmnñpqrstvwxyz"

# solution 1
vowels_qty = 0
consonants_qty = 0

for letter in text:
    for x in vowels:
        if letter == x: 
            vowels_qty = vowels_qty + 1
        
    for c in consonants:
        if letter == c:
            consonants_qty = consonants_qty + 1


print("Vocals:", vowels_qty)
print("Consonants:", consonants_qty)



# solution 2
vowels_qty = 0
consonants_qty = 0

for letter in text:
    if letter in vowels:
        vowels_qty += 1
    if letter in consonants:
        consonants_qty += 1

print("Vocals:", vowels_qty)
print("Consonants:", consonants_qty)

file_reader.close()

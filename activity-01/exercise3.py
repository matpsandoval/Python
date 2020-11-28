# Solucion 1 
# import os

# file_dir = os.path.dirname(__file__)
# file_reader = open(os.path.join(file_dir, "text.txt"))

# text = file_reader.read().lower()

# word_input = input("ingrese una palabra: ")

# if word_input in text:
#     print("Se encontro la palabra:", word_input)
# else:
#     print("No se encontro la palabra")

# file_reader.close()



# Solucion 2
import os

file_dir = os.path.dirname(__file__)
file_reader = open(os.path.join(file_dir, "text.txt"))

text = file_reader.read().lower()

words_arr = text.split()

found = False

word_input = input("Ingrese una palabra: ")

for x in words_arr:
    if word_input == x:
        found = True

if found:
    print("Se encontro la palabra:", word_input)
else: 
    print("No se encontro la palabra")
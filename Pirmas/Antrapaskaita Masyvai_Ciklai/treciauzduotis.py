words  = []
list_size = int(input("Iveskite norima zodziu kieki "))

for word in range(list_size):
     input_words = input("Iveskite zodi ")
     words.append(input_words)

for word in words:
     index = words.index(word)
     print(f"Zodzio: '{word}' ilgis yra {len(word)} jo eiles numeris yra : {index + 1}")
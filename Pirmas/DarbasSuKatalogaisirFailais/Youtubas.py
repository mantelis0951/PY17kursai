import os

os.chdir('C:\\Users\\Mantas\\Desktop\\Naujas Katalogas')

for file in os.listdir():
    if file == '.DS_Store':
        continue
    print(file)
    name, ext = os.path.splitext(file)
    splitted = name.split("-")
    splitted = [s.strip() for s in splitted]
    new_name = f"{splitted[0].zfill(2)}{ext}"
    os.rename(file,new_name)

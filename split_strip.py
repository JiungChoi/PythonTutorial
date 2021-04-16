
with open('data/chicken.txt', 'r',encoding='UTF8') as f:
    for line in f:
     print(line.strip())

#split
my_string = '1. 2. 3. 4. 5. 6'
print(my_string.split(". "))
print(my_string.split("."))

full_name = 'Kin, Yuna'
print(full_name.split("n"))
print(full_name.split())
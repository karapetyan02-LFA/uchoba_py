ids = [] # Пустой список
print("ids:", ids)

ids.append(123)
print("ids:", ids)

ids.append(5)
ids.append(3)
print("ids:", ids)

print("длина списка ids:", len(ids))

pet_names = [ ]

for i in range(3):
    name = input("Введите имена питомцов %i " %(i +1))
    pet_names.append(name)
    
print("Ваш список имен для питомца:", pet_names)

for name in pet_names:
    print(name, end=", ")
    
print *pet_names
is_program_work = True
is_choice_wrong = False
temperature_celsius = 20 
 

while is_program_work:
    # Отрисовка данных и приглашения к вводу 
    print(["ПУЛЬТ ТЕМПЕРАТУРЫ"])
    print("")
    print("Текущая температура: %i " % temperature_celsius)
    print("")
    print("1 - +1 градус")
    print("2 - -1 градус")
    print("0 - выход")

    if is_choice_wrong:
        print("Ошибка, некорректный воод")
        print("")
    print(">>>", end="")
    
    # Получение данных от пользователя (ввод)
    choice = input().strip()
    
    # Обработка данных, обновление состояния 
    
    is_choice_wrong = False
    
    if choice == "0":
        is_program_work = False 
        
    elif choice == "1":
        temperature_celsius +=1
        
    elif choice == "2":
        temperature_celsius -=1
    else: 
        is_choice_wrong = True 
        
         

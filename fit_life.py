print("Добро пожаловать в FitLive Treker")  #  Приветствие

personal_water_ml = 30
personal_water_l = 1000

user_name = input("Укажите Ваше имя :")  #  Запрашиваем Имя
user_age = int(input("Укажите ваш возраст :"))  #  Запрашиваем Возраст

user_weight = float(input("Укажите ваш вес (кг)," 
                          "через точку (Например '74.2') :"))  #  Запрашиваем Вес
user_height = float(input("Укажите ваш рост (метры), " 
                          "используя точку, (Например '1.83') : "))  #  Запрашиваем Рост

bmi = user_weight / (user_height ** 2)  #  Узнаем ИМT(Индекс Массы Тела)
rounding_imt = round(bmi, 1)  #  Округляем ИМТ
water_ml = user_weight * personal_water_ml  #  Узнаем норму воды в МЛ
water_l = water_ml / personal_water_l  #  Переводим В литры
rounding_water = round(water_l, 1)  #  Округляем норму литров

print('-' * 40)
print('-' * 40)

print(
    "Благодарим за данные, отчет для пользователя:"
     f" {user_name} , Возраст : {user_age} (Л) ")
print(f"Индекс массы тела : {rounding_imt}")
print(f"Рекомендуемая суточная норма воды : {rounding_water}")
print("Расчет окончен. Счастливо!")

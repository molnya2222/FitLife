print("Добро пожаловать в FitLive Treker")  # Приветствие

PERSONAL_WATER_ML = 30
PERSONAL_WATER_1 = 1000
BORDER_LENGTH = 40

user_name = input("Укажите Ваше имя :")  # Запрашиваем Имя
user_age = int(input("Укажите ваш возраст :"))  # Запрашиваем Возраст

user_weight = float(input("Укажите ваш вес (кг),"
                          "через точку (Например '74.2') :"))

user_height = float(input("Укажите ваш рост (метры), "
                          "используя точку, (Например '1.83') : "))

bmi = user_weight / (user_height ** 2)  # Узнаем ИМT(Индекс Массы Тела)
rounding_imt = round(bmi, 1)  # Округляем ИМТ
water_ml = user_weight * PERSONAL_WATER_ML  # Узнаем норму воды в МЛ
water_l = water_ml / PERSONAL_WATER_1  # Переводим В литры
rounding_water = round(water_l, 1)  # Округляем норму литров

print("-" * BORDER_LENGTH)
print("-" * BORDER_LENGTH)

print(
    f"Благодарим за данные, отчет для пользователя: {user_name}, "
    f"возраст: {user_age} л.",
)
print(f"Индекс массы тела : {rounding_imt}")
print(f"Рекомендуемая суточная норма воды : {rounding_water}")
print("Расчет окончен. Счастливо!")

import pyttsx3

engine = pyttsx3.init()

name = input('Введите ваше имя:\n')
engine.say('Введите ваше имя')
count = 0

q1 = 'Бразилия'
q2 = '10'
q3 = 'Индия'
q4 = 'США'
q4_1 = 'Америка'
q5 = '25'
q6 = 'г'
q7 = 'в'
q8 = '12'
q8_1 = '21'
q9 = 'разговор'
q10 = '0'

engine.say('первый вопрос')
engine.runAndWait()
engine.say('Назовите столицу Бразилии ')
engine.runAndWait()
first_q = input(f'{name}, вводите ваш ответ:\n')
if first_q == q1:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q1}')
    engine.runAndWait()

engine.say('второй вопрос')
engine.runAndWait()
engine.say('Назовите корень из ста ')
engine.runAndWait()
second_q = input(f'{name}, вводите ваш ответ:\n')
if second_q == q2:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q2}')
    engine.runAndWait()

engine.say('третий вопрос')
engine.runAndWait()
engine.say('Назавите страну с наибольшим количеством населения ')
engine.runAndWait()
third_q = input(f'{name}, вводите ваш ответ:\n')
if third_q == q3:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q3}')
    engine.runAndWait()
    
engine.say('четвёртый вопрос')
engine.runAndWait()
engine.say('Назавите страну с самым большим военным бюджетом')
engine.runAndWait()
fourth_q = input(f'{name}, вводите ваш ответ:\n')
if fourth_q == q4:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
elif fourth_q == q4_1:
    engine.say('Америка это континент, а не страна')
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q4}')
    engine.runAndWait()
    
engine.say('пятый вопрос')
engine.runAndWait()
engine.say('Какой корень у 25 в квадрате?')
engine.runAndWait()
fifth_q = input(f'{name}, вводите ваш ответ:\n')
if fifth_q == q5:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q5}')
    engine.runAndWait()

engine.say('Теперь перейдём к тестовой части')
engine.runAndWait()
engine.say('Указать нужно только букву')
engine.runAndWait()
engine.say('шестой вопрос')
engine.say('Какой герой мультфильма живёт в ананасе под водой')
engine.runAndWait()
engine.say('а   Камбала')
engine.runAndWait()
engine.say('б   Немо')
engine.runAndWait()
engine.say('в   Рик и Морти')
engine.runAndWait()
engine.say('г   Губка Боб Квадратные Штаны')
engine.runAndWait()
sixth_q = input(f'{name}, вводите ваш ответ:\n')
if sixth_q == q6:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q6}')
    engine.runAndWait()

engine.say('седьмой вопрос')
engine.runAndWait()
engine.say('Какая страна производит больше всего кофе в мире? а)Колумбия    б)Индонезия  в)Бразилия    г)Вьетнам')
engine.runAndWait()
engine.say('а   Колумбия')
engine.runAndWait()
engine.say('б   Индонезиям')
engine.runAndWait()
engine.say('в   Бразилия')
engine.runAndWait()
engine.say('г   Вьетнам')
engine.runAndWait()
seventh_q = input(f'{name}, вводите ваш ответ:\n')
if seventh_q == q7:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q7}')
    engine.runAndWait()

engine.say('Теперь перейдём к логическим задачам')
engine.runAndWait()
engine.say('восьмой вопрос')
engine.say('На столе лежат две монеты, в сумме они дают 3 рубля, но одна из них - НЕ 1 рубль')
engine.runAndWait()
engine.say('Ответ дайте в формате двузначного числа.(5 монет и 5 монет - 55)')
engine.runAndWait()
engine.say('Пример   5 монет и 5 монет - 55')
engine.runAndWait()
eighth_q = input(f'{name}, вводите ваш ответ:\n')
if eighth_q == q8:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
elif eighth_q == q8_1:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q8} или {q8_1}')
    engine.runAndWait()

engine.say('девятый вопрос')
engine.runAndWait()
engine.say('Что можно завязать  но нельзя развязать?')
engine.runAndWait()
ninth_q = input(f'{name}, вводите ваш ответ:\n')
if ninth_q == q9:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q9}')
    engine.runAndWait()

engine.say('десятый вопрос')
engine.runAndWait()
engine.say('С какой скоростью км в час должна двигаться собака, чтобы не слышать звона сковородки, привязанного к её хвосту?Ответ дайте цифрой(со скоростью 5км/ч - 5)')
engine.runAndWait()
tenth_q = input(f'{name}, вводите ваш ответ:\n')
if tenth_q == q10:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q10}')
    engine.runAndWait()

# engine.say(f'Вы правильно ответили на {count} вопросов')
# engine.runAndWait()
# if count != 10:
#     engine.say(f'Неправильных ответов {10-count}')
#     engine.runAndWait()
    
if count >= 3:
    engine.say(f'{name}, {count} из десяти  это как-то маловато   иди учись')
    engine.runAndWait()
elif count > 3 and count <= 7:
    engine.say(f'{name}, {count} из десяти  это нормальный результат')
    engine.runAndWait()
elif count > 7 and count <= 10:
    engine.say(f'{name}, {count} из десяти  это отличный результат')
    engine.runAndWait()

engine.runAndWait()

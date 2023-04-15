import pyttsx3

engine = pyttsx3.init()

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

engine.say('1. Назовите столицу Бразилии ')
engine.runAndWait()
first_q = input()
if first_q == q1:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q1}')
    engine.runAndWait()

engine.say('2. Назовите корень из ста ')
engine.runAndWait()
second_q = input()
if second_q == q2:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q2}')
    engine.runAndWait()

engine.say('3. Назавите страну с наибольшим количеством населения ')
engine.runAndWait()
third_q = input()
if third_q == q3:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q3}')
    engine.runAndWait()

engine.say('4. Назавите страну с самым большим военным бюджетом')
engine.runAndWait()
fourth_q = input()
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

engine.say('5. Какой корень у 25 в квадрате?')
engine.runAndWait()
fifth_q = input()
if fifth_q == q5:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q5}')
    engine.runAndWait()

engine.say('Теперь перейдём к тестовой части.(Указать нужно только букву)')
engine.runAndWait()
engine.say('6. Какой герой мультфильма живёт в ананасе под водой? а)Камбала    б)Немо  в)Рик и Морти    г)Губка Боб Квадратные Штаны')
engine.runAndWait()
sixth_q = input()
if sixth_q == q6:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q6}')
    engine.runAndWait()

engine.say('7. Какая страна производит больше всего кофе в мире? а)Колумбия    б)Индонезия  в)Бразилия    г)Вьетнам')
engine.runAndWait()
seventh_q = input('')
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
engine.say('8. На столе лежат две монеты, в сумме они дают 3 рубля, но одна из них - НЕ 1 рубль?.Ответ дайте в формате двузначного числа.(5 монет и 5 монет - 55)')
engine.runAndWait()
eighth_q = input()
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

engine.say('9. Что можно завязать, но нельзя развязать?')
engine.runAndWait()
ninth_q = input()
if ninth_q == q9:
    engine.say('Правильно')
    count += 1
    engine.runAndWait()
else:
    engine.say(f'Неправильно')
    engine.say(f'Правильный ответ {q9}')
    engine.runAndWait()

engine.say('10. С какой скоростью км в час должна двигаться собака, чтобы не слышать звона сковородки, привязанного к её хвосту?Ответ дайте цифрой(со скоростью 5км/ч - 5)')
engine.runAndWait()
tenth_q = input()
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
    engine.say(f'{count} из десяти  это как-то маловато   иди учись')
    engine.runAndWait()
elif count > 3 and count <= 7:
    engine.say(f'{count} из десяти  это нормальный результат')
    engine.runAndWait()
elif count > 7 and count <= 10:
    engine.say(f'{count} из десяти  это отличный результат')
    engine.runAndWait()

engine.runAndWait()

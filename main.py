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
first_q = input()
if first_q == q1:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q1)

engine.say('2. Назовите корень из ста ')
second_q = input()
if second_q == q2:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q2)

engine.say('3. Назавите страну с наибольшим количеством населения ')
third_q = input()
if third_q == q3:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q3)

engine.say('4. Назавите страну с самым большим военным бюджетом')
fourth_q = input()
if fourth_q == q4:
    engine.say('Правильно')
    count += 1
elif fourth_q == q4_1:
    engine.say('Америка это континент, а не страна')
else:
    engine.say('Неправильно.Правильный ответ: ', q4)

engine.say('5. Какой корень у 25 в квадрате?')
fifth_q = input()
if fifth_q == q5:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q5)

engine.say('Теперь перейдём к тестовой части.(Указать нужно только букву)')
engine.say('6. Какой герой мультфильма живёт в ананасе под водой? а)Камбала    б)Немо  в)Рик и Морти    г)Губка Боб Квадратные Штаны')
sixth_q = input()
if sixth_q == q6:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q6)

engine.say('7. Какая страна производит больше всего кофе в мире? а)Колумбия    б)Индонезия  в)Бразилия    г)Вьетнам')
seventh_q = input('')
if seventh_q == q7:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q7)

engine.say('Теперь перейдём к логическим задачам')
engine.say('8. На столе лежат две монеты, в сумме они дают 3 рубля, но одна из них - НЕ 1 рубль?.Ответ дайте в формате двузначного числа.(5 монет и 5 монет - 55)')
eighth_q = input()
if eighth_q == q8:
    engine.say('Правильно')
    count += 1
elif eighth_q == q8_1:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q8)

engine.say('9. Что можно завязать, но нельзя развязать?')
ninth_q = input()
if ninth_q == q9:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q9)

engine.say('10. С какой скоростью км в час должна двигаться собака, чтобы не слышать звона сковородки, привязанного к её хвосту?.Ответ дайте цифрой(со скоростью 5км/ч - 5)')
tenth_q = input()
if tenth_q == q10:
    engine.say('Правильно')
    count += 1
else:
    engine.say('Неправильно.Правильный ответ: ', q10)

engine.say('Вы правильно ответили на ', count, 'вопросов')
if count != 10:
    engine.say('Неправильных ответов: ', 10-count)

engine.runAndWait()

#Місце для коду Завдання 1
"""
x = '(64*125+128*75)/800*500-(300*40-5107*800)/70'
expr = (64*125+128*75)/800*500-(300*40-5107*800)/70
print("Значення виразу ", x, " = {}".format(expr))
"""

#Місце для коду Завдання 2
"""
def separation(z):
    return ((64*125+128*75)/800)*z-((300*40-5107*800)/70)

result = separation(11)
print("Результат обчислення виразу з параметром 11: {}".format(result))
"""

#Місце для коду Завдання 3
"""
lst = ['слон', 10, 333, 'кіт', 'крокодил', 'мавпа', 1, 1000, 'жаба', 22]

# виведення кількості елементів у масиві
print("Кількість елементів масиву: {}".format(len(lst)))

# виведення текстових елементів масиву
text_elements = [str(a) for a in lst if isinstance(a, str)]
print("Перелік текстових рядків: {}".format(", ".join(text_elements)))

# виведення цілих чисел масиву
int_elements = [str(a) for a in lst if isinstance(a, int)]
print("Перелік цілих чисел: {}".format(", ".join(int_elements)))

# виведення відсотку числових елементів масиву
num_count = len([a for a in lst if isinstance(a, int)])
percent = (num_count / len(lst)) * 100
print("Відсоток чисел у масиві: {:.2f}%".format(percent))
"""

#Місце для коду Завдання 4
"""
def replace_lyakh_on_khovrakh(poem):
    words = poem.split()
    for i in range(len(words)):
        if words[i].startswith('лях'):
            words[i] = words[i].replace('лях','ховрах')
            words[i] = words[i].replace('Лях','ховрах')
    return ' '.join(words)

kobzar = "Звір тілько виє по селу, Гризучи трупи. Не ховали, Вовків ляхами годували, Аж поки снігом занесло Огризки вовчі…\nНе спинила хуртовина\nПекельної кари:\nЛяхи мерзли, а козаки\nГрілись на пожарі."

result = replace_lyakh_on_khovrakh(kobzar)
print(result)

text = 'Лях у полях на нулях смажить вовка на вуглях, бо такий Шлях'
result = replace_lyakh_on_khovrakh(text)
print(result)
"""

#Місце для коду Завдання 5
"""
text = input("Введіть текст: ")
aeyuio = ['а', 'е', 'и', 'і', 'о', 'у', 'я', 'ю', 'є', 'ї']
words = text.split()

for i in range(len(words)):
    if words[i][-1].lower() in aeyuio:
        words[i] = words[i][:-1] + words[i][-1].upper()
result = ' '.join(words)

print("Змінений текст - ", result)
"""

#Місце для коду Завдання 6
def triangle_area(a, b):
    area = (a*b)/2
    return area

input_str = input("Введіть довжину катетів через кому: ")
a, b = map(float, input_str.split(','))
area = triangle_area(a, b)

print("Катет 1 = ", a)
print("Катет 2 = ", b)
print("Площа прямокутного трикутника = ", area)
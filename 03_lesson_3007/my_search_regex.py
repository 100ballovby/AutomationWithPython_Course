import re

test = open(r'/Users/demidraksin/PycharmProjects/AutomationWithPython/03_lesson_3007/exam/questions/cap_quiz_1.txt')
content = test.read()
print(content)

ex = input('Введите город: ').capitalize()  # беру текст пользователя
testRegex = re.compile(ex)  # и использую его для поиска

res = testRegex.search(content)
# метод .capitalize() делает первую букву в строке большой

if res.group() != None:
    print('Found: ' + res.group())
else:
    print('Not found!')

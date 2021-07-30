import random
import os

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento',
            'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu',
            'Idaho': 'Boie', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis',
            'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
            'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul',
            'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena',
            'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord',
            'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
            'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus',
            'Oaklahoma': 'Oaklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg',
            'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin',
            'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond',
            'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
            'Wyoming': 'Cheyenne'}
try:
    os.mkdir('exam')
    os.mkdir('exam/answer')
    os.mkdir('exam/questions')
except FileExistsError:
    pass

for i in range(35):
    quizFile = open(os.path.join('exam', 'questions', f'cap_quiz_{i + 1}.txt'), 'w')
    answerKey = open(os.path.join('exam', 'answer', f'ans_quiz_{i + 1}.txt'), 'w')
    # создаю файлы с вопросами и ключами-ответами

    quizFile.writelines('Name:\n\nDate:\n\nForm\n\n')  # заполняю шапку билета
    quizFile.writelines((' ' * 20) + f'State + capitals quiz. Question №{i + 1}\n\n')  # записываю номер билета

    states = list(capitals.keys())  # ключи словаря превращаю в список штатов
    random.shuffle(states)  # перемешиваю список

    for answer in range(50):  # для всех 50 штатов
        correct_answer = capitals[states[i]]  # достану ПРАВИЛЬНУЮ столицу штата
        wrong_answer = list(capitals.values())  # список столиц ВСЕХ штатов
        del wrong_answer[wrong_answer.index(correct_answer)]  # удаляю правильный ответ из списка неправильных
        wrong_answer = random.sample(wrong_answer, 3)  # сохраняю 3 случайных ответа

        ans_option = wrong_answer + [correct_answer]  # создаю варианты ответов
        random.shuffle(ans_option)  # перемешиваю ответы

    # Записываю вопросы и вариантов ответов в файл с билетом
    quizFile.write(f'What is the capital of {states[i]}?\n')

    for i in range(4):
        quizFile.write(' ' * 10 + f'{i + 1}. {ans_option[i]}\n')





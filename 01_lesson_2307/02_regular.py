import re  # импортирую регулярки

# My number is: 497-555-0100
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # создаю объект для поиска
search = phoneRegex.search('My number is: 497-555-0100, thank you!')
print(search.group())

import docx
import requests


url = 'https://gutenberg.org/cache/epub/1112/pg1112.txt'
con = requests.get(url)  # обращаюсь к URL-адресу
print(type(con.text))  # проверил тип объекта, который отправил сервер


doc = docx.Document()  # создаю документ Word
doc.add_paragraph(con.text)
doc.save('my_doc.docx')
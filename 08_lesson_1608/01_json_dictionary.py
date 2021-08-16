list_json = [
    {'userId': 'David', 'id': 1, 'title': 'delectus aut autem', 'completed': False},
    {'userId': 'David', 'id': 2, 'title': 'quis ut nam facilis et officia qui', 'completed': True},
    {'userId': 'David', 'id': 3, 'title': 'fugiat veniam minus', 'completed': False},
    {'userId': 'John', 'id': 4, 'title': 'et porro tempora', 'completed': True},
    {'userId': 'John', 'id': 5, 'title': 'laboriosam mollitia et enim quasi adipisci quia provident illum',
     'completed': False},
    {'userId': 'John', 'id': 6, 'title': 'qui ullam ratione quibusdam voluptatem quia omnis', 'completed': False},
    {'userId': 'Matrin', 'id': 7, 'title': 'illo expedita consequatur quia in', 'completed': False},
    {'userId': 'Matrin', 'id': 8, 'title': 'quo adipisci enim quam ut ab', 'completed': True},
    {'userId': 'Matrin', 'id': 9, 'title': 'molestiae perspiciatis ipsa', 'completed': False}
]
task_by_user = {}
for todo in list_json:
    if todo['completed']:
        try:
            task_by_user[todo['userId']] += 1
        except KeyError:
            task_by_user[todo['userId']] = 1

print(task_by_user)
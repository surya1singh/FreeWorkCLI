

tasks = [
    {
        'id': 1,
        'title': u'Create FreeWorkCLI',
        'status': u'In progress',
        'estimated_time': 10,
        'time spent' : 0
    }
]
def Personal(user):
    show_commands()
    while True:
        break


def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

def show_commands():
    print('What action would you like to take:')
    print('[C]reate a Task')
    print('View [P]ending')
    print('View [C]ompleted')
    print('View [O]n going task')
    print('[L]og work for task')
    print('[C]hange Passowrd')
    print('e[X]it app')
    print('[?] Help (this info)')
    print()

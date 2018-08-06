from colorama import Fore

tasks = [
    {
        'id': 1,
        'title': u'Create FreeWorkCLI',
        'status': u'In progress',
        'estimated_time': 10,
        'time_spent' : 0
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
        'status': request.json.get('status', ""),
        'estimated_time':10
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

def show_commands():
    print(Fore.BLACK)
    print(' '*5,'What action would you like to take:')
    print(' '*5,'[C]reate a Task')
    print(' '*5,'View [P]ending')
    print(' '*5,'View [C]ompleted')
    print(' '*5,'View [O]n going task')
    print(' '*5,'[L]og work for task')
    print(' '*5,'[C]hange Passowrd')
    print(' '*5,'e[X]it app')
    print(' '*5,'[?] Help (this info)')
    print()

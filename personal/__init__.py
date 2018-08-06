from colorama import Fore
from common.general import get_action, unknown_command
from db.todo import tasks
from infrastructure.switchlang import switch
import infrastructure.state as state
from db.user import change_password

def Personal(user):
    global brk
    brk = 0
    show_commands()
    while True:
        action = get_action(user)
        with switch(action) as s:
            s.case('t', lambda: create_task(user))
            s.case('b', lambda: backlog(user))
            s.case('c', lambda: completed_task(user))
            s.case('o', lambda: in_progress(user))
            s.case('l', lambda: log_work(user))
            s.case('p', lambda: change_password(user))
            s.case(['<'], break_loop )
            s.case(['e', 'bye', 'exit', 'exit()'], exit )
            s.case('?', show_commands)
            s.case('', lambda: None)
            s.default(unknown_command)
            if brk:
                break


def show_commands():
    print(Fore.BLACK)
    print(' '*5,'What action would you like to take:')
    print(' '*5,'Create a [T]ask')
    print(' '*5,'View [B]acklog')
    print(' '*5,'View [C]ompleted')
    print(' '*5,'View [O]n going task')
    print(' '*5,'[L]og work for task')
    print(' '*5,'[C]hange [P]assoword')
    print(' '*5,'[<] Main menu')
    print(' '*5,'[E]xit app')
    print(' '*5,'[?] Help (this info)')
    print()

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
    return task

def break_loop():
    global brk
    brk = 1

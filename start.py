from colorama import Fore
from common.general import get_action, unknown_command
from infrastructure.switchlang import switch
import infrastructure.state as state
from common.option_parser import OptParser
from personal import Personal
from db.user import login_user


def main(kwargs):
    user = login_user(kwargs['username'],kwargs['password'])
    if not user:
        raise ValueError("Incorrect User/password")
    try:
        welcome(user)
        while True:
            show_commands()
            action = get_action(user)
            with switch(action) as s:
                s.case('p', lambda: Personal(user))
                s.case('o', lambda: Office(user))
                s.case(['e', 'bye', 'exit', 'exit()'], exit)
                s.case('?', show_commands)
                s.case('', lambda: None)
                s.default(unknown_command)

    except KeyboardInterrupt:
        return ""
    finally:
        print(Fore.BLACK,"Thank you For using FreeWork".center(110," "),end='')
        print()


def welcome(user):
    print(('Hello ' + user).center(110," "))
    print('welcome to FreeWork.'.center(110," "))
    print('Here you can manage your personal to-do list.'.center(110," "))
    print('Here you can manage team task.'.center(110," "))
    print('And many more. Check documentations for more details.'.center(110," "))
    print()

def show_commands():
    print(Fore.BLACK)
    print("[p] Checkout your personal workspace")
    print("[o] Checkout your office workspace")
    print("[e] or ctrl-c to exit")
    print()


if __name__ == '__main__':
    kwargs = OptParser.parseopts()
    main(kwargs)

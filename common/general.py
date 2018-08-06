from colorama import Fore

def get_action(user):
    text = '> '
    if user:
        text = f'{user}> '
    action = input(Fore.YELLOW + text + Fore.WHITE)
    return action.strip().lower()



def unknown_command():
    print(Fore.BLACK,"Sorry we didn't understand that command.")

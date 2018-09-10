

def create_task(user):
    print(' ****************** Create Task **************** ')
    title = input("Please enter title for task ")
    description = input("Please enter description for task ")
    title = input("Please enter title for task ")


def backlog(user)):
    pass

def completed_task(user)):
    pass

def in_progress(user)):
    pass

def log_work(user)):
    pass

def change_password(user)):
    pass


def register_cage():
    if not state.active_account:
        error_msg('You must login first to register a cage.')
        return

    meters = input('How many square meters is the cage? ')
    if not meters:
        error_msg('Cancelled')
        return

    meters = float(meters)
    carpeted = input("Is it carpeted [y, n]? ").lower().startswith('y')
    has_toys = input("Have snake toys [y, n]? ").lower().startswith('y')
    allow_dangerous = input("Can you host venomous snakes [y, n]? ").lower().startswith('y')
    name = input("Give your cage a name: ")
    price = float(input("How much are you charging?  "))

    cage = svc.register_cage(
        state.active_account, name,
        allow_dangerous, has_toys, carpeted, meters, price
    )

    state.reload_account()
    success_msg(f'Register new cage with id {cage.id}.')

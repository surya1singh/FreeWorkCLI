from colorama import Fore
from option_parser import OptParser



def main(kwargs):
    user = kwargs['username']
    if not login_user(kwargs['username'],kwargs['password']):
        raise ValueError("Incorrect User/password")
    try:
        welcome(user)
        while True:
            print("[p] Checkout your personal workspace")
            print("[o] Checkout your office workspace")
            print("[e] or ctrl-c to exit")
            print()
            choice = input("Go to [p]ersonal or [o]ffice tasks? ").lower().strip()
            if choice == 'p':
                Personal(user)
            if choice == 'o':
                Office(user)
            if choice == 'e':
                raise KeyboardInterrupt()
    except KeyboardInterrupt:
        print("Thank you For using FreeWork".center(110," "))
        return ""



def login_user(user, password):
    if user == 'surya' and password == 'surya':
        return True



def welcome(user):
    print(('Hello ' + user).center(110," "))
    print('welcome to FreeWork.'.center(110," "))
    print('Here you can manage your personal to-do list.'.center(110," "))
    print('Here you can manage team task.'.center(110," "))
    print('And many more. Check documentations for more details.'.center(110," "))





if __name__ == '__main__':
    kwargs = OptParser.parseopts()
    main(kwargs)

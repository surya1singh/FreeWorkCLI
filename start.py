from colorama import Fore
from option_parser import OptParser


def main(kwargs):
    if not check_user(kwargs['username'],kwargs['password']):
        raise ValueError("Incorrect User/password")
    try:
        while True:
            pass
            break
    except KeyboardInterrupt:
        return ""

def check_user(user, password):
    if user == 'surya' and password == 'surya':
        return True



def welcome():
    pass



if __name__ == '__main__':
    kwargs = OptParser.parseopts()
    main(kwargs)

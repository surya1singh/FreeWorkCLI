from db.user import User

active_account: User = None


def reload_account():
    global active_account
    if not active_account:
        return

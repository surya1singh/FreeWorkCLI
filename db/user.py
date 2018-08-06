import datetime
import mongoengine


class User(mongoengine.Document):
    id = mongoengine.IntField()
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    team = mongoengine.StringField(required=False)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }


def login_user(user, password):
    if user == 'surya' and password == 'surya':
        return user

def change_password(user):
    pass

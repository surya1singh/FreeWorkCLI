

tasks = [
    {
        'id': 1,
        'title': u'Create FreeWorkCLI',
        'status': u'In progress',
        'estimated_time': 10,
        'time_spent' : 0
    }
]


import mongoengine


class Tasks(mongoengine.Document):
    id = mongoengine.IntField()
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    team = mongoengine.StringField(required=False)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }

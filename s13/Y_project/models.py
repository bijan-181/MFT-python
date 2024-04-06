from peewee import *


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('Y.db')


class Users(BaseModel):
    username = CharField(max_length=32, unique = True, index = True)
    password = CharField(max_length=32)
    first_name = CharField(max_length=64)
    last_name = CharField(max_length=64,null=True)
    bio = TextField(null=True)
    admin = BooleanField()


class Posts(BaseModel):
    author = ForeignKeyField(Users, backref='posts', on_delete='CASCADE')
    text = TextField()
    time = DateTimeField()
    like = IntegerField()

from models import Users, Posts
from peewee import *


db = SqliteDatabase('Y.db')

db.connect()
db.create_tables([Users, Posts])

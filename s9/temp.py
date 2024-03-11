import json
from datetime import datetime
import time


class User:
    def __init__(
            self, username, password,
            fname, lname, bio, admin) -> None:
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.bio = bio
        self.admin = admin

    def to_dict(self):
        d = {self.username: {
            "password": self.password,
            "name": {
                "first_name": self.fname,
                "last_name": self.lname
            },
            "bio": self.bio,
            "admin": self.admin
        }}
        return d
    def __str__(self):
        return f'{self.username} - {self.fname} {self.lname}'


__user_path = 's9/user.json'
__post_path = 's9/post.json'

with open(__user_path, 'r') as f:
    users = json.load(f)
with open(__post_path, 'r') as f:
    posts = json.load(f)

user_list = []

for username, data in users.items():
    tempuser = User(username, data['password'], data['name']['first_name'],
                    data['name']['last_name'], data['bio'], data['admin'])
    user_list.append(tempuser)

for i in user_list:
    print(type(i))
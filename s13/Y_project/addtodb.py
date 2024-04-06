from models import Users, Posts
import json

__user_path = 's13/Y_project/user.json'
__post_path = 's13/Y_project/post.json'

with open(__user_path, 'r') as f:
    users = json.load(f)
with open(__post_path, 'r') as f:
    posts = json.load(f)

for i in users:
    Users.create(
        username=i,
        password=users[i]['password'],
        first_name=users[i]['name']['first_name'],
        last_name=users[i]['name']['last_name'],
        bio=users[i]['bio'],
        admin=users[i]['admin'],
    )

for i in posts:
    Posts.create(
        author = Users.select().where(Users.username == posts[i]['author']).get(),
        text = posts[i]['text'],
        time = posts[i]['time'],
        like = posts[i]['like']
    )

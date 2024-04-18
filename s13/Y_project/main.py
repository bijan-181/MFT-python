from datetime import datetime
import time
from models import Users, Posts




def register_user():
    while True:
        User_username = input('username: ')
        if not Users.select().where(Users.username == User_username).exists():
            User_password = input('password: ')
            User_fname = input("first name: ")
            User_lname = input("last name")
            User_bio = input('bio: ')
            User_admin = input('is admin: ')
            User_admin = True if User_admin == 'YES' else False
            Users.create(
                username=User_username,
                password=User_password,
                first_name=User_fname,
                last_name=User_lname,
                bio=User_bio,
                admin=User_admin
            )
            break
        else:
            print('this username is exist. pleas enter an other one.')


def show_users():
    for i in Users.select():
        print('/\\/\\/\\/\\/\\/\\/\\/\\/\n')
        user_show = [
            f"{i.username} - {i.first_name} {i.last_name}",
            f"bio: {i.bio}"]
        print('\n\n'.join(user_show))


def show_post():
    for i in Posts.select():
        print('/\\/\\/\\/\\/\\/\\/\\/\\/\n')
        t = datetime.fromtimestamp(i.time).strftime('%Y-%m-%d %H:%M')
        post_show = [
            f"{i.author.username}",
            f"{i.text}",
            f"{t} - {i.like}"
        ]
        print('\n\n'.join(post_show))


def add_post(author):
    post_text = input('enter your post : ')
    Posts.create(
        author = author,
        text = post_text,
        time = time.time(),
        like = 0
    )


def banner(user):
    s = ['----------------------------', 'be Y khosh amadid',
         '1.', '2. add post', '3. show posts', '4. show users', '5. logout', '0. exit']
    if user.admin:
        s.insert(7, "6. register user")
    s = '\n'.join(s)
    while True:
        print(s)
        menu_input = input('enter your input: ')
        if menu_input == '1':
            pass
        elif menu_input == '2':
            add_post(user)
        elif menu_input == '3':
            show_post()
        elif menu_input == '4':
            show_users()
        elif menu_input == '5':
            return -1
        elif menu_input == '6' and user.admin:
            register_user()
        elif menu_input == '0':
            return 0


def login():
    Username = input('username : ')
    password = input('password : ')
    user = Users.select().where(Users.username == Username)
    if user.exists():
        u = user.get()
        if u.password == password:
            print('login success')
            stat = banner(u)
            if stat == -1:
                return
            elif stat == 0:
                exit()
        else:
            print('invalid username or password')
    else:
        print('invalid username or password')


while True:
    login()
    print('loging out')

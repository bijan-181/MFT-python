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
        d = {self.username:{
        "password": self.password,
        "name": {
            "first_name": self.fname,
            "last_name": self.lname
        },
        "bio": self.bio,
        "admin": self.admin
        }}
        return d

usr = User('bijan','123','bijan','ahmadi','i am here',True)
a = []
a.append(usr)
usr2 = User('mmd','234','mohammad','mirzaee','i am not here',False)
a.append(usr2)
for i in a :
    print(i.username)
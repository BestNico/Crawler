from iuuuu.sdfsdf import session
from iuuuu.sdfsdf import User
import pymysql

pymysql.install_as_MySQLdb()

user = User()
user.name = "Guo"
session.add(user)
session.commit()

users = session.query(User).all()
for user in users:
    print(user.name)


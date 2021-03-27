from data import db_session
from data.users import User

db_session.global_init("db/mars_explorer.db")
db_sess = db_session.create_session()
for user in db_sess.query(User):
    print(user)

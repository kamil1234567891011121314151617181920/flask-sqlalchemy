from data import db_session
from data.users import User
from data.jobs import Jobs
from random import choice, randint


def add_jobs():
    users_id = list(map(lambda x: x.id, db_sess.query(User)))
    for i in range(22, 25):
        job = Jobs()
        job.team_leader = choice(users_id)
        job.job = f"test_work{i}"
        job.work_size = randint(5, 16)
        tmp = choice(users_id)
        while tmp == job.team_leader:
            tmp = choice(users_id)
        job.collaborators = f'{job.team_leader}, {tmp}'
        job.is_finished = choice([False, True])
        db_sess.add(job)


def add_users():
    for el in [('Scott', 'Ridley', 21, 'captain', 'research engineer',
                'module_1', 'scott_chief@mars.org'),
               ('Andy', 'Weir', 20, 'member', 'pilot',
                'module_2', 'andy_chief@mars.org'),
               ('Watney', 'Mark', 20, 'member', 'navigator',
                'module_3', 'watney_mark_chief@mars.org'),
               ('Bean', 'Sean', 23, 'member', 'doctor',
                'module_6', 'bin1sean1@mars.org'),
               ('Kapoor', 'Venkat', 19, 'member', 'doctor',
                'module_1', 'venkat@mars.org'),
               ('test1', 'test1', 17, 'member', 'test',
                'module_4', 'test1@mars.org'),
               ('test2', 'test2', 18, 'member', 'test',
                'module_2', 'test2@mars.org')]:
        # print(list(db_sess.query(User).filter(User.email == el[-1])))
        if db_sess.query(User).filter(User.email == el[-1]).first():
            continue  # если уже добавили
        print(el[-1])
        user = User()
        user.surname, user.name, user.age, user.position, \
            user.speciality, user.address, user.email = el
        db_sess.add(user)


if __name__ == '__main__':
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    add_jobs()
    db_sess.commit()

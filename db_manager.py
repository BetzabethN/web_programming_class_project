# NARVAEZ BETZABETH 2018106117

from app import db, Role, User, Post

if __name__ == '__main__':
    db.create_all()
    admin_role = Role(name='Admin')
    mod_role = Role(name='Moderator')
    user_role = Role(name='User')
    user_john = User(username='john', role=admin_role)
    user_susan = User(username='susan', role=user_role)
    user_david = User(username='david', role=user_role)

    db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])
    # print(admin_role.id)
    # db.session.commit()
    # print(admin_role.id)

    admin_role.name = 'Adminstrator'
    db.session.add(admin_role)
    # db.session.commit()

    # db.session.delete(mod_role)
    # db.session.commit()

    # joined = User.query.join(Role\
    #                          .add_columns(User.id, User.username, User.role_id, Role.name)\
    #                          .filter(User.role))

    bp_ex1 = Post(body='example 1', title="example 1", user_id=user_john.id)
    bp_ex2 = Post(body='example 2', title="example 2", user_id=user_david.id)
    bp_ex3 = Post(body='example 3', title="example 3",  user_id=user_susan.id)
    db.session.add_all([bp_ex1, bp_ex2, bp_ex3])
    db.session.commit()


    # print(Role.query.all())
    # print(User.query.all())
    # print(User.query.filter_by(role=user_role).all())
    # print(str(User.query.filter_by(role=user_role)))
    #
    # user_role = Role.query.filter_by(name='User').first()
    # print(user_role)
    # users = user_role.users
    # print(users)
    # print(users[0].role)
    # print(user_role.users.order_by(User.username).all())
    # print(user_role.users.count())

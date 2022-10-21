from DataBase.controllers.controllers import UserController
controller = UserController()
# import logging
#
# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# log = logging.getLogger('my-logger')


def main() -> bytes:
    # user = controller.create_user('Elena', 'Index21@gmail.com', '31515ggh')
    controller.update_user_field(id_=1, name='Timmi', email='did51Cycle@gmail.com')
    users_lim, count = controller.get_limit_users(limit=5, offset=0, mode=True)
    print(f'General count : {count}')

    users = controller.get_all_users()
    print('list users:')
    for user in users_lim:
        print(f'id: {user.id} name: {user.username} email: {user.email} password: {user.password}')
    return b'string'


if __name__ == "__main__":
    string = main()
    print(string)

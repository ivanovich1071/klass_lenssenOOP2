class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)

    def remove_user(self, user):
        self.__user_list.remove(user)

    def get_user_list(self):
        return self.__user_list


user1 = User(1, 'Павел')
user2 = User(2, 'Иван')
user3 = User(3, 'Игорь')
admin1 = Admin(101, 'Admin1')

# Добавляем пользователей в список администратора
admin1.add_user(user1)
#admin1.add_user(user2)

# Просмотр списка пользователей администратора
user_list = admin1.get_user_list()
for user in user_list:
    print(user.get_user_id(), user.get_name(), user.get_access_level())
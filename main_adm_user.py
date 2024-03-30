class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = 'user'

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__access_level = 'admin'
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)   # добавление пользователя

    def remove_user(self, user):
        self.__user_list.remove(user)   # улаление пользователя

    def get_user_list(self):
        return self.__user_list

class Docs:
    def __init__(self, name, doc_type, access_level):
        self.name = name
        self.doc_type = doc_type
        self.access_level = access_level

users = []
admins = []
docs_list = []

while True:
    user_input = input("Введите данные сотрудника (user_id, name) или введите 'end' для выхода:")
    if user_input.lower() == 'end':
        break
    user_id, name = user_input.split(', ')
    users.append(User(int(user_id), name))

print("Список всех сотрудников:")
for user in users:
    print(user.get_user_id(), user.get_name(), user.get_access_level())

print("\nВыберите администраторов:")
for user in users:
    print(user.get_user_id(), user.get_name())
choice = input("\nВведите ID администраторов через пробел:")
admin_ids = list(map(int, choice.split()))
admins = [user for user in users if user.get_user_id() in admin_ids]

print("\nСписок администраторов:")
for admin in admins:
    print(admin.get_user_id(), admin.get_name(), admin.get_access_level())

print("\nСписок простых пользователей:")
for user in users:
    if user not in admins:
        print(user.get_user_id(), user.get_name(), user.get_access_level())

# Ввод документов и вывод документов доступных только user
print("\nВведите данные документа (название, тип документа, уровень доступа), или введите 'end' для завершения:")
while True:
    doc_input = input()
    if doc_input.lower() == 'end':
        break
    name, doc_type, access_level = doc_input.split(', ')
    docs_list.append(Docs(name, doc_type, access_level))

print("\nДокументы доступные только для пользователей ('user' для обычных сотрудников):")
for doc in docs_list:
    if doc.access_level == 'user':
        print(doc.name, doc.doc_type, doc.access_level)
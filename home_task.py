# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов. У каждого сотрудника
# есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных
# пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс User: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access_level = "user"

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def user_info(self):
        return f"Это приватные сведения о сотруднике: ID - {self.__id}, ФИО - {self.__name}, уровень доступа - {self.__access_level}"

all_users = []

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._User__access_level = "admin"

    def add_user(self, user):
        all_users.append(user)

    def remove_user(self, id):
        for user in all_users:
            if user.get_id() == id:
                all_users.remove(user)

employee1 = User("007", "James Bond")
print(employee1.user_info())

employee2 = Admin("001", "Super Mario")
print(employee2.user_info())
class Car:
    def __init__(self, vendor, model):
        self.public_vendor = vendor # Публичный атрибут
        self._protected_model = model # Защищённый атрибут
        self.__private_year = 2022 # Приватный атрибут

    def public_method(self):
        return f"Это открытый метод. Машина: {self.public_vendor} {self._protected_model}"

    def _protected_method(self):
        return f"Это защищённый метод."

    def __private_method(self):
        return f"Это приватный метод."

class ElectroCar(Car):
    def __init__(self, vendor, model, battery_size):
        super().__init__(vendor, model)
        self.battery_size = battery_size

    def get_details(self):
        # Можно обратиться к открытому и защищенному методу, но не приватному
        details = f"{self.public_vendor} {self._protected_model}, Батарея: {self.battery_size} kWh "
        # Нельзя напрямую обратиться к __private_method и __private_year
        return details

# Создание экземпляра ElectroCar
tesla = ElectroCar("Tesla", "Model S", 100)

# Доступ к открытому атрибуту и методу
print(tesla.public_vendor)
print(tesla.public_method())

# Доступ к защищённому методу (не рекомендуется, но возможно)
print(tesla._protected_model)
print(tesla._protected_method())

# Доступ к приватному атрибуту и методу невозможен, но Python позволяет обойти это ограничение (не рекомендуется)
print(tesla._Car__private_year) # Доступ к приватному атрибуту через mangling
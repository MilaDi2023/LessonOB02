class Test():
    def public_function(self):
        print("Публичный метод")

    def _protected_function(self):
        print("Защищённый метод")

    def __private_function(self):
        print("Приватный метод")

    def test_private(self):
        self.__private_function()

test = Test()
test.public_function()
test._protected_function()
test.test_private()

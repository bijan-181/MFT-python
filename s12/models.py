class Person:
    def __init__(self, first_name, last_name, national_code, birth_location) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.national_code = national_code
        self.birth_location = birth_location
        self._protected = 'protect'
        self.__private = 'private'

    def print_name(self):
        print(self.first_name)
        print(self.last_name)
        print(self.national_code)

    def __str__(self):
        return f"{self.first_name} {self.last_name} from {self.birth_location}"


class Student(Person):
    def __init__(self, first_name, last_name, national_code, birth_location, avg):
        super().__init__(first_name, last_name, national_code, birth_location)
        self.avg = avg
        self._protected = 'change shod'

    def print_name(self):
        print(f'score : {self.avg}')
        super().print_name()


s = Student('bijan', 'ahmadi', '1234567890', 'tehran', 18)
s.print_name()

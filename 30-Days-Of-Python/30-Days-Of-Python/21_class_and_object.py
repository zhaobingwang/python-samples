print('---------- Creating a Class ----------')


class Person:
    pass


print('---------- Creating an Object ----------')
p = Person()
print(p)

print('---------- Class Constructor ----------')


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person('San', 'Zhang', 25, 'China', 'Hangzhou')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
print(p)

print('---------- Object Methods ----------')


class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.lastname} {self.firstname} is {self.age} years old. He lives in {self.city},{self.country}'


p = Person('San', 'Zhang', 25, 'China', 'Hangzhou')
print(p.person_info())

print('---------- Object Default Methods ----------')


class Person:
    def __init__(self, firstname='San', lastname='Zhang', age=25, country='China', city='Hangzhou'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.lastname} {self.firstname} is {self.age} years old. He lives in {self.city},{self.country}'


p1 = Person()
print(p1.person_info())
p2 = Person('Si', 'Li', 30, 'China', 'Shanghai')
print(p2.person_info())

print('---------- Method to Modify Class Default Values ----------')


class Person:
    def __init__(self, firstname='San', lastname='Zhang', age=25, country='China', city='Hangzhou'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.lastname} {self.firstname} is {self.age} years old. He lives in {self.city},{self.country}'

    def add_skill(self, skill):
        self.skills.append(skill)


p = Person()
print(p.person_info())
p.add_skill('Java')
p.add_skill('.NET')
p.add_skill('Python')
print(p.person_info())
print(p.skills)

print('---------- Inheritance ----------')


class Student(Person):
    pass


s1 = Student('Si', 'Li', 30, 'China', 'Shanghai')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('Vue')
s1.add_skill('HTML')
s1.add_skill('CSS')
print(s1.skills)

print('---------- Overriding parent method ----------')


class Student(Person):
    def __init__(self, firstname='San', lastname='Zhang', age=25, country='China', city='Hangzhou', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        if self.gender == 'male':
            gender = 'He'
        else:
            gender = 'She'
        return f'{self.lastname} {self.firstname} is {self.age} years old. {gender} lives in {self.city},{self.country}'


s1 = Student('Si', 'Li', 30, 'China', 'Shanghai', 'male')
print(s1.person_info())

class Student:
    surname = ""
    name = ""
    middleName = ""
    dateOfBirth = ""
    course = ""

    def setOverwritingSurname(self): self.surname = input("Інше прізвище: ")
    def setOverwritingName(self): self.name = input("Інше ім'я: ")
    def setOverwritingMiddleName(self): self.middleName = input("Інше по батькові: ")
    def setOverwritingDateOfBirth(self): self.dateOfBirth = input("Інша дата народження: ")
    def setOverwritingCourse(self): self.course = input("Інший курс: ")

people = Student()
print("Введіть свої дані")
people.surname = input("Прізвище: ")
people.name = input("Ім'я: ")
people.middleName = input("По батькові: ")
people.dateOfBirth = input("Дата народження: ")
people.course = input("Курс: ")

print()
print("Ваші дані:")
print("Прізвище - ", people.surname, sep="")
print("Ім'я - ", people.name, sep="")
print("По батькові - ", people.middleName, sep="")
print("Дата народження - ", people.dateOfBirth, sep="")
print("Курс - ", people.course, sep="")

work = True

while work:
    print()
    print("Що ви хочите змінити?")
    print("1 - Прізвище")
    print("2 - Ім'я")
    print("3 - По батькові")
    print("4 - Дату народження")
    print("5 - Курс")

    menu = int(input("~ "))
    print()

    match menu:
        case 1:
            people.setOverwritingSurname()
            work = False
        case 2:
            people.setOverwritingName()
            work = False
        case 3:
            people.setOverwritingMiddleName()
            work = False
        case 4:
            people.setOverwritingDateOfBirth()
            work = False
        case 5:
            people.setOverwritingCourse()
            work = False
        case _:
            print("Error")

print()
print("Ваші дані:")
print("Прізвище - ", people.surname, sep="")
print("Ім'я - ", people.name, sep="")
print("По батькові - ", people.middleName, sep="")
print("Дата народження - ", people.dateOfBirth, sep="")
print("Курс - ", people.course, sep="")
# import Entities.Student as stu
import Entities.Library as Library
import Entities.Employee as Employee
import Entities.Book as Book
import Entities.Flat as Flat
import Entities.House as House
import Entities.Order as Order
import Entities.Property as Property

from Entities.Student import Student


# Zad.1

def main():
    from Entities.Student import Student
    Magda = Student("Magda", [3, 3, 2, 2, 3, 4, 5, 3, 4])
    Przemek = Student("Przemek", [5, 100, 200, 5, 300, 50])

    print(Magda.is_passed())
    print(Przemek.is_passed())


main()

# Zad.2


def main2():
    library1 = Library("Katowice", "Katowicka", "40-850", "8-16", "646838929")
    library2 = Library("Mikołów", "Mikołowska", "42-850", "8-16", "949383929")
    book1 = Book(library1, "2022-01-01", "Magdalena", "Dąbrowska", "60")
    book2 = Book(library2, "2022-01-01", "Mateusz", "Haręża", "40")
    book3 = Book(library1, "2022-01-01", "Przemysław", "Doktór", "200")
    book4 = Book(library2, "2022-01-01", "Maciej", "Duda", "20")
    book5 = Book(library1, "2022-01-01", "Andrzej", "Duda", "100")
    Magda = Student("Magda", [3, 3, 2, 2, 3, 4, 5, 3, 4])
    Przemek = Student("Przemek", [5, 100, 200, 5, 300, 50])
    employee1 = Employee("Mateusz", "Haręża", '2020-09-09', '1997-12-11', 'Katowice', 'Zawadzka', '50-001', "111444999")
    employee2 = Employee("Maciej", "Duda", '2020-09-09', '2001-12-11', 'Ruda Slaska', 'Opolska', '50-001', "222333444")
    employee3 = Employee("Magdalena", "Dabrowska", '2020-09-09', '2001-12-11', 'Katowice', 'Polska', '50-001', "999888777")
    order1 = Order(employee2, Magda, [book1, book2], "2022-10-17")
    order2 = Order(employee1, Przemek, [book1, book3], '2015-03-04')

    print(order1)
    print(order2)


main2()


# Zad.3

# zadanie 3


def main3():
    prop = Property("Kostuchna", 4, 2000, 'Katowice')
    house = House(prop, '3x4')
    flat = Flat(prop, 12)
    print(house)
    print(flat)


main3()
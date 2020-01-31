# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер,
# ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.


class OfficeEquipmentWarehouse:
    """На складе хранятся принтер , сканер. крсерокс"""
    pass


class OfficeEquipment:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Ваша техника {self.name}\n '

    def __add__(self, other):
        self.name.append(other)


class Printer(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)


class Scanner(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)


class Xerox(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)


printer = Printer('Принтер')
print(printer)
scanner = Scanner('Сканер')
print(scanner)
xerox = Xerox('Ксерокс')
print(xerox)

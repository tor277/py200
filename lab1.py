# TODO Написать 3 класса с документацией и аннотацией типов

class Sneakers:
    def __init__(self, color, size):
        if not isinstance(color, str):
            raise TypeError('Пиши цвет прописью')
        self.color = color

        if not isinstance(size, (int, float)):
            raise TypeError('Размер пишется числом')
        if not 10 < size < 48:
            raise ValueError("Нет такого размера!")
        self.size = size

    def change_color(self, color):
        if not isinstance(color, str):
            raise TypeError('Пиши цвет прописью')
        self.color = color

    def change_size(self, size):
        if not isinstance(size, (int, float)):
            raise TypeError('Размер пишется числом')
        if not 10 < size < 48:
            raise ValueError("Нет такого размера!")
        self.size = size

    def __str__(self):
        return f'Цвет кроссовок = {self.color}, размер = {self.size}'


class Auto:
    def __init__(self, model, disc_diameter):
        if not isinstance(model, str):
            raise TypeError("Модель авто писать прописью!")
        self.model = model

        if not isinstance(disc_diameter, (int, float)):
            raise TypeError("Диаметр должен быть типа int или float")
        if disc_diameter < 13 or disc_diameter > 24:
            raise ValueError("Такие диски на машину не поставить !")
        self.disc_diameter = disc_diameter

    def change_disc_diameter(self, diameter):
        if not isinstance(diameter, (int, float)):
            raise TypeError("Диаметр должен быть типа int или float")
        if not 0 < diameter <= 11:
            raise ValueError("За пределами диапазина установки !")
        if not 13 <= (self.disc_diameter + diameter) <= 24:
            raise ValueError("Такие диски на машину не поставить !")
        self.disc_diameter += diameter

    def change_model(self, model):
        if not isinstance(model, str):
            raise TypeError("Модель авто писать прописью!")
        self.model = model

    def __str__(self):
        return f'Модель машины = {self.model}, диаметр дисков = {self.disc_diameter}'

class Table:
    def __init__(self, type, height):
        if not isinstance(type, str):
            raise TypeError('Пиши тип стола прописью')
        self.type = type

        if not isinstance(height, (int, float)):
            raise TypeError('Размер пишется числом сантиметров')
        if not 50 <= height <= 100:
            raise ValueError("Нет такой высокий стола !")
        self.height = height

    def change_type(self, type):
        if not isinstance(type, str):
            raise TypeError('Пиши тип стола прописью')
        self.type = type

    def up_change_height(self, height):
        if not isinstance(height, (int, float)):
            raise TypeError('Размер пишется числом сантиметров')
        if not 50 <= (self.height + height) <= 100:
            raise ValueError("Нет такой высокий стол, это барная стойка!")
        if not height > 0:
            raise ValueError("Необходимо увеличить высоту, а не уменьшить")
        self.height += height

    def __str__(self):
        return f'Тип стола = {self.type}, высота стола в см = {self.height}'


if __name__ == "__main__":

    print('----Смотрим класс 1 Кроссовки----')
    sneek = Sneakers('Красные', 45)
    print(sneek)
    sneek.change_color('Зеленые')
    sneek.change_size(25)
    print(sneek)

    print('----Смотрим класс 2 Авто----')
    auto = Auto('Мерседес', 20)
    print(auto)
    auto.change_disc_diameter(1)
    auto.change_model('Ситроен')
    print(auto)

    print('----Смотрим класс 3 Стол----')
    table = Table('Обеденный', 50)
    print(table)
    table.change_type('Столярный')
    table.up_change_height(40)
    print(table)



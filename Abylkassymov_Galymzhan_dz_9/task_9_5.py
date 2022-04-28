class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Ручка для письма')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш для рисование')


class Handle(Stationery):
    def draw(self):
        print('Маркер для дизайна')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*


#Створення додатку
app=QApplication([])
win=QWidget()
#Задаємо розмір екрану
win.resize(200,200)
win.setWindowTitle('Тест ГітХаб')
#Створюємо підпис з текстом
title=QLabel('Тестовий додаток для гітХаб')
#Створення ліній
line_h=QHBoxLayout()
line_h.addWidget(title)
#Добавлення ліній в програму
win.setLayout(line_h)

win.show()
app.exec_()

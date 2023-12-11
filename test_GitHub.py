from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app=QApplication([])
win=QWidget()

win.resize(200,200)
win.setWindowTitle('Тест ГітХаб')

title=QLabel('Тестовий додаток для гітХаб')

line_h=QHBoxLayout()
line_h.addWidget(title)

win.setLayout(line_h)

win.show()
app.exec_()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

app=QApplication([])
win=QWidget()

win.resize(500,500)
win.setWindowTitle('WHAT IS LOVRE')

title=QLabel('What is love, baby dont hurt me No more Baby, dont hurt me, dont hurt me No more')


line_h=QHBoxLayout()
line_h.addWidget(title)

win.setLayout(line_h)

win.show()
app.exec_()
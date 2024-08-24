import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit
class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 600, 100)
        self.createui()
    def createui(self):    
        vbox = QVBoxLayout()
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        vbox.addWidget(self.display)
        grid = QGridLayout()
        buttons = [
            " "," ","C","<-",
            " "," "," ","/",
            "7","8","9","*",
            "4","5","6","-",
            "1","2","3","+",
            " ","0",".","="]
        row,col = 0,0
        for text in buttons:
            if text.strip():
                button = QPushButton(text)
                button.clicked.connect(self.on_button_clicked)
                grid.addWidget(button,row,col)
            col+=1
            if col > 3:
                col = 0
                row+=1
        vbox.addLayout(grid)
        self.setLayout(vbox)
        self.applystyle()
    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == "C":
            self.display.clear()
        elif text == "<-":
            result_list = []
            for i in self.display.text():
                result_list.append(i)
            try:
                result_list.pop()
                new_result = "".join(result_list)
                self.display.setText(new_result)
            except Exception as e:
                self.display.setText("")
        elif text == "=":
            try:
                result = eval(self.display.text())            
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("")
        else:
            current_text = self.display.text()
            new_text = current_text+text
            self.display.setText(new_text)
    def applystyle(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2C3E50;
            }
            QLineEdit {
                background-color: #ECF0F1;
                font-size: 24px;
                padding: 10px;
                border: 2px solid #BDC3C7;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #34495E;
                color: white;
                font-size: 18px;
                border: 2px solid #2C3E50;
                border-radius: 10px;
                padding: 15px;
            }
            QPushButton:hover {
                background-color: #1ABC9C;
            }
            QPushButton:pressed {
                background-color: #16A085;
            }
            """)
def main():
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
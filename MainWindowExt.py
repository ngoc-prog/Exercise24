from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import random

from MODULE1.Exercise24.MainWindow import Ui_MainWindow


class MainWindowExt(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lucky Number Game")
        self.setGeometry(100, 100, 409, 352)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.player_money = 100
        self.machine_money = 100


        self.update_money_display()


        self.ui.pushButtonRandom.clicked.connect(self.spin_random)
        self.ui.pushButtonNewGame.clicked.connect(self.new_game)
        self.ui.pushButtonExit.clicked.connect(self.exit_game)

    def update_money_display(self):
        # Cập nhật tiền của người chơi và máy lên UI
        self.ui.labelPlayerMoney.setText(str(self.player_money))
        self.ui.labelMachinemoney.setText(str(self.machine_money))

    def spin_random(self):
        if self.player_money < 30:
            # Nếu người chơi không đủ tiền để chơi
            self.show_message("Không đủ tiền", "Bạn cần ít nhất 30 đồng để chơi!")
            return

        # Trừ 30 đồng của người chơi
        self.player_money -= 30
        self.machine_money += 30
        self.update_money_display()

        # Random 3 con số
        number1 = random.randint(0, 8)  # Số cho hộp 1 (từ 0 đến 8)
        number2 = random.randint(0, 9)  # Số cho hộp 2 (từ 0 đến 9)
        number3 = random.randint(0, 10)  # Số cho hộp 3 (từ 0 đến 10)

        # Hiển thị các con số trên UI
        self.ui.labelNumber1.setText(str(number1))
        self.ui.labelNumber2.setText(str(number2))
        self.ui.labelNumber3.setText(str(number3))

        # Kiểm tra nếu có con số 7
        if number1 == 7:
            self.player_money += 100 + 0.5 * self.machine_money
            self.machine_money -= 0.5 * self.machine_money
        if number2 == 7:
            self.player_money += 30 + 0.5 * self.machine_money
            self.machine_money -= 0.5 * self.machine_money
        if number3 == 7:
            self.player_money += 10

        # Cập nhật giao diện tiền sau khi chơi
        self.update_money_display()

    def new_game(self):
        # Khởi động lại trò chơi
        self.player_money = 100
        self.machine_money = 100
        self.ui.labelNumber1.setText("")
        self.ui.labelNumber2.setText("")
        self.ui.labelNumber3.setText("")
        self.update_money_display()

    def exit_game(self):
        # Thoát ứng dụng
        self.close()

    def show_message(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()


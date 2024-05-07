import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow
from social import Ui_Dialog
from students import Students
from social_formate import Social_formate

class AutoFiller(QMainWindow):
    def __init__(self):
        super(AutoFiller, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stud = Students()
        self.ui.newStudent_btn.clicked.connect(self.open_new_student)
        self.ui.savePDF_btn.clicked.connect(self.save_docx)
    def open_new_student(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.saveData_btn.clicked.connect(self.add_new_info)
    def add_new_info(self):
        course = self.ui_window.course_data.text()
        group = self.ui_window.group_data.text()
        firstName = self.ui_window.firstName_data.text()
        secondName = self.ui_window.secondName_data.text()
        middleName = self.ui_window.middleName_data.text()
        certNum = self.ui_window.certNum_data.text()
        certDate = self.ui_window.certDate_data.text()
        curDate = self.ui_window.curDate_data.text()
        self.ui.chooseStudent_combobox.addItem(firstName)
        self.stud.addInfo(course, group, firstName, secondName, middleName, certNum, certDate, curDate)
        self.debug()
        self.new_window.close()
    def save_docx(self):
        self.Social_formate = Social_formate(self.stud)
        self.Social_formate.changeDocx()
        self.stud.debug()
    def debug(self):
        self.stud.debug()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutoFiller()
    window.show()

    sys.exit(app.exec())
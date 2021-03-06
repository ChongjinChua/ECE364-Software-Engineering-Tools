import sys

from PySide.QtGui import *
from BasicUI import *
import re


class Consumer(QMainWindow, Ui_MainWindow):

    states = ["AK", "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)

        self.regex = r"<[A-Za-z]+>([A-Za-z0-9/@/./, ]+)<[//A-Za-z]+>"
        self.emailregex = r"\w+@\w+\.\w+"
        self.firstname_var = ""
        self.lastname_var = ""
        self.address_var = ""
        self.city_var = ""
        self.state_var = ""
        self.zip_var = ""
        self.email_var = ""
        self.error_var = ""

        self.clearButton.clicked.connect(self.reset)
        self.loadButton.clicked.connect(self.loadData)
        self.saveToTargetButton.clicked.connect(self.saveData)

        self.firstNameLineEdit.textChanged.connect(self.textStatus)
        self.lastNameLineEdit.textChanged.connect(self.textStatus)
        self.addressLineEdit.textChanged.connect(self.textStatus)
        self.cityLineEdit.textChanged.connect(self.textStatus)
        self.stateLineEdit.textChanged.connect(self.textStatus)
        self.zipLineEdit.textChanged.connect(self.textStatus)
        self.emailLineEdit.textChanged.connect(self.textStatus)

    def saveData(self):
        error_flag = 0
        zip_error = 0
        zip_str = self.zipLineEdit.text()
        if len(zip_str) != 5:
            zip_error = 1
        else:
            for i in zip_str:
                if not i.isdigit():
                    zip_error = 1

        mail_valid = re.search(self.emailregex,self.emailLineEdit.text())

        if self.firstNameLineEdit.text() == "" or self.lastNameLineEdit.text() == "" or self.addressLineEdit.text() == "" or self.cityLineEdit.text() == "" or self.stateLineEdit.text() == "" or self.zipLineEdit.text() == "" or self.emailLineEdit.text() == "":
            self.error_var = "Error: Please populate all fields!"
            error_flag = 1
        elif self.stateLineEdit.text() not in self.states:
            self.error_var = "Error: State is not valid!"
            error_flag = 1
        elif zip_error:
            self.error_var = "Error: ZIP is not valid!"
            error_flag = 1
        elif not mail_valid:
            self.error_var = "Error: Email in not valid!"
            error_flag = 1

        self.firstname_var = self.firstNameLineEdit.text()
        self.lastname_var = self.lastNameLineEdit.text()
        self.address_var = self.addressLineEdit.text()
        self.city_var = self.cityLineEdit.text()
        self.state_var = self.stateLineEdit.text()
        self.zip_var = self.zipLineEdit.text()
        self.email_var = self.emailLineEdit.text()

        if not error_flag:
            self.error_var = ""
            fptr = open('target.xml','w')
            fptr.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            fptr.write('<user>\n')
            fptr.write('\t<FirstName>{0}</FirstName>\n'.format(self.firstname_var))
            fptr.write('\t<LastName>{0}</LastName>\n'.format(self.lastname_var))
            fptr.write('\t<Address>{0}</Address>\n'.format(self.address_var))
            fptr.write('\t<City>{0}</City>\n'.format(self.city_var))
            fptr.write('\t<State>{0}</State>\n'.format(self.state_var))
            fptr.write('\t<ZIP>{0}</ZIP>\n'.format(self.zip_var))
            fptr.write('\t<Email>{0}</Email>\n'.format(self.email_var))
            fptr.write('</user>\n')


        self.display()



    def textStatus(self):
        '''
        self.firstname_var = self.firstNameLineEdit.text()
        self.lastname_var = self.lastNameLineEdit.text()
        self.address_var = self.addressLineEdit.text()
        self.city_var = self.cityLineEdit.text()
        self.state_var = self.stateLineEdit.text()
        self.zip_var = self.zipLineEdit.text()
        self.email_var = self.emailLineEdit.text()
        '''

        if self.firstNameLineEdit.text() == "" and self.lastNameLineEdit.text() == "" and self.addressLineEdit.text() == "" and self.cityLineEdit.text() == "" and self.stateLineEdit.text() == "" and self.zipLineEdit.text() == "" and self.emailLineEdit.text() == "":
            self.loadButton.setEnabled(1)
            self.saveToTargetButton.setDisabled(1)
        else:
            self.loadButton.setDisabled(1)
            self.saveToTargetButton.setEnabled(1)


    def reset(self):

        self.firstname_var = ""
        self.lastname_var = ""
        self.address_var = ""
        self.city_var = ""
        self.state_var = ""
        self.zip_var = ""
        self.email_var = ""
        self.error_var = ""

        self.firstNameLineEdit.setText(self.firstname_var)
        self.lastNameLineEdit.setText(self.lastname_var)
        self.addressLineEdit.setText(self.address_var)
        self.cityLineEdit.setText(self.city_var)
        self.stateLineEdit.setText(self.state_var)
        self.zipLineEdit.setText(self.zip_var)
        self.emailLineEdit.setText(self.email_var)
        self.errorInfoLabel.setText(self.error_var)

        self.loadButton.setEnabled(1)
        self.saveToTargetButton.setDisabled(1)


    def display(self):
        self.firstNameLineEdit.setText(self.firstname_var)
        self.lastNameLineEdit.setText(self.lastname_var)
        self.addressLineEdit.setText(self.address_var)
        self.cityLineEdit.setText(self.city_var)
        self.stateLineEdit.setText(self.state_var)
        self.zipLineEdit.setText(self.zip_var)
        self.emailLineEdit.setText(self.email_var)
        self.errorInfoLabel.setText(self.error_var)

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.

        *** This method is required for unit tests! ***
        """
        with open(filePath,'r') as fptr:
            all_lines = fptr.readlines()

        info_lst = []
        for line in all_lines[2:9]:
            info = re.findall(self.regex,line)
            if info:
                info_lst.extend(info)
            else:
                info_lst.append("")

        print(info_lst)

        self.firstname_var = info_lst[0]
        self.lastname_var = info_lst[1]
        self.address_var = info_lst[2]
        self.city_var = info_lst[3]
        self.state_var = info_lst[4]
        self.zip_var = info_lst[5]
        self.email_var = info_lst[6]
        self.error_var = ""

        self.display()

        self.loadButton.setDisabled(1)
        pass

    def loadData(self):
        """
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        *** DO NOT MODIFY THIS METHOD! ***
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()

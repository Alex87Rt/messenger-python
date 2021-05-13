from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(662, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10,
                                               601, 71))
        self.groupBox.setObjectName("groupBox")
        self.label_username_key = QtWidgets.QLabel(self.groupBox)
        self.label_username_key.setGeometry(QtCore.QRect(20, 20,
                                                         61, 16))
        self.label_username_key.setObjectName("label_username_key")
        self.label_server_ip_key = QtWidgets.QLabel(self.groupBox)
        self.label_server_ip_key.setGeometry(QtCore.QRect(260, 20,
                                                          61, 16))
        self.label_server_ip_key.setObjectName("label_server_ip_key")
        self.label_server_port_key = QtWidgets.QLabel(self.groupBox)
        self.label_server_port_key.setGeometry(QtCore.QRect(520, 20,
                                                            61, 16))
        self.label_server_port_key.setObjectName("label_server_port_key")
        self.label_username_val = QtWidgets.QLabel(self.groupBox)
        self.label_username_val.setGeometry(QtCore.QRect(20, 40,
                                                         121, 16))
        self.label_username_val.setObjectName("label_username_val")
        self.label_server_ip_val = QtWidgets.QLabel(self.groupBox)
        self.label_server_ip_val.setGeometry(QtCore.QRect(260, 40,
                                                          121, 16))
        self.label_server_ip_val.setObjectName("label_server_ip_val")
        self.label_server_port_val = QtWidgets.QLabel(self.groupBox)
        self.label_server_port_val.setGeometry(QtCore.QRect(520, 40,
                                                            51, 16))
        self.label_server_port_val.setObjectName("label_server_port_val")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 240,
                                                 201, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_add_contact = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_add_contact.setGeometry(QtCore.QRect(10, 20,
                                                           131, 21))
        self.lineEdit_add_contact.setObjectName("lineEdit_add_contact")
        self.pushButton_add_contact = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_add_contact.setGeometry(QtCore.QRect(150, 20,
                                                             41, 21))
        self.pushButton_add_contact.setObjectName("pushButton_add_contact")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 300, 201, 371))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_delete_contact = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_delete_contact.setGeometry(QtCore.QRect(10, 340,
                                                                121, 21))
        self.pushButton_delete_contact.setObjectName("pushButton_del_contact")
        self.listWidget_contacts = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_contacts.setGeometry(QtCore.QRect(10, 20,
                                                          181, 311))
        self.listWidget_contacts.setObjectName("listWidget_contacts")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(250, 420,
                                                 381, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.textEdit_input = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_input.setGeometry(QtCore.QRect(10, 20,
                                                     301, 81))
        self.textEdit_input.setObjectName("textEdit_input")
        self.pushButton_send = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_send.setGeometry(QtCore.QRect(320, 20,
                                                      51, 23))
        self.pushButton_send.setObjectName("pushButton_send")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 90,
                                                 381, 321))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser_messages = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_messages.setGeometry(QtCore.QRect(10, 20,
                                                           361, 291))
        self.textBrowser_messages.setObjectName("textBrowser_messages")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(250, 540, 381, 131))
        self.groupBox_6.setObjectName("groupBox_6")
        self.textBrowser_service_info = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser_service_info.setEnabled(True)
        self.textBrowser_service_info.setGeometry(QtCore.QRect(10, 20,
                                                               361, 101))
        self.textBrowser_service_info.setObjectName("textBrowser_service_info")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 90,
                                                 201, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_server_ip = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_server_ip.setGeometry(QtCore.QRect(10, 80,
                                                         111, 20))
        self.lineEdit_server_ip.setObjectName("lineEdit_server_ip")
        self.lineEdit_server_port = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_server_port.setGeometry(QtCore.QRect(10, 110,
                                                           111, 20))
        self.lineEdit_server_port.setObjectName("lineEdit_server_port")
        self.pushButton_connect = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_connect.setGeometry(QtCore.QRect(130, 80,
                                                         61, 21))
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.lineEdit_username = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_username.setGeometry(QtCore.QRect(10, 20,
                                                        181, 20))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_password.setEnabled(True)
        self.lineEdit_password.setGeometry(QtCore.QRect(10, 50,
                                                        181, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.pushButton_disconnect = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_disconnect.setGeometry(QtCore.QRect(130, 110,
                                                            61, 21))
        self.pushButton_disconnect.setObjectName("pushButton_disconnect")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0,
                                              662, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "Messenger"))
        self.groupBox.setTitle(_translate("MainWindow",
                                          "Parameters"))
        self.label_username_key.setText(_translate("MainWindow",
                                                   "User name:"))
        self.label_server_ip_key.setText(_translate("MainWindow",
                                                    "Server IP:"))
        self.label_server_port_key.setText(_translate("MainWindow",
                                                      "Server port:"))
        self.label_username_val.setText(_translate("MainWindow",
                                                   "User"))
        self.label_server_ip_val.setText(_translate("MainWindow",
                                                    "127.0.0.1"))
        self.label_server_port_val.setText(_translate("MainWindow",
                                                      "65789"))
        self.groupBox_2.setTitle(_translate("MainWindow",
                                            "Add contact"))
        self.pushButton_add_contact.setText(_translate("MainWindow",
                                                       "Add"))
        self.groupBox_3.setTitle(_translate("MainWindow",
                                            "Contacts"))
        self.pushButton_delete_contact.setText(_translate("MainWindow",
                                                          "Delete "
                                                          "selected contact"))
        self.groupBox_4.setTitle(_translate("MainWindow",
                                            "Input"))
        self.textEdit_input.setPlaceholderText(_translate("MainWindow",
                                                          "Type your "
                                                          "message here"))
        self.pushButton_send.setText(_translate("MainWindow",
                                                "Send"))
        self.groupBox_5.setTitle(_translate("MainWindow",
                                            "Messages"))
        self.groupBox_6.setTitle(_translate("MainWindow",
                                            "Service info"))
        self.groupBox_7.setTitle(_translate("MainWindow",
                                            "Connection"))
        self.lineEdit_server_ip.setText(_translate("MainWindow",
                                                   "127.0.0.1"))
        self.lineEdit_server_ip.setPlaceholderText(_translate("MainWindow",
                                                              "Server IP"))
        self.lineEdit_server_port.setText(_translate("MainWindow",
                                                     "8006"))
        self.lineEdit_server_port.setPlaceholderText(_translate("MainWindow",
                                                                "Server port"))
        self.pushButton_connect.setText(_translate("MainWindow",
                                                   "Connect"))
        self.lineEdit_username.setText(_translate("MainWindow",
                                                  "TestUser"))
        self.lineEdit_username.setPlaceholderText(_translate("MainWindow",
                                                             "User name"))
        self.lineEdit_password.setText(_translate("MainWindow",
                                                  "TestPassword"))
        self.lineEdit_password.setPlaceholderText(_translate("MainWindow",
                                                             "Password"))
        self.pushButton_disconnect.setText(_translate("MainWindow",
                                                      "Disconnect"))

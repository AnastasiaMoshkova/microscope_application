
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("App")
        Dialog.resize(1001, 800)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 981, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_moving = QtWidgets.QWidget()
        self.tab_moving.setObjectName("tab_moving")
        self.groupBox_parameters = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_parameters.setGeometry(QtCore.QRect(0, 10, 291, 181))
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        self.label_X = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_X.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label_X.setObjectName("label_X")
        self.label_Y = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_Y.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_Y.setObjectName("label_Y")
        self.label_Z = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_Z.setGeometry(QtCore.QRect(30, 120, 55, 16))
        self.label_Z.setObjectName("label_Z")
        self.label_Speed = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_Speed.setGeometry(QtCore.QRect(90, 10, 55, 16))
        self.label_Speed.setObjectName("label_Speed")
        self.label_acceleration = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_acceleration.setGeometry(QtCore.QRect(190, 10, 61, 16))
        self.label_acceleration.setObjectName("label_acceleration")
        self.textEdit_Zacc = QtWidgets.QTextEdit(self.groupBox_parameters)
        self.textEdit_Zacc.setGeometry(QtCore.QRect(170, 120, 91, 31))
        self.textEdit_Zacc.setObjectName("textEdit_Zacc")
        self.textEdit_Xspeed = QtWidgets.QTextEdit(self.groupBox_parameters)
        self.textEdit_Xspeed.setGeometry(QtCore.QRect(60, 40, 91, 31))
        self.textEdit_Xspeed.setObjectName("textEdit_Xspeed")
        self.textEdit_Xacc = QtWidgets.QTextEdit(self.groupBox_parameters)
        self.textEdit_Xacc.setGeometry(QtCore.QRect(170, 40, 91, 31))
        self.textEdit_Xacc.setObjectName("textEdit_Xacc")
        self.textEdit_Yspeed = QtWidgets.QTextEdit(self.groupBox_parameters)
        self.textEdit_Yspeed.setGeometry(QtCore.QRect(60, 80, 91, 31))
        self.textEdit_Yspeed.setObjectName("textEdit_Yspeed")
        self.textEdit_Zspeed = QtWidgets.QTextEdit(self.groupBox_parameters)
        self.textEdit_Zspeed.setGeometry(QtCore.QRect(60, 120, 91, 31))
        self.textEdit_Zspeed.setObjectName("textEdit_Zspeed")
        self.textEdit_Yacc = QtWidgets.QTextEdit(self.groupBox_parameters)
        self.textEdit_Yacc.setGeometry(QtCore.QRect(170, 80, 91, 31))
        self.textEdit_Yacc.setObjectName("textEdit_Yacc")
        self.groupBox_moving = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_moving.setGeometry(QtCore.QRect(300, 10, 171, 181))
        self.groupBox_moving.setObjectName("groupBox_moving")
        self.radioButton_X = QtWidgets.QRadioButton(self.groupBox_moving)
        self.radioButton_X.setGeometry(QtCore.QRect(20, 40, 95, 20))
        self.radioButton_X.setText("")
        self.radioButton_X.setObjectName("radioButton_X")
        self.radioButton_Y = QtWidgets.QRadioButton(self.groupBox_moving)
        self.radioButton_Y.setGeometry(QtCore.QRect(20, 80, 95, 20))
        self.radioButton_Y.setText("")
        self.radioButton_Y.setObjectName("radioButton_Y")
        self.radioButton_Z = QtWidgets.QRadioButton(self.groupBox_moving)
        self.radioButton_Z.setGeometry(QtCore.QRect(20, 120, 95, 20))
        self.radioButton_Z.setText("")
        self.radioButton_Z.setObjectName("radioButton_Z")
        self.pushButton_move = QtWidgets.QPushButton(self.groupBox_moving)
        self.pushButton_move.setGeometry(QtCore.QRect(70, 150, 93, 28))
        self.pushButton_move.setObjectName("pushButton_move")
        self.label_coordinates = QtWidgets.QLabel(self.groupBox_moving)
        self.label_coordinates.setGeometry(QtCore.QRect(10, 160, 55, 16))
        self.label_coordinates.setObjectName("label_coordinates")
        self.textEdit_ipscaner_9 = QtWidgets.QTextEdit(self.groupBox_moving)
        self.textEdit_ipscaner_9.setGeometry(QtCore.QRect(50, 110, 91, 31))
        self.textEdit_ipscaner_9.setObjectName("textEdit_ipscaner_9")
        self.textEdit_move_Y = QtWidgets.QTextEdit(self.groupBox_moving)
        self.textEdit_move_Y.setGeometry(QtCore.QRect(50, 70, 91, 31))
        self.textEdit_move_Y.setObjectName("textEdit_move_Y")
        self.textEdit_move_X = QtWidgets.QTextEdit(self.groupBox_moving)
        self.textEdit_move_X.setGeometry(QtCore.QRect(50, 30, 91, 31))
        self.textEdit_move_X.setObjectName("textEdit_move_X")
        self.groupBox_objective = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_objective.setGeometry(QtCore.QRect(480, 10, 111, 181))
        self.groupBox_objective.setObjectName("groupBox_objective")
        self.pushButton_up = QtWidgets.QPushButton(self.groupBox_objective)
        self.pushButton_up.setGeometry(QtCore.QRect(10, 40, 93, 28))
        self.pushButton_up.setObjectName("pushButton_up")
        self.pushButton_down = QtWidgets.QPushButton(self.groupBox_objective)
        self.pushButton_down.setGeometry(QtCore.QRect(10, 90, 93, 28))
        self.pushButton_down.setObjectName("pushButton_down")
        self.groupBox_product = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_product.setGeometry(QtCore.QRect(600, 10, 201, 171))
        self.groupBox_product.setObjectName("groupBox_product")
        self.pushButton_product_left = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_left.setGeometry(QtCore.QRect(10, 60, 61, 28))
        self.pushButton_product_left.setObjectName("pushButton_product_left")
        self.pushButton_product_right = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_right.setGeometry(QtCore.QRect(130, 60, 61, 28))
        self.pushButton_product_right.setObjectName("pushButton_product_right")
        self.pushButton_product_up = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_up.setGeometry(QtCore.QRect(70, 30, 61, 28))
        self.pushButton_product_up.setObjectName("pushButton_product_up")
        self.pushButton_product_down = QtWidgets.QPushButton(self.groupBox_product)
        self.pushButton_product_down.setGeometry(QtCore.QRect(70, 90, 61, 28))
        self.pushButton_product_down.setObjectName("pushButton_product_down")
        self.groupBox_image = QtWidgets.QGroupBox(self.tab_moving)
        self.groupBox_image.setGeometry(QtCore.QRect(810, 10, 151, 171))
        self.groupBox_image.setObjectName("groupBox_image")

        self.pushButton_imageSave = QtWidgets.QPushButton(self.groupBox_image)
        self.pushButton_imageSave.setGeometry(QtCore.QRect(30, 140, 93, 28))
        self.pushButton_imageSave.setObjectName("pushButton_imageSave")
        self.listView_current_coordinate = QtWidgets.QListView(self.tab_moving)
        self.listView_current_coordinate.setGeometry(QtCore.QRect(610, 220, 341, 371))
        self.listView_current_coordinate.setObjectName("listView_current_coordinate")
        self.label_current_coordinate = QtWidgets.QLabel(self.tab_moving)
        self.label_current_coordinate.setGeometry(QtCore.QRect(730, 190, 151, 16))
        self.label_current_coordinate.setObjectName("label_current_coordinate")
        self.verticalScrollBar_current_coordinate = QtWidgets.QScrollBar(self.tab_moving)
        self.verticalScrollBar_current_coordinate.setGeometry(QtCore.QRect(950, 220, 16, 371))
        self.verticalScrollBar_current_coordinate.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_current_coordinate.setObjectName("verticalScrollBar_current_coordinate")

        self.tabWidget.addTab(self.tab_moving, "")
        self.tab_casset = QtWidgets.QWidget()
        self.tab_casset.setObjectName("tab_casset")
        self.groupBox_position = QtWidgets.QGroupBox(self.tab_casset)
        self.groupBox_position.setGeometry(QtCore.QRect(10, 10, 951, 71))
        self.groupBox_position.setObjectName("groupBox_position")
        self.label_ipscaner_current_position = QtWidgets.QLabel(self.groupBox_position)
        self.label_ipscaner_current_position.setGeometry(QtCore.QRect(60, 10, 91, 16))
        self.label_ipscaner_current_position.setObjectName("label_ipscaner_current_position")
        self.label_ipscaner_3 = QtWidgets.QLabel(self.groupBox_position)
        self.label_ipscaner_3.setGeometry(QtCore.QRect(220, 10, 131, 16))
        self.label_ipscaner_3.setObjectName("label_ipscaner_3")
        self.textEdit_current_position = QtWidgets.QTextEdit(self.groupBox_position)
        self.textEdit_current_position.setGeometry(QtCore.QRect(60, 30, 91, 31))
        self.textEdit_current_position.setObjectName("textEdit_current_position")
        self.textEdit_change_position = QtWidgets.QTextEdit(self.groupBox_position)
        self.textEdit_change_position.setGeometry(QtCore.QRect(190, 30, 91, 31))
        self.textEdit_change_position.setObjectName("textEdit_change_position")
        self.pushButton_change_position = QtWidgets.QPushButton(self.groupBox_position)
        self.pushButton_change_position.setGeometry(QtCore.QRect(300, 30, 111, 28))
        self.pushButton_change_position.setObjectName("pushButton_change_position")
        self.frame = QtWidgets.QFrame(self.tab_casset)
        self.frame.setGeometry(QtCore.QRect(9, 89, 951, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget.addTab(self.tab_casset, "")
        self.tab_z_stack = QtWidgets.QWidget()
        self.tab_z_stack.setObjectName("tab_z_stack")
        self.groupBox = QtWidgets.QGroupBox(self.tab_z_stack)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 951, 111))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_current_Z = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_current_Z.setGeometry(QtCore.QRect(20, 40, 91, 31))
        self.textEdit_current_Z.setObjectName("textEdit_current_Z")
        self.textEdit_upToZ = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_upToZ.setGeometry(QtCore.QRect(130, 40, 91, 31))
        self.textEdit_upToZ.setObjectName("textEdit_upToZ")
        self.textEdit_downToZ = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_downToZ.setGeometry(QtCore.QRect(240, 40, 61, 31))
        self.textEdit_downToZ.setObjectName("textEdit_downToZ")
        self.textEdit_downToZ_step = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_downToZ_step.setGeometry(QtCore.QRect(310, 40, 61, 31))
        self.textEdit_downToZ_step.setObjectName("textEdit_downToZ_step")
        self.checkBox_save_z_stack = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_save_z_stack.setGeometry(QtCore.QRect(390, 50, 161, 17))
        self.checkBox_save_z_stack.setObjectName("checkBox_save_z_stack")
        self.pushButton_execute_downZ = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_execute_downZ.setGeometry(QtCore.QRect(250, 80, 111, 28))
        self.pushButton_execute_downZ.setObjectName("pushButton_execute_downZ")
        self.pushButton__execute_UpZ = QtWidgets.QPushButton(self.groupBox)
        self.pushButton__execute_UpZ.setGeometry(QtCore.QRect(120, 80, 111, 28))
        self.pushButton__execute_UpZ.setObjectName("pushButton__execute_UpZ")
        self.label_current_z = QtWidgets.QLabel(self.groupBox)
        self.label_current_z.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label_current_z.setObjectName("label_current_z")
        self.label_upToZ = QtWidgets.QLabel(self.groupBox)
        self.label_upToZ.setGeometry(QtCore.QRect(140, 20, 81, 16))
        self.label_upToZ.setObjectName("label_upToZ")
        self.label_downToZ = QtWidgets.QLabel(self.groupBox)
        self.label_downToZ.setGeometry(QtCore.QRect(240, 20, 191, 16))
        self.label_downToZ.setObjectName("label_downToZ")
        self.frame_Z = QtWidgets.QFrame(self.tab_z_stack)
        self.frame_Z.setGeometry(QtCore.QRect(9, 129, 951, 471))
        self.frame_Z.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Z.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Z.setObjectName("frame_Z")
        self.tabWidget.addTab(self.tab_z_stack, "")
        self.tab_autofocus = QtWidgets.QWidget()
        self.tab_autofocus.setObjectName("tab_autofocus")
        self.tabWidget.addTab(self.tab_autofocus, "")
        self.tab_trajectory = QtWidgets.QWidget()
        self.tab_trajectory.setObjectName("tab_trajectory")
        self.groupBox_trajectory = QtWidgets.QGroupBox(self.tab_trajectory)
        self.groupBox_trajectory.setGeometry(QtCore.QRect(10, 10, 951, 111))
        self.groupBox_trajectory.setObjectName("groupBox_trajectory")
        self.checkBox_trajectory_save_image = QtWidgets.QCheckBox(self.groupBox_trajectory)
        self.checkBox_trajectory_save_image.setGeometry(QtCore.QRect(780, 30, 161, 17))
        self.checkBox_trajectory_save_image.setObjectName("checkBox_trajectory_save_image")
        self.pushButton_trajectory_execute = QtWidgets.QPushButton(self.groupBox_trajectory)
        self.pushButton_trajectory_execute.setGeometry(QtCore.QRect(800, 60, 111, 28))
        self.pushButton_trajectory_execute.setObjectName("pushButton_trajectory_execute")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_trajectory)
        self.progressBar.setGeometry(QtCore.QRect(520, 50, 251, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_time = QtWidgets.QLabel(self.groupBox_trajectory)
        self.label_time.setGeometry(QtCore.QRect(610, 30, 91, 16))
        self.label_time.setObjectName("label_time")
        self.label_load_trajectory = QtWidgets.QLabel(self.groupBox_trajectory)
        self.label_load_trajectory.setGeometry(QtCore.QRect(310, 30, 91, 20))
        self.label_load_trajectory.setObjectName("label_load_trajectory")
        self.label_trajectory_speed = QtWidgets.QLabel(self.groupBox_trajectory)
        self.label_trajectory_speed.setGeometry(QtCore.QRect(40, 30, 171, 16))
        self.label_trajectory_speed.setObjectName("label_trajectory_speed")
        self.textEdit__trajectory_speedX = QtWidgets.QTextEdit(self.groupBox_trajectory)
        self.textEdit__trajectory_speedX.setGeometry(QtCore.QRect(280, 50, 71, 31))
        self.textEdit__trajectory_speedX.setObjectName("textEdit__trajectory_speedX")
        self.textEdit_trajectory_speedY = QtWidgets.QTextEdit(self.groupBox_trajectory)
        self.textEdit_trajectory_speedY.setGeometry(QtCore.QRect(360, 50, 71, 31))
        self.textEdit_trajectory_speedY.setObjectName("textEdit_trajectory_speedY")
        self.pushButton_load_trajectory = QtWidgets.QPushButton(self.groupBox_trajectory)
        self.pushButton_load_trajectory.setGeometry(QtCore.QRect(60, 60, 111, 28))
        self.pushButton_load_trajectory.setObjectName("pushButton_load_trajectory")
        self.listView_trajectory = QtWidgets.QListView(self.tab_trajectory)
        self.listView_trajectory.setGeometry(QtCore.QRect(680, 150, 256, 451))
        self.listView_trajectory.setObjectName("listView_trajectory")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.tab_trajectory)
        self.verticalScrollBar.setGeometry(QtCore.QRect(940, 150, 20, 451))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_trajectory_ = QtWidgets.QLabel(self.tab_trajectory)
        self.label_trajectory_.setGeometry(QtCore.QRect(740, 130, 141, 16))
        self.label_trajectory_.setObjectName("label_trajectory_")
        self.frame_trajectory = QtWidgets.QFrame(self.tab_trajectory)
        self.frame_trajectory.setGeometry(QtCore.QRect(9, 149, 661, 451))
        self.frame_trajectory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_trajectory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_trajectory.setObjectName("frame_trajectory")
        self.tabWidget.addTab(self.tab_trajectory, "")
        self.tab_sensor = QtWidgets.QWidget()
        self.tab_sensor.setObjectName("tab_sensor")
        self.tabWidget.addTab(self.tab_sensor, "")
        self.groupBox_initial = QtWidgets.QGroupBox(Dialog)
        self.groupBox_initial.setGeometry(QtCore.QRect(10, 10, 981, 141))
        self.groupBox_initial.setObjectName("groupBox_initial")
        self.textEdit_ipscaner = QtWidgets.QTextEdit(self.groupBox_initial)
        self.textEdit_ipscaner.setGeometry(QtCore.QRect(80, 20, 331, 31))
        self.textEdit_ipscaner.setObjectName("textEdit_ipscaner")
        self.textEdit_folder = QtWidgets.QTextEdit(self.groupBox_initial)
        self.textEdit_folder.setGeometry(QtCore.QRect(130, 100, 701, 31))
        self.textEdit_folder.setObjectName("textEdit_folder")
        self.label_ipscaner = QtWidgets.QLabel(self.groupBox_initial)
        self.label_ipscaner.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_ipscaner.setObjectName("label_ipscaner")
        self.label_folder = QtWidgets.QLabel(self.groupBox_initial)
        self.label_folder.setGeometry(QtCore.QRect(10, 100, 111, 16))
        self.label_folder.setObjectName("label_folder")
        self.textEdit_idscaner = QtWidgets.QTextEdit(self.groupBox_initial)
        self.textEdit_idscaner.setGeometry(QtCore.QRect(500, 20, 331, 31))
        self.textEdit_idscaner.setObjectName("textEdit_idscaner")
        self.label_idscaner = QtWidgets.QLabel(self.groupBox_initial)
        self.label_idscaner.setGeometry(QtCore.QRect(430, 30, 71, 16))
        self.label_idscaner.setObjectName("label_idscaner")
        self.pushButton_connection = QtWidgets.QPushButton(self.groupBox_initial)
        self.pushButton_connection.setGeometry(QtCore.QRect(862, 20, 111, 28))
        self.pushButton_connection.setObjectName("pushButton_connection")
        self.pushButton_scaner = QtWidgets.QPushButton(self.groupBox_initial)
        self.pushButton_scaner.setGeometry(QtCore.QRect(862, 60, 111, 28))
        self.pushButton_scaner.setObjectName("pushButton_scaner")
        self.label_scaner_code = QtWidgets.QLabel(self.groupBox_initial)
        self.label_scaner_code.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_scaner_code.setObjectName("label_scaner_code")
        self.textEdit_ipscaner_2 = QtWidgets.QTextEdit(self.groupBox_initial)
        self.textEdit_ipscaner_2.setGeometry(QtCore.QRect(80, 60, 331, 31))
        self.textEdit_ipscaner_2.setObjectName("textEdit_ipscaner_2")
        self.checkBox_scaner_code_file = QtWidgets.QCheckBox(self.groupBox_initial)
        self.checkBox_scaner_code_file.setGeometry(QtCore.QRect(430, 70, 161, 17))
        self.checkBox_scaner_code_file.setObjectName("checkBox_scaner_code_file")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox_parameters.setTitle(_translate("Dialog", "Параметры"))
        self.label_X.setText(_translate("Dialog", "X"))
        self.label_Y.setText(_translate("Dialog", "Y"))
        self.label_Z.setText(_translate("Dialog", "Z"))
        self.label_Speed.setText(_translate("Dialog", "Скорость"))
        self.label_acceleration.setText(_translate("Dialog", "Ускорение"))
        self.groupBox_moving.setTitle(_translate("Dialog", "Перемещение"))
        self.pushButton_move.setText(_translate("Dialog", "Переместить"))
        self.label_coordinates.setText(_translate("Dialog", "(0, 0, 0)"))
        self.groupBox_objective.setTitle(_translate("Dialog", "Объектив"))
        self.pushButton_up.setText(_translate("Dialog", "Вверх"))
        self.pushButton_down.setText(_translate("Dialog", "Вниз"))
        self.groupBox_product.setTitle(_translate("Dialog", "Препарат"))
        self.pushButton_product_left.setText(_translate("Dialog", "влево"))
        self.pushButton_product_right.setText(_translate("Dialog", "вправо"))
        self.pushButton_product_up.setText(_translate("Dialog", "вверх"))
        self.pushButton_product_down.setText(_translate("Dialog", "вниз"))
        self.groupBox_image.setTitle(_translate("Dialog", "Изображение"))
        self.pushButton_imageSave.setText(_translate("Dialog", "Сохранить"))
        self.label_current_coordinate.setText(_translate("Dialog", "Текущая координата"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_moving), _translate("Dialog", "Перемещение"))
        self.groupBox_position.setTitle(_translate("Dialog", "Позиция"))
        self.label_ipscaner_current_position.setText(_translate("Dialog", "Текущая позиция"))
        self.label_ipscaner_3.setText(_translate("Dialog", "Переместить в позицию"))
        self.pushButton_change_position.setText(_translate("Dialog", "Выполнить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_casset), _translate("Dialog", "Кассета"))
        self.groupBox.setTitle(_translate("Dialog", "Перемещение по z"))
        self.checkBox_save_z_stack.setText(_translate("Dialog", "сохранять все изображения"))
        self.pushButton_execute_downZ.setText(_translate("Dialog", "Выполнить"))
        self.pushButton__execute_UpZ.setText(_translate("Dialog", "Выполнить"))
        self.label_current_z.setText(_translate("Dialog", "Текущее Z"))
        self.label_upToZ.setText(_translate("Dialog", "Подняться в Z"))
        self.label_downToZ.setText(_translate("Dialog", "Спуститься по Z до значения с шагом"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_z_stack), _translate("Dialog", "Z-стеки"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_autofocus), _translate("Dialog", "Автофокусировка"))
        self.groupBox_trajectory.setTitle(_translate("Dialog", "GroupBox"))
        self.checkBox_trajectory_save_image.setText(_translate("Dialog", "сохранить изображение"))
        self.pushButton_trajectory_execute.setText(_translate("Dialog", "Выполнить"))
        self.label_time.setText(_translate("Dialog", "Время загрузки"))
        self.label_load_trajectory.setText(_translate("Dialog", "Скорость по X и Y"))
        self.label_trajectory_speed.setText(_translate("Dialog", "Загрузить траекторию из файла"))
        self.pushButton_load_trajectory.setText(_translate("Dialog", "Выбрать файл"))
        self.label_trajectory_.setText(_translate("Dialog", "Движение по траектории"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trajectory), _translate("Dialog", "По траектории"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sensor), _translate("Dialog", "Датчики"))
        self.groupBox_initial.setTitle(_translate("Dialog", "Параметры инициализации"))
        self.label_ipscaner.setText(_translate("Dialog", "IP Сканера"))
        self.label_folder.setText(_translate("Dialog", "Папка сохранения"))
        self.label_idscaner.setText(_translate("Dialog", "ID Сканера"))
        self.pushButton_connection.setText(_translate("Dialog", "Подключить"))
        self.pushButton_scaner.setText(_translate("Dialog", "Сканер ШтрихКода"))
        self.label_scaner_code.setText(_translate("Dialog", "Штрих-Код"))
        self.checkBox_scaner_code_file.setText(_translate("Dialog", "Сохранять в имени файла"))

    def setInitialImage(self):

        self.frame_small = QtWidgets.QLabel(self.groupBox_image)
        self.frame_small.setGeometry(QtCore.QRect(20, 20, 121, 111))
        self.frame_small.setObjectName("frame_small")
        pixmap = QPixmap('s1_l3_Seg1_defocus-1450.jpg')
        self.frame_small.setPixmap(pixmap.scaled(self.frame_small.width(),self.frame_small.height()))

        self.frame_large = QtWidgets.QLabel(self.tab_moving)
        self.frame_large.setGeometry(QtCore.QRect(10, 219, 581, 371))
        self.frame_large.setObjectName("frame_large")
        pixmap = QPixmap('s1_l3_Seg1_defocus-1450.jpg')
        self.frame_large.setPixmap(pixmap.scaled(self.frame_large.width(),self.frame_large.height()))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.setInitialImage()
    Dialog.show()
    sys.exit(app.exec_())
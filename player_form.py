from PyQt6 import QtCore, QtGui, QtWidgets


class UiWizardPage(object):

    def setup_ui(self, wizard_page):
        wizard_page.setObjectName("wizard_page")
        wizard_page.resize(652, 596)
        wizard_page.setAutoFillBackground(False)

        self.scroll_area = QtWidgets.QScrollArea(wizard_page)
        self.scroll_area.setGeometry(QtCore.QRect(90, 20, 481, 331))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")

        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 479, 329))

        self.verticalScrollBar = QtWidgets.QScrollBar(self.scroll_area_widget_contents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(460, 0, 16, 331))
        self.verticalScrollBar.setObjectName("verticalScrollBar")

        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        self.push_button_1 = QtWidgets.QPushButton(wizard_page)

        self.push_button_1.setGeometry(QtCore.QRect(290, 370, 89, 25))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/pause.png"))
        self.push_button_1.setIcon(icon)
        self.push_button_1.setCheckable(True)
        self.push_button_1.setObjectName("pause")

        self.push_button_2 = QtWidgets.QPushButton(wizard_page)
        self.push_button_2.setGeometry(QtCore.QRect(390, 370, 89, 25))
        self.push_button_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/forward_button.png"))
        self.push_button_2.setIcon(icon1)
        self.push_button_2.setObjectName("forward")

        self.push_button_3 = QtWidgets.QPushButton(wizard_page)
        self.push_button_3.setGeometry(QtCore.QRect(190, 370, 89, 25))
        self.push_button_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/backward_button.png"))
        self.push_button_3.setIcon(icon2)
        self.push_button_3.setObjectName("backward")

        self.vertical_slider = QtWidgets.QSlider(wizard_page)
        self.vertical_slider.setGeometry(QtCore.QRect(550, 370, 16, 160))
        self.vertical_slider.setObjectName("vertical_slider")

        self.progress_bar = QtWidgets.QProgressBar(wizard_page)
        self.progress_bar.setGeometry(QtCore.QRect(170, 440, 318, 23))
        self.progress_bar.setProperty("value", 50)
        self.progress_bar.setObjectName("progress_bar")

        self.retranslate_ui(wizard_page)
        QtCore.QMetaObject.connectSlotsByName(wizard_page)

    @staticmethod
    def retranslate_ui(wizard_page):
        _translate = QtCore.QCoreApplication.translate
        wizard_page.setWindowTitle(_translate("wizard_page", "wizard_page"))

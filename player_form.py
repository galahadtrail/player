from PyQt6 import QtCore, QtGui, QtWidgets


class UiWizardPage(object):
    def setup_ui(self, wizard_page):
        wizard_page.setObjectName("wizard_page")
        wizard_page.resize(651, 596)
        wizard_page.setAutoFillBackground(False)
        wizard_page.setStyleSheet("")

        self.scroll_area = QtWidgets.QScrollArea(wizard_page)
        self.scroll_area.setGeometry(QtCore.QRect(90, 20, 481, 331))
        self.scroll_area.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 112, 0, 255));\n"
"border:1px solid orange")
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(QtCore.QRect(0, 0, 479, 329))
        self.scroll_area_widget_contents.setObjectName("scroll_area_widget_contents")
        
        self.vertical_scroll_bar = QtWidgets.QScrollBar(self.scroll_area_widget_contents)
        self.vertical_scroll_bar.setGeometry(QtCore.QRect(460, 0, 16, 331))
        self.vertical_scroll_bar.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.vertical_scroll_bar.setObjectName("vertical_scroll_bar")
        self.scroll_area.setWidget(self.scroll_area_widget_contents)
        
        self.push_button = QtWidgets.QPushButton(wizard_page)
        self.push_button.setGeometry(QtCore.QRect(290, 400, 101, 91))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        self.push_button.setFont(font)
        self.push_button.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.02, y1:0.0628636, x2:0.94, y2:0.954545, stop:0 rgba(255, 138, 0, 255), stop:1 rgba(0, 0, 44, 255));\n"
"border-bottom: 4px solid orange;\n"
"border-right:4px solid orange;\n"
"border-left:2px solid orange;\n"
"border-top:2px solid orange;\n"
"color: rgb(228, 223, 207);")
        self.push_button.setCheckable(True)
        self.push_button.setObjectName("push_button")
        
        self.push_button2 = QtWidgets.QPushButton(wizard_page)
        self.push_button2.setGeometry(QtCore.QRect(420, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        self.push_button2.setFont(font)
        self.push_button2.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.02, y1:0.0628636, x2:0.94, y2:0.954545, stop:0 rgba(255, 138, 0, 255), stop:1 rgba(0, 0, 44, 255));\n"
"border-bottom: 4px solid orange;\n"
"border-right:4px solid orange;\n"
"border-left:2px solid orange;\n"
"border-top:2px solid orange;\n"
"color: rgb(228, 223, 207);")
        self.push_button2.setObjectName("push_button2")
        
        self.push_button3 = QtWidgets.QPushButton(wizard_page)
        self.push_button3.setGeometry(QtCore.QRect(170, 420, 91, 61))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        self.push_button3.setFont(font)
        self.push_button3.setStyleSheet("border-radius:10px;\n"
"background-color: qlineargradient(spread:pad, x1:0.02, y1:0.0628636, x2:0.94, y2:0.954545, stop:0 rgba(255, 138, 0, 255), stop:1 rgba(0, 0, 44, 255));\n"
"border-bottom: 4px solid orange;\n"
"border-right:4px solid orange;\n"
"border-left:2px solid orange;\n"
"border-top:2px solid orange;\n"
"color: rgb(228, 223, 207);")
        self.push_button3.setObjectName("push_button3")
        
        self.progress_bar = QtWidgets.QProgressBar(wizard_page)
        self.progress_bar.setGeometry(QtCore.QRect(90, 350, 481, 23))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(14)
        font.setItalic(True)
        self.progress_bar.setFont(font)
        self.progress_bar.setStyleSheet("color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 112, 0, 255));\n"
"color: rgb(228, 223, 207);")
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        
        self.widget = QtWidgets.QWidget(wizard_page)
        self.widget.setGeometry(QtCore.QRect(-10, 0, 661, 601))
        self.widget.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 112, 0, 255));")
        self.widget.setObjectName("widget")
        
        self.vertical_slider = QtWidgets.QSlider(self.widget)
        self.vertical_slider.setGeometry(QtCore.QRect(560, 380, 16, 160))
        self.vertical_slider.setStyleSheet("background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 112, 0, 255));")
        self.vertical_slider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.vertical_slider.setObjectName("vertical_slider")
        
        self.widget.raise_()
        self.scroll_area.raise_()
        self.push_button.raise_()
        self.push_button2.raise_()
        self.push_button3.raise_()
        self.progress_bar.raise_()

        self.retranslate_ui(wizard_page)
        QtCore.QMetaObject.connectSlotsByName(wizard_page)

    def retranslate_ui(self, wizard_page):
        _translate = QtCore.QCoreApplication.translate
        wizard_page.setWindowTitle(_translate("wizard_page", "wizard_page"))
        self.push_button.setText(_translate("wizard_page", "Play"))
        self.push_button2.setText(_translate("wizard_page", "Frwd"))
        self.push_button3.setText(_translate("wizard_page", "Back"))

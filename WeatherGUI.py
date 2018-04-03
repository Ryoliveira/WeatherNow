import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui

from WeatherData import WeatherData

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather now")
        self.setGeometry(600, 600, 500, 200)

        self.city_search = QtWidgets.QLabel("  City:")
        self.city_entry = QtWidgets.QLineEdit()

        self.state_search = QtWidgets.QLabel("State:")
        self.state_entry = QtWidgets.QLineEdit()

        self.searchb = QtWidgets.QPushButton('Search')
        self.searchb.clicked.connect(self.search_location)
        self.clearb = QtWidgets.QPushButton('Clear')
        self.clearb.clicked.connect(self.clear)

        self.sun_image = QtWidgets.QLabel()
        self.sun_image.setPixmap(QtGui.QPixmap('Sun-logo-resize.png'))


        self.loclb = QtWidgets.QLabel("Location:")
        self.datelb = QtWidgets.QLabel("Date:")
        self.templb = QtWidgets.QLabel("Temp:")

        self.loclb_value = QtWidgets.QLabel()
        self.datelb_value = QtWidgets.QLabel()
        self.templb_value = QtWidgets.QLabel()

        self.condlb = QtWidgets.QLabel("Condition:")
        self.windspdlb = QtWidgets.QLabel("Wind Speed:")
        self.winddirlb = QtWidgets.QLabel("Wind Direction:")

        self.condlb_value = QtWidgets.QLabel()
        self.windspdlb_value = QtWidgets.QLabel()
        self.winddirlb_value = QtWidgets.QLabel()

        # City label and entry box
        city_box = QtWidgets.QHBoxLayout()
        city_box.addWidget(self.city_search)
        city_box.addWidget(self.city_entry)

        # State label and entry box
        state_box = QtWidgets.QHBoxLayout()
        state_box.addWidget(self.state_search)
        state_box.addWidget(self.state_entry)
        state_box.addStretch(1)

        # Buttons Box
        button_box = QtWidgets.QHBoxLayout()
        button_box.addWidget(self.searchb)
        button_box.addWidget(self.clearb)

        # Puts all search widgets in the same box(frame)
        search_widgets_box = QtWidgets.QVBoxLayout()
        search_widgets_box.addLayout(city_box)
        search_widgets_box.addLayout(state_box)
        search_widgets_box.addLayout(button_box)
        search_widgets_box.addStretch()

        # Sun Box(Frame)
        sun_image_box = QtWidgets.QVBoxLayout()
        sun_image_box.addWidget(self.sun_image)
        sun_image_box.addStretch(1)

        # Title box to hold search widgets and sun image
        title_box = QtWidgets.QHBoxLayout()
        title_box.addLayout(search_widgets_box)
        title_box.addStretch(1)
        title_box.addLayout(sun_image_box)

        # First row of labels
        v_labels = QtWidgets.QVBoxLayout()
        v_labels.addWidget(self.loclb)
        v_labels.addWidget(self.datelb)
        v_labels.addWidget(self.templb)

        # Values for first row of labels
        v_label_values = QtWidgets.QVBoxLayout()
        v_label_values.addWidget(self.loclb_value)
        v_label_values.addWidget(self.datelb_value)
        v_label_values.addWidget(self.templb_value)

        # Second row of labels
        v_labels2 = QtWidgets.QVBoxLayout()
        v_labels2.addWidget(self.condlb)
        v_labels2.addWidget(self.windspdlb)
        v_labels2.addWidget(self.winddirlb)
        v_labels2.addStretch()

        # Values for second row of labels
        v_labels2_values = QtWidgets.QVBoxLayout()
        v_labels2_values.addWidget(self.condlb_value)
        v_labels2_values.addWidget(self.windspdlb_value)
        v_labels2_values.addWidget(self.winddirlb_value)

        # Labels put together
        info_box = QtWidgets.QHBoxLayout()
        info_box.addLayout(v_labels)
        info_box.addLayout(v_label_values)
        info_box.addStretch(1)
        info_box.addLayout(v_labels2)
        info_box.addLayout(v_labels2_values)
        info_box.addStretch(1)

        # All frames are put together in this box
        main_box = QtWidgets.QVBoxLayout()
        main_box.addLayout(title_box)
        main_box.addLayout(info_box)
        main_box.addStretch(1)


        self.setLayout(main_box)
        self.show()

    def search_location(self):
        weather_obj = WeatherData(self.city_entry.text(), self.state_entry.text())
        weather_obj.get_weather_data()

        if weather_obj.data == 0:
            self.error_msg(1)
        if 'results' in weather_obj.data:
            self.error_msg(2)

        else:
            print(weather_obj.data['local_time_rfc822'])
            self.loclb_value.setText(weather_obj.data["display_location"]["full"])
            self.datelb_value.setText(weather_obj.data['local_time_rfc822'][:-6])
            self.templb_value.setText(str(weather_obj.data['temp_f']))

            self.condlb_value.setText(weather_obj.data['weather'])
            self.windspdlb_value.setText(str(weather_obj.data['wind_mph']))
            self.winddirlb_value.setText(weather_obj.data['wind_dir'])

    def clear(self):
        self.city_entry.clear()
        self.state_entry.clear()

    def error_msg(self, error_num):
        if error_num == 1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Oops!")
            msg.setInformativeText('Input Invalid')
            msg.setWindowTitle("Error")
            msg.exec_()
        if error_num == 2:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Oops!")
            msg.setInformativeText('Too many results, please put in correct state')
            msg.setWindowTitle("Error!")
            msg.exec_()



app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

def timestamp_to_datetime(timestamp):
    """
    Convert UTC timestamp to formatted datetime string.
    :param timestamp: UTC timestamp (integer or float)
    :return: Formatted datetime string
    """
    try:
        # Convert the timestamp to local structured time
        local_time = time.localtime(timestamp)
        # Format as Year-Month-Day Hour:Minute:Second
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return formatted_time
    except Exception as e:
        return f"Conversion failed: {e}"


class TimeStampConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Timestamp Converter")
        self.setGeometry(100, 100, 400, 200)

        # Create layout
        layout = QVBoxLayout()

        # Input prompt label
        self.label = QLabel("Enter UTC timestamp:")
        layout.addWidget(self.label)

        # Input field
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Convert button
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_timestamp)
        layout.addWidget(self.convert_button)

        # Output result label
        self.result_label = QLabel("Conversion result:")
        layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(layout)

    def convert_timestamp(self):
        user_input = self.input_field.text()
        try:
            timestamp = float(user_input)
            result = timestamp_to_datetime(timestamp)
            self.result_label.setText(f"Conversion result: {result}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid numeric timestamp!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = TimeStampConverter()
    converter.show()
    sys.exit(app.exec_())
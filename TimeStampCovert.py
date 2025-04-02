import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.simpledialog import Dialog

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


def datetime_to_timestamp(datetime_str):
    """
    Convert formatted datetime string to UTC timestamp.
    :param datetime_str: Formatted datetime string (e.g., "2023-01-01 12:00:00")
    :return: UTC timestamp
    """
    try:
        # Parse the datetime string to structured time
        structured_time = time.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        # Convert to UTC timestamp
        timestamp = time.mktime(structured_time)
        return int(timestamp)
    except Exception as e:
        return f"Conversion failed: {e}"

class DateTimePickerDialog(Dialog):
    def __init__(self, parent):
        self.selected_date = None
        self.selected_time = None
        super().__init__(parent, title="Select Date and Time")

    def body(self, master):
        tk.Label(master, text="Select Date:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.calendar = Calendar(master, date_pattern="yyyy-mm-dd")
        self.calendar.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(master, text="Time (HH:MM:SS):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.time_input = tk.Entry(master, width=15)
        self.time_input.grid(row=1, column=1, padx=10, pady=10)
        self.time_input.insert(0, "00:00:00")  # Default time

    def apply(self):
        self.selected_date = self.calendar.get_date()
        self.selected_time = self.time_input.get()

class TimeStampConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timestamp Converter")
        self.geometry("500x300")  # Adjusted size to fit all components
        self.resizable(False, False)  # Fix the window size
        self.attributes("-topmost", True)  # Ensure the window stays on top
        self.init_ui()

    def init_ui(self):
        # Input prompt label for timestamp to datetime
        label1 = tk.Label(self, text="UTC timestamp:")
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Input field for timestamp
        self.input_field_timestamp = tk.Entry(self, width=25)
        self.input_field_timestamp.grid(row=0, column=1, padx=10, pady=10)
        self.input_field_timestamp.insert(0, str(int(time.time())))  # Set current UTC timestamp as default input

        # Output result label for timestamp to datetime
        result_label1 = tk.Label(self, text="Conversion result:")
        result_label1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.result_print_timestamp = tk.Label(self, text="", fg="blue")
        self.result_print_timestamp.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Convert button for timestamp to datetime
        convert_button1 = tk.Button(self, text="Convert to Datetime", command=self.convert_timestamp, bg="#4CAF50", fg="white")
        convert_button1.grid(row=2, column=1, columnspan=2, pady=10, sticky="we")

        # Input prompt label for datetime to timestamp
        label2 = tk.Label(self, text="Datetime:")
        label2.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        # Button to open DateTimePickerDialog
        self.datetime_button = tk.Button(self, text="Select DateTime", command=self.open_datetime_picker, bg="#FFC107", fg="black")
        self.datetime_button.grid(row=3, column=1, padx=10, pady=10, sticky="we")

        # Output result label for datetime to timestamp
        result_label2 = tk.Label(self, text="Conversion result:")
        result_label2.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.result_print_datetime = tk.Label(self, text="", fg="blue")
        self.result_print_datetime.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Convert button for datetime to timestamp
        convert_button2 = tk.Button(self, text="Convert to Timestamp", command=self.convert_datetime, bg="#2196F3", fg="white")
        convert_button2.grid(row=5, column=1, columnspan=2, pady=10, sticky="we")

    def open_datetime_picker(self):
        dialog = DateTimePickerDialog(self)
        if dialog.selected_date and dialog.selected_time:
            self.selected_datetime = f"{dialog.selected_date} {dialog.selected_time}"
            messagebox.showinfo("Selected Datetime", f"Selected: {self.selected_datetime}")

    def convert_timestamp(self):
        user_input = self.input_field_timestamp.get()
        try:
            timestamp = float(user_input)
            result = timestamp_to_datetime(timestamp)
            self.result_print_timestamp.config(text=result)
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid numeric timestamp!")

    def convert_datetime(self):
        try:
            if hasattr(self, 'selected_datetime'):
                result = datetime_to_timestamp(self.selected_datetime)
                self.result_print_datetime.config(text=result)
            else:
                messagebox.showwarning("Error", "Please select a valid datetime first!")
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid time in the format HH:MM:SS!")


if __name__ == "__main__":
    app = TimeStampConverter()
    app.mainloop()

import time
import tkinter as tk
from tkinter import messagebox


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


class TimeStampConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timestamp Converter")
        self.geometry("350x150")
        self.resizable(False, False)  # Fix the window size
        self.attributes("-topmost", True)  # Ensure the window stays on top
        self.init_ui()

    def init_ui(self):
        # Input prompt label
        label = tk.Label(self, text="UTC timestamp:")
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Input field
        self.input_field = tk.Entry(self, width=25)
        self.input_field.grid(row=0, column=1, padx=10, pady=10)
        self.input_field.insert(0, str(int(time.time())))  # Set current UTC timestamp as default input

        # Output result label
        result_label = tk.Label(self, text="Conversion result:")
        result_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.result_print = tk.Label(self, text="", fg="blue")
        self.result_print.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Convert button
        convert_button = tk.Button(self, text="Convert", command=self.convert_timestamp, bg="#4CAF50", fg="white")
        convert_button.grid(row=2, column=1, columnspan=2, pady=20, sticky="we")  # Stretch button to fill width

    def convert_timestamp(self):
        user_input = self.input_field.get()
        try:
            timestamp = float(user_input)
            result = timestamp_to_datetime(timestamp)
            self.result_print.config(text=result)
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid numeric timestamp!")


if __name__ == "__main__":
    app = TimeStampConverter()
    app.mainloop()

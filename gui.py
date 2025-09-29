import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class HelpdeskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Helpdesk System")

        # Create tabs
        self.notebook = ttk.Notebook(root)
        self.employee_helpdesk_frame = ttk.Frame(self.notebook)
        self.customer_helpdesk_frame = ttk.Frame(self.notebook)
        self.circular_summarizer_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.employee_helpdesk_frame, text="Employee Helpdesk")
        self.notebook.add(self.customer_helpdesk_frame, text="Customer Helpdesk")
        self.notebook.add(self.circular_summarizer_frame, text="Circular Summarizer")

        # Employee Helpdesk
        self.create_employee_helpdesk()

        # Customer Helpdesk
        self.create_customer_helpdesk()

        # Circular Summarizer
        self.create_circular_summarizer()

        # Pack the notebook
        self.notebook.pack(expand=True, fill='both')

    def create_employee_helpdesk(self):
        employee_helpdesk_label = ttk.Label(self.employee_helpdesk_frame, text="Employee Helpdesk")
        employee_helpdesk_label.grid(row=0, column=0, padx=10, pady=10)

        # Add more widgets for employee helpdesk

    def create_customer_helpdesk(self):
        customer_helpdesk_label = ttk.Label(self.customer_helpdesk_frame, text="Customer Helpdesk")
        customer_helpdesk_label.grid(row=0, column=0, padx=10, pady=10)

        # Add more widgets for customer helpdesk

    def create_circular_summarizer(self):
        circular_summarizer_label = ttk.Label(self.circular_summarizer_frame, text="Circular Summarizer Helpdesk")
        circular_summarizer_label.grid(row=0, column=0, padx=10, pady=10)

        # Add more widgets for circular summarizer

if __name__ == "__main__":
    root = tk.Tk()

    # Set window size and position
    window_width = 800
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Set window icon
    icon_path = "your_icon.png"  # Replace with the path to your icon image
    icon = ImageTk.PhotoImage(Image.open(icon_path))
    root.iconphoto(True, icon)

    app = HelpdeskApp(root)
    root.mainloop()

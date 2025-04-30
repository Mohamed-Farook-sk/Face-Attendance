import ttkbootstrap as tttk
from ttkbootstrap.constants import *
from tkinter import Toplevel, messagebox
import random
from PIL import Image, ImageTk

class HelpDesk:
    def __init__(self, root):
        self.root = root
        self.root.title("Helpdesk")
        self.root.geometry("1920x1080+0+0")

        bg_image = Image.open("background.jpg")  # Give correct path to your background image
        bg_image = bg_image.resize((1920, 1080))  # Resize it to match your window size
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tttk.Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

       

        # Top Bar
        self.top_bar = tttk.Frame(self.root, bootstyle=PRIMARY, height=50)
        self.top_bar.pack(side='top', fill='x')

        tttk.Label(self.top_bar, text='Welcome to Helpdesk System', font=('Helvetica', 16, 'bold'), bootstyle="inverse-primary").pack(pady=10)

        # Main Content Area
        self.main_content = tttk.Frame(self.root, width=950, height=650)
        self.main_content.pack(side='right', fill='both', expand=True, padx=20, pady=20)

        tttk.Label(self.main_content, text='How can we assist you today?', background="", foreground="black", font=('Helvetica', 24, 'bold')).pack(pady=20)

        # Create button frame inside HelpDesk class
        self.button_frame = tttk.Frame(self.root)
        self.button_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Set the button styles
        style = tttk.Style()
        style.configure("success.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
        style.configure("primary.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
        style.configure("info.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
        style.configure("warning.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
        style.configure("secondary.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
        style.configure("danger.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))

        # Create the buttons and assign their commands
        btn1 = tttk.Button(self.button_frame, text="How does face recognition work?", command=self.prob1, width=70, style="success.TButton")
        btn2 = tttk.Button(self.button_frame, text="How to register my face in the system?", command=self.prob2, width=70, style="primary.TButton")
        btn3 = tttk.Button(self.button_frame, text="What to do if my face is not recognized?", command=self.prob3, width=70, style="info.TButton")
        btn4 = tttk.Button(self.button_frame, text="How secure is the face recognition system?", command=self.prob4, width=70, style="warning.TButton")
        btn5 = tttk.Button(self.button_frame, text="How to reset my password if I can't log in?", command=self.prob5, width=70, style="secondary.TButton")
        btn6 = tttk.Button(self.button_frame, text="System not responding - What to do?", command=self.prob6, width=70, style="danger.TButton")

        # Arrange buttons in grid layout
        btn1.grid(row=0, column=0, padx=20, pady=20)
        btn2.grid(row=1, column=0, padx=20, pady=20)
        btn3.grid(row=2, column=0, padx=20, pady=20)
        btn4.grid(row=3, column=0, padx=20, pady=20)
        btn5.grid(row=4, column=0, padx=20, pady=20)
        btn6.grid(row=5, column=0, padx=20, pady=20)

    def prob1(self):
        messagebox.showinfo("Report", "Face recognition captures unique facial features and matches them with stored data.",parent = self.root)

    def prob2(self):
        messagebox.showinfo("Report", "1) Fill your details in Student Details Tab\n2) Click on 'Take Photo Sample'\n3) Camera will open, register your face!",parent = self.root)

    def prob3(self):
        messagebox.showinfo("Report", "Ensure proper lighting, clean camera lens, and retry registration if needed.",parent = self.root)

    def prob4(self):
        messagebox.showinfo("Report", "Only authorized Admins can access the system. External users are restricted.",parent = self.root)

    def prob5(self):
        messagebox.showinfo("Report", "Click on 'Forgot Password', follow the email/OTP instructions.", parent = self.root)

    def prob6(self):
        messagebox.showinfo("Report", "Restart the application, check your internet, or contact support.",parent = self.root)


if __name__ == "__main__":
    root = tttk.Window(themename="minty")
    obj = HelpDesk(root)
    root.mainloop()

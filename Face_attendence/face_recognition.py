from tkinter import Toplevel, messagebox
from student_details import studentdetails 
from train_data import traindata
from attendence import attendence
from face_rec import facerecognition
from helpdesk import HelpDesk
import os
import ttkbootstrap as tttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk

# Create main window
root = tttk.Window(themename="litera")
root.title("Student Face Recognition Attendance System")
root.geometry("1920x1080+0+0")
root.configure(bg='white')

bg_image = Image.open("background.jpg")  # Give correct path to your background image
bg_image = bg_image.resize((1920, 1080))  # Resize it to match your window size
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tttk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1) 

# Header label (now using ttkbootstrap Label)
header = tttk.Label(root, text="STUDENT FACE ATTENDENCE", font=("Helvetica", 24, "bold"),foreground = "white",background="#4682b4",anchor="center", padding=10)
header.pack(fill=tttk.X)

sub_frame = tttk.Frame(root)
sub_frame.pack(side='left', fill='y')

color_label = tttk.Label(sub_frame, background="#4582EC")  # sub_frame background
color_label.place(x=0, y=0, relwidth=1, relheight=1)

#sub_frame_label = tttk.Label(sub_frame, text="",font=("Georgia", 20, "bold"),foreground="#154360",background="#4582EC",width=10,anchor="center",padding=10)
#sub_frame_label.grid(row=0, column=0,padx=0,pady=0)

sub_frame =tttk.Frame(sub_frame)
sub_frame.grid(row=1,column=0)

color_label_2 = tttk.Label(sub_frame, background="#4582EC")  # sub_frame background
color_label_2.place(x=0, y=0, relwidth=1, relheight=1)




# Functions to open windows
def open_student_details():
    new_window = Toplevel(root)
    studentdetails(new_window)

def face_recognition():
    new_window3 = Toplevel(root)
    facerecognition(new_window3)

def attendance():
    new_window4 = Toplevel(root)
    attendence(new_window4)

def train_data():
    new_window2 = Toplevel(root)
    traindata(new_window2)

def photos():
    os.startfile("Photos")

def help_desk():
    new_window5 = Toplevel(root)
    HelpDesk(new_window5)

def exit_app():
    root.destroy()

# Create a frame to hold buttons
button_frame = tttk.Frame(root)
button_frame.pack(pady=250)
color_label_3 = tttk.Label(button_frame, background="#D3D4D8")
color_label_3.place(x=0, y=0, relwidth=1, relheight=1)

# Create buttons (now using ttkbootstrap Buttons)

style = tttk.Style()
style.configure("success.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))        
style.configure("primary.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
style.configure("info.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
style.configure("warning.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
style.configure("secondary.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))
style.configure("danger.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))

btn1 = tttk.Button(button_frame, text="Student Details", command=open_student_details, width=25,style="success.TButton")
btn2 = tttk.Button(button_frame, text="Face Recognition", command=face_recognition, width=25, style="primary.TButton")
btn3 = tttk.Button(button_frame,text="Attendance", command=attendance, width=25, style="info.TButton")
btn4 = tttk.Button(button_frame, text="Train Data", command=train_data, width=25, style="danger.TButton")
btn5 = tttk.Button(button_frame,text="Photos", command=photos, width=25,style="secondary.TButton")
btn6 = tttk.Button(button_frame,text="Exit", command=exit_app, width=25,style="warning.TButton")

# Arrange buttons in place layout
btn1.grid(row=0,column=0,padx=20,pady=20,sticky="ew")
btn2.grid(row=1,column=0,padx=20,pady=20,sticky="ew")
btn3.grid(row=1,column=1,padx=20,pady=20,sticky="ew")
btn4.grid(row=0,column=1,padx=20,pady=20,sticky="ew")
btn5.grid(row=2,column=0,padx=20,pady=20,sticky="ew")
btn6.grid(row=2,column=1,padx=20,pady=20,sticky="ew")



#help Desk #3498db

style = tttk.Style()
style.configure("custom.TButton",padding=(10, 20),font=("Helvetica", 10, "bold"),foreground = "#154360" ,bordercolor="#4582EC")
btn_helpdesk = tttk.Button(sub_frame, text="Help Desk", command=lambda: help_desk(), width=25, style="custom.TButton")
btn_helpdesk.grid(row=0, column=0,pady=20)

btn_faq = tttk.Button(sub_frame, text="FAQs", command=lambda: common_questions(), width=25, style="custom.TButton")
btn_faq.grid(row=1, column=0,pady=20)

btn_con = tttk.Button(sub_frame, text="Contact Support", command=lambda: contact_support(), width=25, style="custom.TButton")
btn_con.grid(row=2, column=0,pady=20)

btn_report = tttk.Button(sub_frame, text="Report an Issue", command=lambda: report_issue(), width=25, style="custom.TButton")
btn_report.grid(row=3, column=0,pady=20)

btn_dev = tttk.Button(sub_frame, text="Developer", command=lambda: dev(), width=25, style="custom.TButton")
btn_dev.grid(row=4, column=0,pady=20)

def report_issue():
    messagebox.showinfo("Report an Issue", "Please describe your issue in detail and submit it to our support team.")

def contact_support():
        messagebox.showinfo("Contact Information", "Mohamed Farook SK\nEmail: farook@mail.com\nPhone: 5689741230\nAvailable: 9 AM - 6 PM")

def common_questions():
        messagebox.showinfo("FAQ", "For further Assitance Reach Help Desk!")

def dev():
     messagebox.showinfo("Developers","1)Name: Mohamed Farook \n Mail: farook@gmail.com \n Contact: 4578963214 \n")

root.mainloop()

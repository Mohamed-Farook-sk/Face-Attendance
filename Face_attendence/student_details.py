import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class studentdetails:

    def __init__(self, root):
        self.root = root  # Use the provided Toplevel window
        self.root.title("Student Details")
        self.root.geometry("1920x1080+0+0")
        self.root.configure(bg='cyan')

        bg_image = Image.open("background.jpg")  # Give correct path to your background image
        bg_image = bg_image.resize((1920, 1080))  # Resize it to match your window size
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tb.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_ph=StringVar()
        self.var_mail=StringVar()
        self.var_regno=StringVar()
        self.var_dept=StringVar()
        self.var_branch=StringVar()
        self.var_semester=StringVar()



            # Title Label
        title_Label = tb.Label(self.root, text="STUDENT INFORMATION", font=("Helvetica", 14, "bold"),bootstyle="inverse-success", anchor=CENTER, padding=10)
        title_Label.pack(fill=tb.X)

        root.grid_propagate(False)

        # Main Frame
        main_frame = tb.Frame(self.root, bootstyle="default")
        main_frame.place(x=15, y=70, width=1878, height=950)
        main_frame.grid_propagate(False)

        # Upper Frame
        main_frame_2 = tb.Labelframe(main_frame, text="Student Details", bootstyle="primary")
        main_frame_2.place(x=10, y=10, height=450, width=1854)
        main_frame_2.grid_propagate(False)

        ui_image = Image.open("filler2.jpg")  # Correct image path here
        ui_image = ui_image.resize((300, 100))  # Resize if needed

        self.ui_photo = ImageTk.PhotoImage(ui_image)

        self.ui_label = tb.Label(main_frame, image=self.ui_photo, compound="top")
        self.ui_label.place(x=1550, y=325)   # You can adjust 'y' if needed

        # Bottom Frame
        bottom_frame = tb.Labelframe(main_frame, text="Edit Student Details", bootstyle="primary")
        bottom_frame.place(x=10, y=475, height=450, width=1854)
        bottom_frame.grid_propagate(False)

        # Subframes
        sub_frame = tb.Labelframe(main_frame_2, text="Personal Information", bootstyle="info")
        sub_frame.place(x=20, y=0, height=410, width=730)
        sub_frame.grid_propagate(False)

        sub_frame_2 = tb.Labelframe(main_frame_2, text="Academic Details", bootstyle="info")
        sub_frame_2.place(x=770, y=0, height=410, width=730)
        sub_frame_2.grid_propagate(False)

        sub_frame_3 = tb.Labelframe(main_frame_2, text="~~~",bootstyle="info")
        sub_frame_3.place(x=1520, y=0, height=277, width=323)
        sub_frame_3.grid_propagate(False)

         # Create a new style for Label
        style = tb.Style()
        style.configure('CustomLabel.TLabel', font=('Lato', 13, 'normal'))

        # Personal Info Labels and Entries
        student_name = tb.Label(sub_frame, text="Student Name:",style="CustomLabel.TLabel")
        student_name.grid(row=0, column=0, padx=10, pady=25, sticky=W)

        student_name_entry = tb.Entry(sub_frame, textvariable=self.var_name, width=40, font=('Lato', 13, 'normal'))
        student_name_entry.grid(row=0, column=1, padx=10, pady=10)

        Gender = tb.Label(sub_frame, text="Gender:", style="CustomLabel.TLabel")
        Gender.grid(row=1, column=0, padx=10, pady=25, sticky=W)

        Gender_combo = tb.Combobox(sub_frame, textvariable=self.var_gender,font=('Lato', 13, 'normal'), width=38, state="readonly")
        Gender_combo["values"] = ("Select", "Male", "Female")
        Gender_combo.current(0)
        Gender_combo.grid(row=1, column=1, padx=10, pady=10)

        DOB = tb.Label(sub_frame, text="DOB:",style="CustomLabel.TLabel")
        DOB.grid(row=2, column=0, padx=10, pady=25, sticky=W)

        DOB_entry = tb.Entry(sub_frame, textvariable=self.var_dob, width=40, font=('Lato', 13, 'normal'))
        DOB_entry.grid(row=2, column=1, padx=10, pady=10)

        PhoneNo = tb.Label(sub_frame, text="Phone No:",style="CustomLabel.TLabel")
        PhoneNo.grid(row=3, column=0, padx=10, pady=25, sticky=W)

        PhoneNo_entry = tb.Entry(sub_frame, textvariable=self.var_ph, width=40,font=('Lato', 13, 'normal'))
        PhoneNo_entry.grid(row=3, column=1, padx=10, pady=10)

        Mail = tb.Label(sub_frame, text="Mail:",style="CustomLabel.TLabel")
        Mail.grid(row=4, column=0, padx=10, pady=25, sticky=W)

        Mail_entry = tb.Entry(sub_frame, textvariable=self.var_mail, width=40, font=('Lato', 13, 'normal'))
        Mail_entry.grid(row=4, column=1, padx=10, pady=10)

        # Academic Details
        Roll_No = tb.Label(sub_frame_2, text="Register Number:", style="CustomLabel.TLabel")
        Roll_No.grid(row=0, column=0, padx=10, pady=25, sticky=W)

        Roll_No_entry = tb.Entry(sub_frame_2, textvariable=self.var_regno, width=40, font=('Lato', 13, 'normal'))
        Roll_No_entry.grid(row=0, column=1, padx=10, pady=10)

        Department = tb.Label(sub_frame_2, text="Department:", style="CustomLabel.TLabel")
        Department.grid(row=1, column=0, padx=10, pady=25, sticky=W)

        Department_entry = tb.Entry(sub_frame_2, textvariable=self.var_dept, width=40,font=('Lato', 13, 'normal'))
        Department_entry.grid(row=1, column=1, padx=10, pady=10)

        Branch = tb.Label(sub_frame_2, text="Branch:",style="CustomLabel.TLabel")
        Branch.grid(row=2, column=0, padx=10, pady=25, sticky=W)

        Branch_entry = tb.Entry(sub_frame_2, textvariable=self.var_branch, width=40, font=('Lato', 13, 'normal'))
        Branch_entry.grid(row=2, column=1, padx=10, pady=10)

        Semester = tb.Label(sub_frame_2, text="Semester:", style="CustomLabel.TLabel")
        Semester.grid(row=3, column=0, padx=10, pady=25, sticky=W)

        Semester_entry = tb.Entry(sub_frame_2, textvariable=self.var_semester, width=40,font=('Lato', 13, 'normal'))
        Semester_entry.grid(row=3, column=1, padx=10, pady=10)


        # Action Buttons
        style = tb.Style()
        style.configure("mybutton.TButton",background="#007bff",bordercolor="#007bff",focuscolor="transparent",borderwidth=0 )
        style.map("mybutton.TButton",background=[("active", "#0056b3")]) # Change when pressed
        style.configure("mybutton2.TButton",background="#17a2b8",bordercolor="#17a2b8",focuscolor="transparent",borderwidth=0)
        style.map("mybutton2.TButton",background=[("active", "#138496")])
        style.configure("mybutton3.TButton",background="#ffc107",bordercolor="#ffc107",focuscolor="transparent",borderwidth=0 )
        style.map("mybutton3.TButton",background=[("active", "#e0a800")])
        style.configure("mybutton4.TButton",background="#28a745",bordercolor="#28a745",focuscolor="transparent" ,borderwidth=0)
        style.map("mybutton4.TButton",background=[("active", "#218838")])
        style.configure("mybutton5.TButton",background="#dc3545",bordercolor="#dc3545",focuscolor="transparent",borderwidth=0 )
        style.map("mybutton5.TButton",background=[("active", "#c82333")])

        save_bt = tb.Button(sub_frame_3, text="Save", command=self.add_data, style="mybutton.TButton", width=33)
        save_bt.grid(row=0, column=0, padx= 15,pady=7)

        update_bt = tb.Button(sub_frame_3, text="Update", command=self.update_data, style="mybutton2.TButton", width=33)
        update_bt.grid(row=1, column=0, padx= 4,pady=7)

        delete_bt = tb.Button(sub_frame_3, text="Delete", command=self.delete_data, style="mybutton3.TButton", width=33)
        delete_bt.grid(row=2, column=0, padx= 4,pady=7)

        reset_bt = tb.Button(sub_frame_3, text="Reset", command=self.reset_data, style="mybutton4.TButton", width=33)
        reset_bt.grid(row=3, column=0,padx= 4,pady=7)

        takephoto_bt = tb.Button(sub_frame_3, text="Take Photo Sample", command=self.take_photo_sample,style="mybutton5.TButton", width=33)
        takephoto_bt.grid(row=4, column=0,padx= 4,pady=7)


        #updatephoto_bt = tb.Button(sub_frame_3, text="Update Photo Sample", bootstyle="info", width=33)
        #updatephoto_bt.grid(row=5, column=0, pady=2)

        # Radio Buttons
        self.var_rad1 = StringVar()
        rad_bt = tb.Radiobutton(sub_frame_2, text="Take Photo Sample", variable=self.var_rad1, value="Yes", bootstyle="success")
        rad_bt.place(x=130, y=330)

        rad_bt2 = tb.Radiobutton(sub_frame_2, text="No Photo Sample", variable=self.var_rad1, value="No", bootstyle="danger")
        rad_bt2.place(x=400, y=330)

        # Table Frame
        #bottom_frame_2 = tb.Frame(bottom_frame, bootstyle="light", relief=RIDGE)
        #bottom_frame_2.place(x=5, y=50, width=1461, height=230)

        scroll_x = tb.Scrollbar(bottom_frame, orient=HORIZONTAL, bootstyle="secondary-round")
        scroll_y = tb.Scrollbar(bottom_frame, orient=VERTICAL, bootstyle="secondary-round")
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_details = tb.Treeview(bottom_frame, columns=("Name", "gender", "dob", "Phone", "mail", "Regno", "Department", "Branch", "Semester", "pss"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, bootstyle="success")
        scroll_x.config(command=self.student_details.xview)
        scroll_y.config(command=self.student_details.yview)

        self.student_details.heading("Name", text="Name")
        self.student_details.heading("gender", text="Gender")
        self.student_details.heading("dob", text="DOB")
        self.student_details.heading("Phone", text="Phone")
        self.student_details.heading("mail", text="Mail")
        self.student_details.heading("Regno", text="Register No")
        self.student_details.heading("Department", text="Department")
        self.student_details.heading("Branch", text="Branch")
        self.student_details.heading("Semester", text="Semester")
        self.student_details.heading("pss", text="Photo Sample Status")

        self.student_details["show"] = "headings"
        self.student_details.config(height=20)
        self.student_details.pack(fill=BOTH, expand=1)
        self.student_details.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    def add_data(self):
        conn = None  # Ensure conn is defined
        try:
            if (
                self.var_name.get() == "" or 
                self.var_gender.get() == "Select" or 
                self.var_dob.get() == "" or 
                self.var_ph.get() == "" or 
                self.var_mail.get() == "" or 
                self.var_regno.get() == "" or 
                self.var_dept.get() == "" or 
                self.var_branch.get() == "" or 
                self.var_semester.get() == "" or 
                self.var_rad1.get() == ""
            ):
                messagebox.showerror("Error", "Please fill all Fields", parent=self.root)
                return  # Exit function to prevent further execution

            print("Connecting to database...")  # Debug print

            conn = mysql.connector.connect(
                host="localhost", username="root", password="farook", database="faceapp"
            )
            my_cur = conn.cursor()

            print("Inserting data...")  # Debug print

            my_cur.execute(
                "INSERT INTO student (name, gender, dob, phone, mail, regno, dept, branch, semester, photo_st) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_ph.get(),
                    self.var_mail.get(),
                    self.var_regno.get(),
                    self.var_dept.get(),
                    self.var_branch.get(),
                    self.var_semester.get(),
                    self.var_rad1.get(),
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details are entered", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Unexpected Error: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
            my_cur = conn.cursor()
            my_cur.execute("SELECT * FROM student")
            data = my_cur.fetchall()

            if len(data) != 0:
                self.student_details.delete(*self.student_details.get_children())
                for row in data:
                    self.student_details.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)

    def get_cursor(self,event=""):
        cursor_focus=self.student_details.focus()
        content=self.student_details.item(cursor_focus)
        data=content["values"]
        self.var_name.set(data[0]),
        self.var_gender.set(data[1]),
        self.var_dob.set(data[2]),
        self.var_ph.set(data[3]),
        self.var_mail.set(data[4]),
        self.var_regno.set(data[5]),
        self.var_dept.set(data[6]),
        self.var_branch.set(data[7]),
        self.var_semester.set(data[8]),
        self.var_rad1.set(data[9])

    def update_data(self):
        if (
                self.var_name.get() == "" or 
                self.var_gender.get() == "Select" or 
                self.var_dob.get() == "" or 
                self.var_ph.get() == "" or 
                self.var_mail.get() == "" or 
                self.var_regno.get() == "" or 
                self.var_dept.get() == "" or 
                self.var_branch.get() == "" or 
                self.var_semester.get() == "" or 
                self.var_rad1.get() == ""
            ):
                messagebox.showerror("Error", "Please fill all Fields", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
                    my_cur = conn.cursor()
                    my_cur.execute("UPDATE student SET name=%s,gender=%s,dob=%s,phone=%s,mail=%s,dept=%s,branch=%s,semester=%s,photo_st=%s WHERE regno=%s",(
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_ph.get(),
                        self.var_mail.get(),
                        self.var_dept.get(),
                        self.var_branch.get(),
                        self.var_semester.get(),
                        self.var_rad1.get(),
                        self.var_regno.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_regno.get()=="":
            messagebox.showerror("Error","Register Number must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Record!","Do you want to delete the Selected Record?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
                    my_cur = conn.cursor()
                    my_cur.execute("DELETE FROM student WHERE regno=%s",(self.var_regno.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)
    
    def reset_data(self):
        self.var_name.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_ph.set(""),
        self.var_mail.set(""),
        self.var_regno.set(""),
        self.var_dept.set(""),
        self.var_branch.set(""),
        self.var_semester.set(""),
        self.var_rad1.set("")

    def take_photo_sample(self):
        if (
                self.var_name.get() == "" or 
                self.var_gender.get() == "Select" or 
                self.var_dob.get() == "" or 
                self.var_ph.get() == "" or 
                self.var_mail.get() == "" or 
                self.var_regno.get() == "" or 
                self.var_dept.get() == "" or 
                self.var_branch.get() == "" or 
                self.var_semester.get() == "" or 
                self.var_rad1.get() == ""
            ):
                messagebox.showerror("Error", "Please fill all Fields", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
                my_cur = conn.cursor()
                my_cur.execute("SELECT * FROM student")
                my_result=my_cur.fetchall()
                id=0
                for x in my_result:
                    id+=1
                my_cur.execute("UPDATE student SET name=%s,gender=%s,dob=%s,phone=%s,mail=%s,dept=%s,branch=%s,semester=%s,photo_st=%s WHERE regno=%s",(
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_ph.get(),
                        self.var_mail.get(),
                        self.var_dept.get(),
                        self.var_branch.get(),
                        self.var_semester.get(),
                        self.var_rad1.get(),
                        self.var_regno.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    face=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in face:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop
                    
                capure=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,frame_cap=capure.read()
                    if face_crop(frame_cap) is not None:
                        img_id+=1
                        face=cv2.resize(face_crop(frame_cap),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        path="Photos/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capure.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Results","Completed Generation",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)


if __name__ == "__main__":
    root = tb.Window(themename="litera")
    obj = studentdetails(root)
    root.mainloop()

                










        
        
        















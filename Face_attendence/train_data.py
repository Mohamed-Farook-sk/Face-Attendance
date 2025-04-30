import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import ttkbootstrap as tttk  
from ttkbootstrap.constants import *
import cv2
import os
import numpy as np

class traindata:

    def __init__(self, root):
        self.root = root  # Use the provided Toplevel window
        self.root.title("Train Data")
        
        self.root.geometry("1920x1080+0+0")
        self.root.configure(bg='cyan')

        bg_image = Image.open("background.jpg")  # Give correct path to your background image
        bg_image = bg_image.resize((1920, 1080))  # Resize it to match your window size
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tttk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.var_cvid=StringVar()
        self.var_roll=StringVar()

        ui_image = Image.open("train.jpg")  # Provide the correct path to your image (icon, etc.)
        ui_image = ui_image.resize((500, 500))  # Resize as needed
        self.ui_photo = ImageTk.PhotoImage(ui_image)

        # UI Image label (on top of the background)
        self.ui_label = tttk.Label(self.root, image=self.ui_photo)
        self.ui_label.place(x=1250,y=250)


        # Title Label with custom font and background color
        title_Label = tttk.Label(self.root, text="TRAIN DATA SET", font=("Ariel", 30, "bold"), bootstyle="inverse-danger", anchor="center")
        title_Label.pack(fill="x", pady=10)  # Use pack to span the width and add padding

        main_frame = tttk.Frame(self.root, bootstyle="default")
        main_frame.place(x=25, y=100, width=900, height=930)
        main_frame.grid_propagate(False)

        main_frame_2 = tttk.Labelframe(main_frame, text="ID Mapping", bootstyle="danger")
        main_frame_2.place(x=27, y=10, height=500, width=850)
        main_frame_2.grid_propagate(False)

        sub_frame_3 = tttk.Labelframe(main_frame, text="~~~",bootstyle="danger")
        sub_frame_3.place(x=27, y=716, height=200, width=850)
        sub_frame_3.grid_propagate(False)

        # Button style configuration using Style
        style = tttk.Style()
        style.configure("danger.TButton", font=("Helvetica", 16, "bold"), padding=(10, 20))

        # Train Data button with proper width, height, and style
        train_data_bt = tttk.Button(self.root,text="Train Data", command=self.train_class, style="danger.TButton",width=32)
        train_data_bt.place(x=1250, y=751)  # Use pack to align the button properly

        #ID FRAME
        scroll_x = tttk.Scrollbar(main_frame_2, orient=HORIZONTAL, bootstyle="secondary-round")
        scroll_y = tttk.Scrollbar(main_frame_2, orient=VERTICAL, bootstyle="secondary-round")
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.id_mapping = tttk.Treeview(main_frame_2, columns=("Opencv", "rollno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, bootstyle="Danger")
        scroll_x.config(command=self.id_mapping.xview)
        scroll_y.config(command=self.id_mapping.yview)

        self.id_mapping.heading("Opencv", text="OpenCv ID")
        self.id_mapping.heading("rollno", text="Register No")

        self.id_mapping["show"] = "headings"
        self.id_mapping.config(height=20)
        self.id_mapping.pack(fill=BOTH, expand=1)
        self.id_mapping.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

        #ENTRY FIELDS
        style = tttk.Style()
        style.configure('CustomLabel2.TLabel', font=('Lato', 13, 'normal'))

        opencvid = tttk.Label(main_frame, text="OpenCv ID:",style="CustomLabel2.TLabel")
        opencvid.place(x=80,y=556)

        opencvid_entry = tttk.Entry(main_frame, width=35,textvariable=self.var_cvid, font=('Lato', 13, 'normal'))
        opencvid_entry.place(x=250,y=550)

        RegisterNo = tttk.Label(main_frame, text="Register No:",style="CustomLabel2.TLabel")
        RegisterNo.place(x=80,y=621)

        RegisterNo_entry = tttk.Entry(main_frame, width=35,textvariable=self.var_roll,font=('Lato', 13, 'normal'))
        RegisterNo_entry.place(x=250,y=615)


        #ACTION BUTTON
        style = tttk.Style()
        style.configure("1mybutton2.TButton",background="#17a2b8",bordercolor="#17a2b8",focuscolor="transparent",borderwidth=0)
        style.map("1mybutton2.TButton",background=[("active", "#138496")])
        style.configure("1mybutton3.TButton",background="#ffc107",bordercolor="#ffc107",focuscolor="transparent",borderwidth=0 )
        style.map("1mybutton3.TButton",background=[("active", "#e0a800")])
        style.configure("1mybutton4.TButton",background="#28a745",bordercolor="#28a745",focuscolor="transparent" ,borderwidth=0)
        style.map("1mybutton4.TButton",background=[("active", "#218838")])
        style.configure("1mybutton5.TButton",background="#dc3545",bordercolor="#dc3545",focuscolor="transparent",borderwidth=0 )
        style.map("1mybutton5.TButton",background=[("active", "#c82333")])

        save_bt = tttk.Button(sub_frame_3, text="Save", command=self.add_data,style="1mybutton5.TButton", width=100)
        save_bt.grid(row=0, column=0, padx= 15,pady=7)

        update_bt = tttk.Button(sub_frame_3, text="Update",command=self.update_data,style="1mybutton2.TButton", width=100)
        update_bt.grid(row=1, column=0, padx= 4,pady=7)

        delete_bt = tttk.Button(sub_frame_3, text="Delete", command=self.delete_data,style="1mybutton3.TButton", width=100)
        delete_bt.grid(row=2, column=0, padx= 4,pady=7)

        reset_bt = tttk.Button(sub_frame_3, text="Reset",command=self.reset_data, style="1mybutton4.TButton", width=100)
        reset_bt.grid(row=3, column=0,padx= 4,pady=7)



    def train_class(self):
        Photos_dir = "Photos"
        path = [os.path.join(Photos_dir, file) for file in os.listdir(Photos_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        lbph = cv2.face.LBPHFaceRecognizer_create()
        lbph.train(faces, ids)
        lbph.write("Train.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Data Set Training Completed",parent=self.root)

    #FETCH DATA
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
            my_cur = conn.cursor()
            my_cur.execute("SELECT * FROM id_mapping")
            data = my_cur.fetchall()

            if len(data) != 0:
                self.id_mapping.delete(*self.id_mapping.get_children())
                for row in data:
                    self.id_mapping.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error fetching data: {str(es)}", parent=self.root)

    #get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.id_mapping.focus()
        content=self.id_mapping.item(cursor_focus)
        data=content["values"]
        self.var_cvid.set(data[0]),
        self.var_roll.set(data[1])
    
    #reset 
    def reset_data(self):
        self.var_cvid.set(""),
        self.var_roll.set(""),
    #save
    def add_data(self):
        conn = None
        try:
            if (
                self.var_cvid.get() == "" or 
                self.var_roll.get() == ""
                
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
                "INSERT INTO id_mapping (opencv_id,roll_no) VALUES (%s,%s)",
                (
                    self.var_cvid.get(),
                    self.var_roll.get()
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "New ID is Mapped", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Unexpected Error: {str(es)}", parent=self.root)

    def update_data(self):
        if (
                self.var_cvid.get() == "" or 
                self.var_roll.get() == "" 
            ):
                messagebox.showerror("Error", "Please fill all Fields", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
                    my_cur = conn.cursor()
                    my_cur.execute("UPDATE id_mapping SET roll_no=%s WHERE opencv_id=%s",
                    (
                        self.var_roll.get(),   # correct order
                            self.var_cvid.get()
                            )
                                )
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Updated Successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)
    #delete
    def delete_data(self):
        if self.var_cvid.get()=="":
            messagebox.showerror("Error","CV ID must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete Record!","Do you want to delete the Selected Record?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="farook", database="faceapp")
                    my_cur = conn.cursor()
                    my_cur.execute("DELETE FROM id_mapping WHERE opencv_id=%s",(self.var_cvid.get(),))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)

if __name__ == "__main__":
    root = tttk.Window(themename="litera")
    obj = traindata(root)
    root.mainloop()

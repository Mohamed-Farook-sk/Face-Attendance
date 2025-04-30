import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import mysql.connector
import cv2
import os
import csv
import ttkbootstrap as tb 
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from tkinter import StringVar

mydata=[]
class attendence:

    def __init__(self, root):
        self.root = root  
        self.root.title("Attendence")
        self.root.geometry("1920x1080+0+0")
        self.root.configure(bg='cyan')

        bg_image = Image.open("background.jpg")  # Give correct path to your background image
        bg_image = bg_image.resize((1920, 1080))  # Resize it to match your window size
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        self.bg_label = tb.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #var
        self.var_stu_name=StringVar()
        self.var_regno=StringVar()
        self.var_dept=StringVar()
        self.var_branch=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_atts=StringVar()


        #frame
        title_Label = tb.Label(self.root, text="STUDENT ATTENDENCE", font=("Helvetica", 14, "bold"),bootstyle="inverse-info", anchor=CENTER, padding=10)
        title_Label.pack(fill=tb.X)

        main_frame = tb.Frame(self.root, bootstyle="default")
        main_frame.place(x=15, y=70, width=1878, height=950)
        main_frame.grid_propagate(False)

        main_frame_2 = tb.Labelframe(main_frame,text="~",bootstyle="primary")
        main_frame_2.place(x=10, y=10, height=921, width=1854)
        main_frame_2.grid_propagate(False)

        left_frame = tb.Labelframe(main_frame_2, text="Student Attendence Details", bootstyle="info")
        left_frame.place(x=26, y=0, height=878, width=890)
        left_frame.grid_propagate(False)

        right_frame = tb.Labelframe(main_frame_2, text="Attendence Details", bootstyle="info")
        right_frame.place(x=935, y=0, height=878, width=890)
        right_frame.grid_propagate(False)

        #left_frame= tb.Labelframe(left_frame, text="~", bootstyle="info")
        #left_frame.place(x=13,y=620,height=200,width=863)

        #labes

        style = tb.Style()
        style.configure('CustomLabel.TLabel', font=('Lato', 13, 'normal'))

        student_name = tb.Label(left_frame, text="Student Name:",style="CustomLabel.TLabel")
        student_name.grid(row=0, column=0, padx=10, pady=25)

        student_name_entry = tb.Entry(left_frame, width=40, textvariable=self.var_stu_name,font=('Lato', 13, 'normal'))
        student_name_entry.grid(row=0, column=1, padx=10, pady=10)


        roll_no=tb.Label(left_frame, text="Register Number:", style="CustomLabel.TLabel")
        roll_no.grid(row=1, column=0, padx=10, pady=25,)

        roll_no_entry= tb.Entry(left_frame, width=40,textvariable=self.var_regno, font=('Lato', 13, 'normal'))
        roll_no_entry.grid(row=1, column=1, padx=10, pady=25,)

        dept=tb.Label(left_frame, text="Department:", style="CustomLabel.TLabel")
        dept.grid(row=2,column=0,padx=10,pady=25)

        dept_entry= tb.Entry(left_frame, width=40,textvariable=self.var_dept,font=('Lato', 13, 'normal'))
        dept_entry.grid(row=2,column=1,padx=10,pady=25)

        branch=tb.Label(left_frame, text="Branch:",style="CustomLabel.TLabel")
        branch.grid(row=3,column=0,padx=10,pady=25)

        branch_entry= tb.Entry(left_frame, width=40,textvariable=self.var_branch, font=('Lato', 13, 'normal'))
        branch_entry.grid(row=3,column=1,padx=10,pady=25)

        date=tb.Label(left_frame, text="Date:",style="CustomLabel.TLabel")
        date.grid(row=4,column=0,padx=10,pady=25)

        date_entry= tb.Entry(left_frame, width=40, textvariable=self.var_date,font=('Lato', 13, 'normal'))
        date_entry.grid(row=4,column=1,padx=10,pady=25)

        time=tb.Label(left_frame, text="Time:",style="CustomLabel.TLabel")
        time.grid(row=5,column=0,padx=10,pady=25)

        time_entry= tb.Entry(left_frame, width=40, textvariable=self.var_time,font=('Lato', 13, 'normal'))
        time_entry.grid(row=5,column=1,padx=10,pady=25)

        Att_st=tb.Label(left_frame, text="Attendance Status:",style="CustomLabel.TLabel")
        Att_st.grid(row=6,column=0,padx=10,pady=25)

        Att_combo = tb.Combobox(left_frame,font=('Lato', 13, 'normal'),textvariable=self.var_atts,width=38, state="readonly")
        Att_combo["values"] = ("Select", "Present", "Absent")
        Att_combo.current(0)
        Att_combo.grid(row=6, column=1, padx=10, pady=10)

    #style
        style = tb.Style()
        style.configure("abutton.TButton",background="#17a2b8",bordercolor="#17a2b8",font=("Lato", 16, "normal"),focuscolor="transparent",borderwidth=0)
        style.map("abutton.TButton",background=[("active", "#138496")])
    #button

        import_csv_bt=tb.Button(left_frame, text="Import csv",command=self.importcsv,style="abutton.TButton", width=57)
        import_csv_bt.place(x=6,y=674)

        export_csv_bt=tb.Button(left_frame, text="Export csv",command=self.exportcsv, style="abutton.TButton", width=57)
        export_csv_bt.place(x=6,y=716)

        Update_bt=tb.Button(left_frame, text="Update",command=self.update_data,style="abutton.TButton", width=57)
        Update_bt.place(x=6,y=758)

        reset_bt=tb.Button(left_frame, text="Reset",command=self.reset_data, style="abutton.TButton", width=57)
        reset_bt.place(x=6,y=800)
    
    #Table

        scroll_x = tb.Scrollbar(right_frame, orient=HORIZONTAL, bootstyle="secondary-round")
        scroll_y = tb.Scrollbar(right_frame, orient=VERTICAL, bootstyle="secondary-round")
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_attendence_details = tb.Treeview(right_frame, columns=("Name", "regno", "dept", "branch", "date", "time", "atts"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set, bootstyle="info")
        scroll_x.config(command=self.student_attendence_details.xview)
        scroll_y.config(command=self.student_attendence_details.yview)

        self.student_attendence_details.heading("Name", text="Name")
        self.student_attendence_details.heading("regno", text="Register Number")
        self.student_attendence_details.heading("dept", text="Department")
        self.student_attendence_details.heading("branch", text="Branch")
        self.student_attendence_details.heading("date", text="Date")
        self.student_attendence_details.heading("time", text="Time")
        self.student_attendence_details.heading("atts", text="Attendance Status")

        self.student_attendence_details["show"] = "headings"
        self.student_attendence_details.config(height=20)
        self.student_attendence_details.pack(fill=BOTH, expand=1)
        self.student_attendence_details.bind("<ButtonRelease>", self.getcursor)

    #fetching data

    def fetchdata(self,rows):
        self.student_attendence_details.delete(*self.student_attendence_details.get_children())
        for i in rows:
            self.student_attendence_details.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        file_name =filedialog.askopenfilename(initialdir=os.getcwd(),title="Open",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    #export
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data Found to Export",parent=self.root)
                return False
            file_name =filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(file_name,mode="w",newline="") as myfile:
                export = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export.writerow(i)
                messagebox.showinfo("INFO!","Your Data Exported to "+os.path.basename(file_name)+" Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Unexpected Error: {str(es)}", parent=self.root)      

    def getcursor(self,event=""):
        cursor_row = self.student_attendence_details.focus()
        content = self.student_attendence_details.item(cursor_row)
        rows=content['values']
        self.var_stu_name.set(rows[0])
        self.var_regno.set(rows[1])
        self.var_dept.set(rows[2])
        self.var_branch.set(rows[3])
        self.var_date.set(rows[4])
        self.var_time.set(rows[5])
        self.var_atts.set(rows[6])

    def reset_data(self):
        self.var_stu_name.set("")
        self.var_regno.set("")
        self.var_dept.set("")
        self.var_branch.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_atts.set("")
    
    def update_data(self):
        try:
            selected = self.student_attendence_details.focus()
            if not selected:
                messagebox.showerror("Error", "No record selected to update", parent=self.root)
                return

            # Get updated data from entry fields
            updated_row = [
                self.var_stu_name.get(),
                self.var_regno.get(),
                self.var_dept.get(),
                self.var_branch.get(),
                self.var_date.get(),
                self.var_time.get(),
                self.var_atts.get()
            ]

            # Update in Treeview
            self.student_attendence_details.item(selected, values=updated_row)

            # Also update in the mydata list
            index = self.student_attendence_details.index(selected)
            mydata[index] = updated_row

            messagebox.showinfo("Success", "Record updated successfully", parent=self.root)

        except Exception as es:
            messagebox.showerror("Error", f"Error updating record: {str(es)}", parent=self.root)






if __name__ == "__main__":
    root = tb.Window(themename="litera")
    obj = attendence(root)
    root.mainloop()
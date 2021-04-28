from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk


#import random
#from time import strftime
#from datetime import datetime



class DetailsRoom:
    def __init__(self, root):

        self.root = root
        self.root.title("Room Details Page")
        self.root.geometry("1140x480+225+220")

        ####title*****
        lbl_title = Label(self.root, text='ROOM BOOKING DETAILS', font=('times new roman', 18, 'bold'), fg='gold',
                          bg='black', relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1400, height=50)

        ####logo***
        img2 = Image.open("F:\Hotel\Images\logo.jpg")
        img2 = img2.resize((230, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbling = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbling.place(x=0, y=0, width=200, height=50)

        ####label frame*****
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text='New Room Add',
                                    font=('times new roman', 12, 'bold'), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # Labels and entry fields
        # Floor
        lbl_floor = Label(labelframeleft, text='Floor', font=('times new roman', 12, 'bold'), padx=2,
                                 pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W,padx=20)

        self.var_floor=StringVar()

        entry_floor = ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20, font=('arial', 13, 'bold'))
        entry_floor.grid(row=0, column=1, sticky=W)

        # room no
        lbl_RoomNo = Label(labelframeleft, text='Room No', font=('times new roman', 12, 'bold'), padx=2,
                          pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W,padx=20)

        self.var_roomNo=StringVar()

        entry_RoomNo = ttk.Entry(labelframeleft,textvariable=self.var_roomNo, width=20, font=('arial', 13, 'bold'))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # room type
        lbl_RoomType = Label(labelframeleft, text='Room Type', font=('times new roman', 12, 'bold'), padx=2,
                           pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W, padx=20)

        self.var_RoomType=StringVar()
        entry_RoomType = ttk.Entry(labelframeleft, textvariable=self.var_RoomType, width=20, font=('arial', 13, 'bold'))
        entry_RoomType.grid(row=2, column=1, sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text='Add',command=self.add_data,font=('times new roman', 12, 'bold'), bg='black',
                        fg='gold', width=10)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame,command=self.update, text='Update',font=('times new roman', 12, 'bold'),
                           bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame,command=self.mDelete, text='Delete',font=('times new roman', 12, 'bold'),
                           bg='black', fg='gold', width=10)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame,command=self.reset_data, text='Reset',font=('times new roman', 12, 'bold'), bg='black',
                          fg='gold', width=10)
        btnReset.grid(row=0, column=3)


        #label frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='Show Room Details',
                                    font=('times new roman', 12, 'bold'), padx=2)
        Table_Frame.place(x=590, y=55, width=530, height=350)


        #scroll bar
        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, column=('floor','roomno', 'roomType',
                                                              ),
                                       xscrollcommand=scroll_x.set,
                                       yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('floor', text='Floor')
        self.room_table.heading('roomno', text='Room No')
        self.room_table.heading('roomType', text='Room Type')


        self.room_table['show'] = 'headings'
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    #add data
    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror('Error', 'all fields required', parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root",
                                               password="2589", database='management')

                my_cursor = conn.cursor()
                my_cursor.execute('insert into details values(%s,%s,%s)'
                                  , (        self.var_floor.get(),
                                             self.var_roomNo.get(),
                                             self.var_RoomType.get(),

                                             ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'New room added successfully', parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning", f"something went wrong:{str(es)}", parent=self.root)

    # FETCH DATA
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='2589', database='management')

        my_cursor = conn.cursor()
        my_cursor.execute('select * from details')

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('', END, values=i)

            conn.commit()
        conn.close()



    #get cursor

    def get_cursor(self, event=''):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_RoomType.set(row[2])

        # update function

    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error", "please enter floor number", parent=self.root)

        else:

            conn = mysql.connector.connect(host='localhost', user='root',
                                           password='2589', database='management')

            my_cursor = conn.cursor()
            my_cursor.execute(
                'update details set Floor=%s,RoomType=%s where RoomNo=%s',
                (

                    self.var_floor.get(),
                    self.var_RoomType.get(),
                    self.var_roomNo.get(),

                ))

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'New Room details has been udated successfully', parent=self.root)

    # Delete function

    def mDelete(self):
        mDelete = messagebox.askyesno('Hotel Management System', 'Do you want to delete this room details?',
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host='localhost', user='root',
                                           password='2589', database='management')

            my_cursor = conn.cursor()
            query = 'delete from details where RoomNo=%s'
            value = (self.var_roomNo.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")


if __name__ == "__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()
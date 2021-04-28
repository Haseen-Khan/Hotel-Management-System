from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import random
from time import strftime
from datetime import datetime



class Roombooking:
    def __init__(self, root):

        self.root = root
        self.root.title("Room Booking Page")
        self.root.geometry("1140x480+225+220")

        ##variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()


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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE,text='Room Booking Details',font=('times new roman',12,'bold'),padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)


        #Labels and entry fields
        # customer contact
        lbl_cust_contact = Label(labelframeleft, text='Customer Contact', font=('times new roman', 12, 'bold'), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact,width=20, font=('arial', 13, 'bold'))
        entry_contact.grid(row=0, column=1,sticky=W)

        #Fetch data Button
        btnFetchData = Button(labelframeleft, text='Fetch Data',command=self.Fetch_contact, font=('times new roman', 12, 'bold'), bg='black',
                        fg='gold', width=8)
        btnFetchData.place(x=330,y=4)

        # check in date
        check_in_date = Label(labelframeleft, text='Check In Date', font=('times new roman', 12, 'bold'), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft,width=29,textvariable=self.var_checkin ,font=('arial', 13, 'bold'))
        txtcheck_in_date.grid(row=1, column=1)

        # check  out date
        lbl_Check_out = Label(labelframeleft, text='Check Out Date', font=('times new roman', 12, 'bold'), padx=2,
                              pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, width=29,textvariable=self.var_checkout, font=('arial', 13, 'bold'))
        txt_Check_out.grid(row=2, column=1)

        #room type
        label_RoomType = Label(labelframeleft, text='Room Type', font=('times new roman', 12, 'bold'), padx=2,
                              pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host='localhost', user='root', password='2589', database='management')

        my_cursor = conn.cursor()
        my_cursor.execute('select RoomType from details')
        ide = my_cursor.fetchall()



        combo_RoomType = ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=('arial', 12, 'bold'), width=27,
                                    state='readonly')
        combo_RoomType['value'] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)


        # available room
        lblRoomAvailable = Label(labelframeleft,text='Available Room',font=('times new roman', 12, 'bold'), padx=2,
                              pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

       # txtRoomAvailable = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, width=29, font=('arial', 13, 'bold'))
        #txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host='localhost', user='root', password='2589', database='management')

        my_cursor = conn.cursor()
        my_cursor.execute('select RoomNo from details')
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=('arial', 12, 'bold'),
                                      width=27,
                                      state='readonly')
        combo_RoomNo['value'] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        #Meal
        lblMeal = Label(labelframeleft, text='Meal', font=('times new roman', 12, 'bold'), padx=2,
                                 pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal,width=29, font=('arial', 13, 'bold'))
        txtMeal.grid(row=5, column=1)

        # No of days
        lblNoOfDays = Label(labelframeleft, text='No of Days', font=('times new roman', 12, 'bold'), padx=2,
                                 pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, width=29, font=('arial', 13, 'bold'))
        txtNoOfDays.grid(row=6, column=1)


        #Paid tax
        lblPaidTax = Label(labelframeleft, text='Paid Tax', font=('times new roman', 12, 'bold'), padx=2,
                                 pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft,textvariable=self.var_paidtax, width=29, font=('arial', 13, 'bold'))
        txtPaidTax.grid(row=7, column=1)

        #Sub Total
        lblSubTotal = Label(labelframeleft, text='Sub Total', font=('times new roman', 12, 'bold'), padx=2,
                                 pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft,textvariable=self.var_actualtotal, width=29, font=('arial', 13, 'bold'))
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, text='Total Cost', font=('times new roman', 12, 'bold'), padx=2,
                                 pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft,textvariable=self.var_total, width=29, font=('arial', 13, 'bold'))
        txtTotalCost.grid(row=9, column=1)


        #bill button

        btnBill = Button(labelframeleft, text='Bill',command=self.total, font=('times new roman', 12, 'bold'), bg='black',
                        fg='gold', width=10)
        btnBill.grid(row=10, column=0,sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=380, width=412, height=40)

        btnAdd = Button(btn_frame, text='Add',command=self.add_data,font=('times new roman', 12, 'bold'), bg='black',
                        fg='gold', width=10)
        btnAdd.grid(row=0, column=0)

        btnUpdate = Button(btn_frame, text='Update',command=self.update,font=('times new roman', 12, 'bold'),
                           bg='black', fg='gold', width=10)
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btn_frame, text='Delete',command=self.mDelete, font=('times new roman', 12, 'bold'),
                           bg='black', fg='gold', width=10)
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btn_frame, text='Reset',command=self.reset, font=('times new roman', 12, 'bold'), bg='black',
                          fg='gold', width=10)
        btnReset.grid(row=0, column=3)

        #right side image
        img3 = Image.open("F:\Hotel Management System\images\Room.jpg")
        img3 = img3.resize((360,200), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbling = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbling.place(x=760, y=55, width=360, height=200)

        ##table frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text='View Details and Search System',
                                    font=('times new roman', 12, 'bold'), padx=2)
        Table_Frame.place(x=435, y=270, width=860, height=260)

        lblSearchBy = Label(Table_Frame, text='Search By', font=('Arial', 12, 'bold'),bg='red',fg='white')
        lblSearchBy.grid(row=0, column=0, sticky=W,padx=2)


        self.search_var =StringVar()
        combo_Search= ttk.Combobox(Table_Frame,textvariable=self.search_var,
                                font=('arial', 12, 'bold'), width=20, state='readonly')
        combo_Search['value'] = ('Contact', 'Room')
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)


        self.txt_search= StringVar()
        txtSearch = ttk.Entry(Table_Frame, width=20,textvariable=self.txt_search, font=('arial', 13, 'bold'))
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame, text='Search',command=self.search,font=('arial', 11, 'bold'), bg='black', fg='gold', width=7)
        btnSearch.grid(row=0, column=3,padx=1)

        btnShowAll = Button(Table_Frame, text='Show All',command=self.fetch_data, font=('arial', 11, 'bold'), bg='black', fg='gold',
                           width=7)
        btnShowAll.grid(row=0, column=4,padx=1)


        ####show data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=690, height=140)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, column=('contact', 'checkin', 'checkout', 'roomtype',
                                                                      'roomavailable', 'meal', 'noOfdays'), xscrollcommand=scroll_x.set,
                                               yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading('contact', text='Contact')
        self.room_table.heading('checkin', text='Check-in')
        self.room_table.heading('checkout', text='Check-out')
        self.room_table.heading('roomtype', text='Room Type')
        self.room_table.heading('roomavailable', text='Room No')
        self.room_table.heading('meal', text='Meal')
        self.room_table.heading('noOfdays', text='NoOfDays')


        self.room_table['show'] = 'headings'
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #add data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror('Error', 'all fields required',parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",
                                             password="2589",database='management')

                my_cursor = conn.cursor()
                my_cursor.execute('insert into room values(%s,%s,%s,%s,%s,'
                                  '%s,%s)',(  self.var_contact.get(),
                                              self.var_checkin.get(),
                                              self.var_checkout.get(),
                                              self.var_roomtype.get(),
                                              self.var_roomavailable.get(),
                                              self.var_meal.get(),
                                              self.var_noofdays.get()
                                              ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','room has been booked',parent=self.root)

            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong:{str(es)}",parent=self.root)



    #get cursor

    def get_cursor(self, event=''):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content['values']

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])


    # update function
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "please enter mobile number", parent=self.root)

        else:

            conn = mysql.connector.connect(host='localhost', user='root',
                                           password='2589', database='management')

            my_cursor = conn.cursor()
            my_cursor.execute(
                'update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s',
                                                                                                     (

                                                                                                    self.var_checkin.get(),
                                                                                                    self.var_checkout.get(),
                                                                                                    self.var_roomtype.get(),
                                                                                                    self.var_roomavailable.get(),
                                                                                                    self.var_meal.get(),
                                                                                                    self.var_noofdays.get(),
                                                                                                    self.var_contact.get()
                                                                                                 ))


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('Update', 'Room details has been udated successfully', parent=self.root)

    # Delete function
    def mDelete(self):
        mDelete = messagebox.askyesno('Hotel Management System', 'Do you want to delete this customer?',
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host='localhost', user='root',
                                           password='2589', database='management')

            my_cursor = conn.cursor()
            query = 'delete from room where Contact=%s'
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return

        conn.commit()
        self.fetch_data()
        conn.close()

    #reset
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")


    # FETCH DATA
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', user='root', password='2589', database='management')

        my_cursor = conn.cursor()
        my_cursor.execute('select * from room')

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert('', END, values=i)

            conn.commit()
        conn.close()




    # fetch CONTACT
    def Fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "please enter contact number", parent=self.root)

        else:

            conn = mysql.connector.connect(host='localhost', user='root',
                                           password='2589', database='management')

            my_cursor = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row= my_cursor.fetchone()

            if row == None:
                messagebox.showerror('Error','This number not found',parent=self.root)

            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE,padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                #name
                lblName=Label(showDataframe,text='Name:',font=('arial',12,'bold'))
                lblName.place(x=0,y=0)

                lbl= Label(showDataframe,text=row,font=('arial',12,'bold'))
                lbl.place(x=90,y=0)

                #gender
                conn = mysql.connector.connect(host='localhost', user='root',
                                               password='2589', database='management')

                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text='Gender:', font=('arial', 12, 'bold'))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl2.place(x=90, y=30)

                #Email
                conn = mysql.connector.connect(host='localhost', user='root',
                                               password='2589', database='management')

                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showDataframe, text='Email:', font=('arial', 12, 'bold'))
                lblemail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl3.place(x=90, y=60)


                #nationality
                conn = mysql.connector.connect(host='localhost', user='root',
                                               password='2589', database='management')

                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataframe, text='Nationality:', font=('arial', 12, 'bold'))
                lblNationality.place(x=0, y=90)

                lbl4 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl4.place(x=90, y=90)

                #address
                conn = mysql.connector.connect(host='localhost', user='root',
                                               password='2589', database='management')

                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladdress = Label(showDataframe, text='Address:', font=('arial', 12, 'bold'))
                lbladdress.place(x=0, y=120)

                lbl5 = Label(showDataframe, text=row, font=('arial', 12, 'bold'))
                lbl5.place(x=90, y=120)


    #search system Function
    def search(self):
        conn = mysql.connector.connect(host='localhost', user='root',
                                       password='2589', database='management')

        my_cursor = conn.cursor()
        my_cursor.execute(
            "select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(
                self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    def total(self):
        inDate = self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate = datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if self.var_meal.get()=='Breakfast' and self.var_roomtype.get()=='Luxury':
            q1=float(600)
            q2=float(5000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="TK. "+str("%.2f"%((q5)*0.1))
            ST="TK. "+str("%.2f"%((q5)))
            TT="TK. "+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == 'Beakfast' and self.var_roomtype.get() == 'Single':
            q1 = float(600)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "TK. " + str("%.2f" % ((q5) * 0.1))
            ST = "TK. " + str("%.2f" % ((q5)))
            TT = "TK. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == 'Breakfast' and self.var_roomtype.get() == 'Double':
            q1 = float(600)
            q2 = float(3500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "TK. " + str("%.2f" % ((q5) * 0.1))
            ST = "TK. " + str("%.2f" % ((q5)))
            TT = "TK. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == 'Lunch' and self.var_roomtype.get() == 'Single':
            q1 = float(1000)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "TK. " + str("%.2f" % ((q5) * 0.1))
            ST = "TK. " + str("%.2f" % ((q5)))
            TT = "TK. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif self.var_meal.get() == 'Dinner' and self.var_roomtype.get() == 'Double':
            q1 = float(1200)
            q2 = float(3500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)
            Tax = "TK. " + str("%.2f" % ((q5) * 0.1))
            ST = "TK. " + str("%.2f" % ((q5)))
            TT = "TK. " + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)






if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
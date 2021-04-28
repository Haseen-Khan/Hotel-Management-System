from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")


        #variable***
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_conpass = StringVar()




        # background image*******
        self.bg = ImageTk.PhotoImage(file=r"F:\Hotel Management System\images\reg1.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        #left image***
        self.bg1 = ImageTk.PhotoImage(file=r"F:\Hotel Management System\images\regleft.png")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=400, height=500)


        #frame****
        frame = Frame(self.root, bg="white")
        frame.place(x=450, y=100, width=800, height=500)


        #register label
        register_lbl = Label(frame, text='REGISTER HERE',font=('times new roman', 20, 'bold'), fg='darkgreen',bg='white')
        register_lbl.place(x=20, y=20)

        #label and entry field
        fname = Label(frame, text='First Name', font=('times new roman', 15, 'bold'), bg='white')
        fname.place(x=50, y=100)

        self.fname = ttk.Entry(frame,textvariable=self.var_fname, font=('times new roman', 15, 'bold'))
        self.fname.place(x=50, y=130,width=250)

        l_name = Label(frame, text='Last Name', font=('times new roman', 15, 'bold'), fg='black',bg='white')
        l_name.place(x=370, y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=('times new roman',15))
        self.txt_lname.place(x=370,y=130,width=250)

        ##*****row 2*****

        contact = Label(frame, text='Contact No', font=('times new roman', 15, 'bold'), bg='white')
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact ,font=('times new roman', 15, 'bold'))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text='Email', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email ,font=('times new roman', 15))
        self.txt_email.place(x=370, y=200, width=250)

        ##row 3*****
        security_Q = Label(frame,text='Select Security Questions', font=('times new roman', 15, 'bold'), bg='white')
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame,textvariable=self.var_securityQ, font=('times new roman', 15, 'bold'), state='readonly')
        self.combo_security_Q['values']=('Select','Your birth place','Your pet name')
        self.combo_security_Q.place(x=50, y=270,width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text='Security Answer', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA,font=('times new roman', 15))
        self.txt_security.place(x=370, y=270, width=250)


        ##row 4****

        pswd = Label(frame, text='Password', font=('times new roman', 15, 'bold'), bg='white')
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass,font=('times new roman', 15, 'bold'))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text='Confirm Password', font=('times new roman', 15, 'bold'), fg='black', bg='white')
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_conpass,font=('times new roman', 15))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        ### check buttons
        self.var_check=IntVar()
        checkbtn = Checkbutton(frame,variable=self.var_check, text='I Agree to The Terms and Conditions', font=('times new roman', 13, 'bold'),onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)

        ###buttons*****
        img = Image.open(r"F:\Hotel Management System\images\registernow.jpg")
        img = img.resize((200, 55), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1=Button(frame, image=self.photoimage,command=self.register_data,borderwidth=0, cursor='hand2',font=('times new roman',15,'bold'))
        b1.place(x=10,y=420,width=300)

        img1 = Image.open(r"F:\Hotel Management System\images\loginnow.jpg")
        img1 = img1.resize((200, 45), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, command=self.return_login,borderwidth=0, cursor='hand2', font=('times new roman', 15, 'bold'))
        b2.place(x=330, y=420, width=300)


        ###function declaration*****
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'all fields required',parent=self.root)

        elif self.var_pass.get() != self.var_conpass.get() :
            messagebox.showinfo('Success', 'password and confirm password must be same',parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror('Invalid', 'please agree to the terms and conditions',parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root",
                                           password="2589", database='management')

            my_cursor = conn.cursor()
            query = ('select * from register where email=%s')
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror('Error','user already exists, please try another email',parent=self.root)
            else:
                my_cursor.execute('insert into register values(%s,%s,%s,%s,%s,%s,%s)',(
                                                            self.var_fname.get(),
                                                            self.var_lname.get(),
                                                            self.var_contact.get(),
                                                            self.var_email.get(),
                                                            self.var_securityQ.get(),
                                                            self.var_securityA.get(),
                                                            self.var_pass.get()
                ))

            conn.commit()
            conn.close()
            messagebox.showinfo('success','registered successfully!',parent=self.root)

    def return_login(self):
        self.root.destroy()








if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
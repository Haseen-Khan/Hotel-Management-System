import sys
sys.path.append("..")

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from View.hotel import HotelManagementSystem


def main():
    win=Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")


        self.bg = ImageTk.PhotoImage(file = r"F:\Hotel Management System\images\h2.jpg")
        lbl_bg = Label(self.root, image = self.bg)
        lbl_bg.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        frame = Frame(self.root, bg = "black")
        frame.place(x = 570, y = 150, width = 340, height = 450)

        img1 = Image.open(r"F:\Hotel Management System\images\login1.png")
        img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image= self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x= 700, y= 170, width = 100, height= 100)

        get_str = Label(frame, text='Get Started', font=('times new roman',20,'bold'),fg='white',bg='black')
        get_str.place(x=105,y=120)


        #label
        username =lbl = Label(frame, text='Username', font=('times new roman', 20, 'bold'), fg='white', bg='black')
        username.place(x=75, y=160)

        self.txtuser=ttk.Entry(frame,  font=('times new roman', 15,'bold'))
        self.txtuser.place(x=40,y=195,width=270)

        password = lbl = Label(frame, text='Password', font=('times new roman', 20, 'bold'), fg='white', bg='black')
        password.place(x=75, y=225)

        self.txtpass = ttk.Entry(frame, font=('times new roman', 15, 'bold'))
        self.txtpass.place(x=40, y=260, width=270)

        #*****icon image*******#
        img2 = Image.open(r"F:\Hotel Management System\images\login1.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=615, y=315, width=25, height=25)

        img3 = Image.open(r"F:\Hotel Management System\images\password.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=615, y=380, width=25, height=25)

        #****login button******
        loginbtn = Button(frame,command=self.login, text='Login',font=('times new roman', 15, 'bold'),bd=3,relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
        loginbtn.place(x=110,y=305,width=120,height=35)

        #register button

        loginbtn = Button(frame, text='Create New Account', command=self.register_window,font=('times new roman', 10, 'bold'), borderwidth=0,fg='white',bg='black', activeforeground='white', activebackground='black')
        loginbtn.place(x=18, y=350, width=160)

        #forget pass button
        loginbtn = Button(frame, text='Forgot Password', command=self.forgot_password_window,font=('times new roman', 10, 'bold'), borderwidth=0, fg='white',bg='black', activeforeground='white', activebackground='black')
        loginbtn.place(x=10, y=370, width=160)



    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app= Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror('Error','all fields required')

        elif self.txtuser.get() == "Haseen" or self.txtpass.get() == "123":
            messagebox.showinfo('Success', 'Welcome')
        else:
            conn = mysql.connector.connect(host="localhost", user="root",
                                           password="2589", database='management')

            my_cursor = conn.cursor()
            my_cursor.execute('select * from register where email=%s and password=%s',(
                                                                        self.txtuser.get(),
                                                                        self.txtpass.get()

                                                                            ))
            row= my_cursor.fetchone()
            #print(row)
            if row== None:
                messagebox.showerror("Error","inalid username and password")
            else:
                open_main=messagebox.askyesno('YesNo',"Access only admin")
                if open_main>0:
                     self.new_window= Toplevel(self.root)
                     self.app= HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return


            conn.commit()
            conn.close()


    ##reset password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror('Error','Select the secutrity question',parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror('Error','please enter the answer',parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror('Error','please enter new password',parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root",
                                           password="2589", database='management')

            my_cursor = conn.cursor()
            qury=('select * from register where email=%s and securityQ=%s and securityA=%s')
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,value)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter correct answer",parent=self.root2)
            else:
                query=('update register set password=%s where email=%s')
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with new password",parent=self.root2)
                self.root2.destroy()




    #forgot password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","please enter the Email address to reset password",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root",
                                           password="2589", database='management')

            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value= (self.txtuser.get(), )
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
           # print(row)

            if row == None:
                messagebox.showerror('Error','please enter the valid username',parent=self.root)
            else:
                conn.close()
                self.root2= Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x440+570+160")

                l = Label(self.root2,text='Forgot password',font=('times new roman', 20, 'bold'),bd=3,relief=RIDGE,fg='red',bg='white')
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text='Select Security Questions', font=('times new roman', 15, 'bold'),
                                   bg='white')
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=('times new roman', 15, 'bold'), state='readonly')
                self.combo_security_Q['values'] = ('Select', 'Your birth place', 'Your pet name')
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text='Security Answer', font=('times new roman', 15, 'bold'), fg='black',
                                   bg='white')
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,font=('times new roman', 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text='New Password', font=('times new roman', 15, 'bold'), fg='black',
                                   bg='white')
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=('times new roman', 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2,text='RESET',command=self.reset_pass,font=('times new roman',15,'bold'),fg='white',bg='green')
                btn.place(x=100,y=290)






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
            messagebox.showerror('Error', 'all fields required')

        elif self.var_pass.get() != self.var_conpass.get() :
            messagebox.showinfo('Success', 'password and confirm password must be same')
        elif self.var_check.get()==0:
            messagebox.showerror('Invalid', 'please agree to the terms and conditions')
        else:
            conn = mysql.connector.connect(host="localhost", user="root",
                                           password="2589", database='management')

            my_cursor = conn.cursor()
            query = ('select * from register where email=%s')
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row!= None:
                messagebox.showerror('Error','user already exists, please try another email')
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
            messagebox.showinfo('success','registered successfully!')

    def return_login(self):
        self.root.destroy()





if __name__ == "__main__":
   main()
from tkinter import *
root = Tk()
from tkinter import messagebox
root.resizable(0,0)

# importing mysql

import mysql.connector
mydb= mysql.connector.connect(host="localhost", user="root", passwd="password_123", database="database1")

mycursor= mydb.cursor()


flag= False

#=============================================== creating database username ============================================

'''
mycursor.execute("CREATE DATABASE database1")

mycursor.execute("CREATE TABLE username(Fullname VARCHAR(255),"
                 "username VARCHAR(255),"
                 "email VARCHAR(255),"
                 "contactno VARCHAR(255),"
                 "adress VARCHAR(255),"
                 "password VARCHAR(255),"
                 "uniqueid INTEGER AUTO_INCREMENT Primary KEY);")
                 '''



root.title("SCHOOL MANAGEMENT SYSTEM")

#====================================== window after Successful Login ==================================================





def loginwindow():
    global login



    window_login = Tk()
    window_login.resizable(0,0)

    window_login.title("Login successful")

    permanent = (e_email.get(), e_password.get())

    temp=(permanent[0],)


    mycursor.execute("SELECT Fullname,email,contactno,adress FROM database1.username WHERE email=(%s)",temp)

    result1= mycursor.fetchone()


    Name_label= Label(window_login, text="Full Name:", font=("arial", 25, "bold"), fg="BLACK")
    Name_label.grid(row=0, column=0)
    show_name= Label(window_login, text=result1[0], font=("arial", 25, "bold"), fg="BLACK")
    show_name.grid(row=0, column=2)

    email_label= Label(window_login, text="email:", font=("arial", 25, "bold"), fg="BLACK" )
    email_label.grid(row=1, column=0)
    show_email= Label(window_login, text=result1[1], font=("arial", 25, "bold"), fg="BLACK")
    show_email.grid(row=1, column=2)



    contactno_label= Label(window_login, text="Contact no: ", font=("arial", 25, "bold"), fg="BLACK" )
    contactno_label.grid(row=2, column=0)
    show_contact= Label(window_login, text= result1[2], font=("arial", 25, "bold"), fg="BLACK")
    show_contact.grid(row=2, column=2)

    address_label= Label(window_login, text="Address:", font=("arial", 25, "bold"), fg="BLACK" )
    address_label.grid(row=3, column=0)
    show_address= Label(window_login, text=result1[3], font=("arial", 25, "bold"), fg="BLACK")
    show_address.grid(row=3, column=2)

    updatepassword_label= Label(window_login, text="New password",font=("arial", 25, "bold"), fg="BLACK" )
    updatepassword_label.grid(row=4, column=0)
    updatepassword_entry= Entry(window_login,font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    updatepassword_entry.grid(row=4, column=2)


    def delete():
        entry= (permanent[0], permanent[1])
        mycursor.execute("DELETE FROM  database1.username WHERE email=(%s) AND password=(%s)", entry)
        mydb.commit()
        messagebox.showinfo('data deleted', 'your data has been successfully deleted')
        window_login.destroy()

    def update():

        entry= (updatepassword_entry.get(),permanent[0],permanent[1])
        mycursor.execute("UPDATE database1.username SET password=(%s) WHERE email=(%s) AND password=(%s)",entry)
        mydb.commit()
        messagebox.showinfo('password updated', 'your password has been successfully updated')

    button_update=Button(window_login,font=("arial", 25, "bold"), text="reset password", width=30,bg="YELLOW", command=update)
    button_update.grid(row=5, column=2)


    button_delete= Button(window_login, font=("arial", 25, "bold"),text="Delete Account",width=25, bg="RED", command=delete)
    button_delete.grid(row=6, column=2)


    button_exit= Button(window_login,font=("arial",25,"italic"),text="Exit",width=20,bg="BLUE", command=window_login.destroy)
    button_exit.grid(row=7, column=2)



#loginbutton
def login():

    global e_email,e_username,e_password
    global permanent



    global flag

    mycursor.execute("SELECT  email,password FROM database1.username")
    result= mycursor.fetchall()
    if (e_email.get()!=''and e_password.get()!=''):
        for row in result:
            flag= False
            if e_email.get()==row[0] and e_password.get()== row[1]:
                flag= True
                break

        if flag:
            messagebox.showinfo('login successfull', 'You have successfully logged in')
            loginwindow()
            root.destroy()


        else:
            messagebox.showinfo('wrong credentials', 'record does not exists')


    elif (e_email.get()=='' and e_password.get()==''):
        messagebox.showinfo('invalid login', 'empty field')



    elif (e_email.get()=='') :
        messagebox.showinfo('invalid login', 'username cannot be empty')

    elif (e_password.get()=='') :
        messagebox.showinfo('invalid login', 'password cannot be empty')







#Reistration button,menu
def register():
    global e_fullname, e_username, e_email, e_contact, e_address, e_password

    global flag
    global top
    top = Toplevel()
    top.resizable(0,0)
    top.title("REGISTRATION MENU")





    label_fullname= Label(top, text="Full Name: ",font=("arial",15,"bold"), fg="GREEN")
    label_fullname.grid(row=0,column=0)

    label_username = Label(top, text="Username: ", font=("arial", 15, "bold"), fg="GREEN")
    label_username.grid(row=1, column=0)

    label_email = Label(top, text="e-mail: ", font=("arial", 15, "bold"), fg="GREEN")
    label_email.grid(row=2, column=0)

    label_contact = Label(top, text="Contact no: ", font=("arial", 15, "bold"), fg="GREEN")
    label_contact.grid(row=3, column=0)

    label_address = Label(top, text="Address: ", font=("arial", 15, "bold"), fg="GREEN")
    label_address.grid(row=4, column=0)

    label_password = Label(top, text="Password: ", font=("arial", 15, "bold"), fg="GREEN")
    label_password.grid(row=5, column=0)






#Entriessssssss
    e_fullname = Entry(top, font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    e_fullname.grid(row=0, column=1)

    e_username = Entry(top, font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    e_username.grid(row=1, column=1)

    e_email = Entry(top, font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    e_email.grid(row=2, column=1)

    e_contact = Entry(top, font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    e_contact.grid(row=3, column=1)

    e_address = Entry(top, font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    e_address.grid(row=4, column=1)

    e_password = Entry(top, font=("arial", 15, "italic"), bd=20, width= 30, insertwidth=4, fg="black")
    e_password.grid(row=5, column=1)

    def message():
        global e_fullname, e_username, e_email, e_contact, e_address, e_password

        insert = "INSERT INTO username(Fullname,username,email,contactno,adress,password) VALUES (%s,%s,%s,%s,%s,%s);"
        record = (e_fullname.get(), e_username.get(), e_email.get(), e_contact.get(), e_address.get(), e_password.get())
        mycursor.execute("SELECT Fullname,username,email,contactno,adress,password FROM database1.username")
        result = mycursor.fetchall()
        if (e_fullname.get() != '' and e_username.get() != '' and e_email.get() != '' and e_contact.get() != '' and e_address.get()
                != '' and e_password.get() != ''):
            for row in result:
                if e_email.get() == row[2]:
                    messagebox.showinfo('repeated entry', 'Email already exists')
                    break
                elif ("@" not in e_email.get()):
                    messagebox.showinfo('invalid email', 'INVALID EMAIL')
                    break
                elif e_contact.get().isnumeric() == False:
                    messagebox.showinfo("'Contact No' error", ' please enter valid contact num')
                    break
                elif len(e_contact.get()) < 10:
                    messagebox.showinfo("'Contact No' error", "Contact num cannot contain less than 10 character")
                    break


                else:
                    pass
            else:
                mycursor.execute(insert, record)
                mydb.commit()
                e_fullname.delete(0,'end')
                e_username.delete(0,'end')
                e_email.delete(0,'end')
                e_contact.delete(0,'end')
                e_address.delete(0,'end')
                e_password.delete(0,'end')
                root.destroy()
                messagebox.showinfo('status', 'Registration completed!')

        else:
            messagebox.showinfo('emmpty field', 'please fill all inputs')

    btn_confirm = Button(top, text="Confirm Registration", fg="green", font=("arial", 20, "bold"), command=message)
    btn_confirm.grid(row=6, column=1)

    btn_exit = Button(top, text="Exit", font=("arial", 19, "bold"), width=20, fg="red",
                      command=(top.destroy and root.destroy))
    btn_exit.grid(row=10, column=1)

    btn_back = Button(top, text="Back", font=("arial", 19, "bold"), width=20, fg="red", command=(top.destroy))
    btn_back.grid(row=11, column=1)




#Login window(labeling0
username_ask= Label(root, text="Email: ",font=("arial",15,"bold"), fg="GREEN")
username_ask.grid(row=2,column=0)

e_email= Entry(root, font=("arial",15, "italic"), bd=20, insertwidth=3,fg="black")
e_email.grid(row=2,column=1)

password_ask= Label(root, text="Password: ",font=("arial",15,"bold"), fg="GREEN")
password_ask.grid(row=3,column=0)

e_password= Entry(root, font=("arial",15, "italic"), bd=15, insertwidth=3,fg="black")
e_password.grid(row=3,column=1)

btn_login= Button(root, text=("Login"), font=("arial", 15, "bold"), fg="red", bg="white",command= login)
btn_login.grid(row=4,column=1)

btn_register= Button(root, text=("Register here(for new user)"), font=("arial", 15, "bold"), fg="red", bg="white",command=(register))
btn_register.grid(row=5,column=1)


root.mainloop()



mycursor.close()
mydb.close()
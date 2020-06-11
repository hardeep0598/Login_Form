from tkinter import *
import os


def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(window1, text="Registered Successfully", fg="green", font=("Calibri", 11)).pack()


def Register():
    global window1
    window1 = Toplevel(window)
    window1.geometry("300x250")
    window1.title("Register")

    global username_entry
    global password_entry
    global username
    global password
    username = StringVar()
    password = StringVar()
    Label(window1, text="Please enter details below : ", bg="grey", width="300", height="2",
          font=("Calibri", 13)).pack()
    Label(window1, text="").pack()
    Label(window1, text="").pack()
    Label(window1, text="User Name : ").pack()
    username_entry = Entry(window1, textvariable=username)
    username_entry.pack()
    Label(window1, text="Password : ").pack()
    password_entry = Entry(window1, textvariable=password)
    password_entry.pack()
    Button(window1, text="Register", width="10", height="1", command=register_user).pack()


def delete2():
    window3.destroy()



def login_sucess():
    global window3
    window3=Toplevel(window)
    window3.title("Success")
    window3.geometry("200x200")
    Label(window3, text="Login Success", fg="green", font=("Calibri", 11)).pack()
    Button(window3,text="Ok",command=delete2).pack()


def delete3():
    window4.destroy()


def password_incorrect():
    global window4
    window4 = Toplevel(window)
    window4.title("Password error")
    window4.geometry("200x200")
    Label(window4, text="Password has not been recognized", fg="red", font=("Calibri", 11)).pack()
    Button(text="Ok", command=delete3).pack()


def delete4():
    window5.destroy()


def user_not_found():
    global window5
    window5 = Toplevel(window)
    window5.title("error")
    window5.geometry("200x200")
    Label(window5, text="User not found", fg="red", font=("Calibri", 11)).pack()
    Button(window5,text="Ok", command=delete4).pack()



def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_incorrect()
    else:
        user_not_found()


def Login():
    global window2
    window2 = Toplevel(window)
    window2.geometry("300x250")
    window2.title("Login")

    Label(window2, text="Please enter details below : ", bg="grey", width="300", height="2",font=("Calibri", 13)).pack()
    Label(window2, text="").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label(window2, text="UserName : ").pack()
    username_entry1 = Entry(window2, textvariable=username_verify)
    username_entry1.pack()
    Label(window2, text="Password : ").pack()
    password_entry1 = Entry(window2, textvariable=password_verify)
    password_entry1.pack()
    Button(window2, text="Login", width="10", height="1", command=login_verify).pack()


def main_screen():
    global window
    window = Tk()
    window.geometry("300x250")
    window.title("Notes 1.0")
    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="1", width="30", command=Login()).pack()
    Label(text="").pack()
    Button(text="Register", height="1", width="30", command=Register()).pack()

    window.mainloop()


main_screen()

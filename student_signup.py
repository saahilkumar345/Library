import student_backend
import student_login
from tkinter import*

def student_signup():        
    window = Tk()
    window.wm_title("Student Signup")

    def add_to_table():
        username = username_var.get()
        roll_no = rollno_var.get()
        mobile_no = mobileno_var.get()
        password = password_var.get()
        confirm_password = confirm_var.get()
    
        if var.get() == 1:
            gender = "Male"
        else:
            gender = "Female"

        if (not (username == roll_no == mobile_no == "")) and (password == confirm_password):
            student_backend.insert(username,roll_no, mobile_no, gender, password, confirm_password)
            E4.delete(0, END)
            E4.insert(END, "You are successfuly Registered")
        else:
            E4.delete(0, END)
            E4.insert(END, "Please Renter the password!!")

    def jump_to_login():
        window.destroy()
        student_login.student_login()
                    
        
    

    #window.geometry("500x500")
    L1 = Label(window, text = "Student Signup", bg = "gray80", fg = "black")
    L1.grid(row = 0, columnspan = 2, sticky = W+E,padx = 2, pady = 2)

    L2 = Label(window, text = "Student Name:")
    L2.grid(row = 1, column = 0, sticky = N+E+W+S)

    L3 = Label(window, text = "Roll Number:")
    L3.grid(row = 2, column = 0, sticky = N+E+W+S)

    L4 = Label(window, text = "Mobile Number:")
    L4.grid(row = 3, column = 0, sticky = N+E+W+S)

    L5 = Label(window, text = "Gender:")
    L5.grid(row = 4, column = 0, sticky = N+E+W+S, padx = 10)

    L6 = Label(window, text = "Password:")
    L6.grid(row = 7, column = 0, sticky = N+E+W+S)

    L7 = Label(window, text = "Confirm Password:")
    L7.grid(row = 8, column = 0, sticky = N+E+W+S)

    L8 = Label(window, text = "Already have an account Then :", bg = "gray80")
    L8.grid(row = 11, column = 0)

    username_var = StringVar()
    E1 = Entry(window, textvariable = username_var)
    E1.grid(row = 1, column = 1)

    rollno_var = StringVar()
    E1 = Entry(window, textvariable = rollno_var)
    E1.grid(row = 2, column = 1)

    mobileno_var = StringVar()
    E1 = Entry(window, textvariable = mobileno_var)
    E1.grid(row = 3, column = 1)

    var = IntVar()
    R1 = Radiobutton(window, text="Male", variable=var, value=1)
    R1.grid(row = 5, column = 0, sticky = W, padx = 120)

    R2 = Radiobutton(window, text="Female", variable=var, value=2)
    R2.grid(row = 6, column = 0, sticky = W, padx = 120)

    password_var = StringVar()
    E2 = Entry(window, textvariable = password_var)
    E2.grid(row = 7, column = 1)

    confirm_var = StringVar()
    E3 = Entry(window, textvariable = confirm_var)
    E3.grid(row = 8, column = 1)

    E4 = Entry(window)
    E4.grid(row = 10, columnspan = 2, sticky = W+E)



    B1 = Button(text = "Submit", bd = 4, command = add_to_table)
    B1.grid(row = 9, columnspan = 2, sticky=N+S+E+W)

    B2 = Button(text = "Login", bd = 4, command = jump_to_login)
    B2.grid(row = 11, column = 1, sticky=N+S+E+W, padx = 3, pady = 3)

    window.mainloop()


if __name__ == '__main__' :
    student_signup()




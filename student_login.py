import student_signup
from tkinter import*
import student_backend
import recover_password

import book_selection

def student_login():
    window1 = Tk()

    window1.configure(background = "gray88")
    window1.wm_title("Student Login")


    def check(username, password):
        print(student_backend.view())
        for value in student_backend.view():
            if (username == value[1] and password == value[5]) and not(username == "" and password == ""):
                return True   
        else:
            return False
    
    def login_check():
        username = username_text.get()
        password = password_text.get()
        E3.delete(0, END)
        if (check(username, password)):
            E3.insert(END, "Welcome Users")
            window1.destroy()
            global roll_global
            roll_global = student_backend.search(username,password)
            book_selection.book_selection(roll_global)
            
            
        else:
            E3.insert(END, "Username and Password is wrong")
    
    def jump_to_signup():
        window1.destroy()
        student_signup.student_signup()
    def jump_to_recovery():
        window1.destroy()
        recover_password.recover_password()
        


        

    L1 = Label(window1, text = "Student Login", bg = "gray80", fg = "black")
    L1.grid(row = 0, columnspan = 2, sticky = W+E,padx = 2, pady = 2)
    L2 = Label(window1, text = "Username:", bg = "gray88", fg = "black")
    L2.grid(row = 1, column = 0, sticky = W+E,padx = 2, pady = 2) 
    L3 = Label(window1, text = "Password:",  bg = "gray88", fg = "black")
    L3.grid(row = 2, column = 0, sticky = W+E,padx = 2, pady = 2)
    L4 = Label(window1, text = "Don't have an Account Then :",  bg = "gray88", fg = "black")
    L4.grid(row = 4, column = 0, sticky = W+E,padx = 2, pady = 2)
    L5 = Label(window1, text = "Forget your Password:",  bg = "gray88", fg = "black")
    L5.grid(row = 5, column = 0, sticky = W+E,padx = 2, pady = 2)


    username_text = StringVar()
    E1 = Entry(window1, textvariable = username_text, bg = "gray98")
    E1.grid(row = 1,column = 1, padx = 2, sticky = W+E)

    password_text = StringVar()
    E2 = Entry(window1, textvariable = password_text, bg = "gray98")
    E2.grid(row = 2,column = 1, padx = 2, sticky = W+E)


    E3 = Entry(window1, bg = "gray98")
    E3.grid(row = 6,columnspan = 2, padx = 2, pady = 2, sticky = W+E)

    B1 = Button(window1, text = "Login",bg = "gray80", fg = "black", command = login_check, activebackground = "gray77", activeforeground = "gray1")
    B1.grid(row = 3, columnspan = 2, sticky = N+E+W+S, pady = 2, padx = 2)

    B2 = Button(window1, text = "Singup",bg = "gray80", fg = "black", command = jump_to_signup, activebackground = "gray77", activeforeground = "gray1")
    B2.grid(row = 4, column = 1, sticky = N+E+W+S, pady = 2, padx = 2)

    B3 = Button(window1, text = "Click Here",bg = "gray80", fg = "black", command = jump_to_recovery, activebackground = "gray77", activeforeground = "gray1")
    B3.grid(row = 5, column = 1, sticky = N+E+W+S, pady = 2, padx = 2)

    window1.mainloop()



if __name__ == '__main__':
    student_login()

   


    

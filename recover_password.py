from tkinter import*
import student_backend
import student_login
def recover_password():
	window1 = Tk()
	window1.configure(background = "gray88")
	window1.wm_title("Student Password Recovery")

	def password_recovery():
                roll_no = rollno_text.get()
                mobile_no = mobileno_text.get()
                password = password_text.get()
                confirm_password = confirm_password_text.get()
                E5.delete(0,END)

                if (password == confirm_password) and (not (roll_no == mobile_no == password == confirm_password == "") ):
                        student_backend.update(roll_no, mobile_no, password, confirm_password)
                        E5.insert(END, "you have changed the password")
                        window1.destroy()
                        student_login.student_login()
                        
                else:
                        E5.insert(END, "You have given wrong inputs")

	L1 = Label(window1, text = "Password Recovery", bg = "gray80", fg = "black")
	L1.grid(row = 0, columnspan = 2, sticky = W+E,padx = 2, pady = 2)
	L2 = Label(window1, text = "Roll Number: ", bg = "gray88", fg = "black")
	L2.grid(row = 1, column = 0, sticky = W+E,padx = 2, pady = 2)
	L3 = Label(window1, text = "Mobile Number: ",  bg = "gray88", fg = "black")
	L3.grid(row = 2, column = 0, sticky = W+E,padx = 2, pady = 2)
	L4 = Label(window1, text = "New Password:",  bg = "gray88", fg = "black")
	L4.grid(row = 3, column = 0, sticky = W+E,padx = 2, pady = 2)
	L5 = Label(window1, text = "Confirm Password: ",  bg = "gray88", fg = "black")
	L5.grid(row = 4, column = 0, sticky = W+E,padx = 2, pady = 2)

	rollno_text = IntVar()
	E1 = Entry(window1, textvariable = rollno_text, bg = "gray98")
	E1.grid(row = 1,column = 1, padx = 2, sticky = W+E)
	
	mobileno_text = IntVar()
	E2 = Entry(window1, textvariable = mobileno_text, bg = "gray98")
	E2.grid(row = 2,column = 1, padx = 2, sticky = W+E)

	password_text = StringVar()
	E3 = Entry(window1, textvariable = password_text, bg = "gray98")
	E3.grid(row = 3,column = 1, padx = 2, sticky = W+E)

	confirm_password_text = StringVar()
	E4 = Entry(window1, textvariable = confirm_password_text, bg = "gray98")
	E4.grid(row = 4,column = 1, padx = 2, sticky = W+E)

	E5 = Entry(window1, bg = "gray98")
	E5.grid(row = 6,columnspan = 2, padx = 2, sticky = N+E+W+S, pady = 3)


	B1 = Button(window1, text = "Recover Password",bg = "gray80", fg = "black", activebackground = "gray77", activeforeground = "gray1", command = password_recovery)
	B1.grid(row = 5, columnspan = 2, sticky = N+E+W+S, pady = 2, padx = 2)

	window1.mainloop()

if __name__ == '__main__':
        recover_password()
	

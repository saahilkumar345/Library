from tkinter import*
import student_login
import frontend

window = Tk()

def student_command():
    window.destroy()
    student_login.student_login()
    
def librarian_command():
    window.destroy()
    frontend.frontend()
    

window.configure(background = "gray88")
window.wm_title("Library")

L1 = Label(window, text = "Welcome to the Library:", bg = "light cyan", fg = "black", height = 5)
L1.grid(row = 0, columnspan = 8,rowspan = 2, sticky = W+E,padx = 2, pady = 20)


B1 = Button(window, text = "  Librarian  ",bg = "lavender", fg = "black", activebackground = "gray77", activeforeground = "gray1", width = 20, height = 10, command = librarian_command)
B1.grid(row = 3, columnspan = 4, sticky = N+E+W+S, pady = 15, padx = 20)

B2 = Button(window, text = "  Student  ",bg = "green yellow", fg = "black", activebackground = "gray77", activeforeground = "gray1", width = 20, command = student_command)
B2.grid(row = 3,column = 4, columnspan = 4, sticky = N+E+W+S, pady = 15, padx = 20)

B3 = Button(window, text = "Close",bg = "snow4", fg = "black", activebackground = "gray77", activeforeground = "gray1", command = window.destroy, height = 2)
B3.grid(row = 4, columnspan = 8, sticky = N+E+W+S, pady = 20, padx = 20)

window.mainloop()

from tkinter import *

import backend

import book_selection_backend

import student_login

def book_selection(roll):
    

    def get_selected_row(event):
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)

    
    def view_command():
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END,row)    
    
    def add_book():
        book_selection_backend.insert(roll, selected_tuple[0])

    def view_Selected_Book():
        list1.delete(0,END)
        for a in book_selection_backend.selected_bookid_search(roll):
            for b in book_selection_backend.view_selected_books(a[2]):
                list1.insert(END,b)

    def delete_selected_book():
        book_selection_backend.delete(selected_tuple[0])                

    window=Tk()

    window.wm_title("Book Selection")


    L1 = Label(window, text = "Book Selection", bg = "gray80", fg = "black")
    L1.grid(row = 0, columnspan = 4, sticky = W+E,padx = 2, pady = 2)


    list1=Listbox(window, height=6,width=35)
    list1.grid(row=1,column=0,rowspan=6,columnspan=2,padx = 4, pady = 4)

    sb1=Scrollbar(window)
    sb1.grid(row=1,column=2,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>',get_selected_row)

    B1 = Button(window, text = "View Books",bg = "gray80", fg = "black", activebackground = "gray77", activeforeground = "gray1", command = view_command)
    B1.grid(row = 1, column = 3, sticky = W+E, pady = 2, padx = 2)

    B2 = Button(window, text = "Add Book",bg = "gray80", fg = "black", activebackground = "gray77", activeforeground = "gray1"   , command = add_book)
    B2.grid(row = 2, column = 3, sticky = W+E, pady = 2, padx = 2)

    B3 = Button(window, text = "View Selected Book",bg = "gray80", fg = "black", activebackground = "gray77", activeforeground = "gray1",command = view_Selected_Book)
    B3.grid(row = 3, column = 3, sticky = W+E, pady = 2, padx = 2)

    B4 = Button(window, text = "Remove Selected Book",bg = "gray80", fg = "black", activebackground = "gray77", activeforeground = "gray1", command = delete_selected_book)
    B4.grid(row = 4, column = 3, sticky = W+E, pady = 2, padx = 2)

    B5 = Button(window, text = "Close",bg = "gray80", fg = "black", activebackground = "gray77", activeforeground = "gray1", command = window.destroy)
    B5.grid(row = 5, column = 3, sticky = W+E, pady = 2, padx = 2)

    L2 = Label(window, text = "Student Roll Number:", bg = "gray80", fg = "black")
    L2.grid(row = 6,column = 0, columnspan = 2, sticky = W+E,padx = 2, pady = 2)
    
    rollno_value = StringVar()
    E1 = Entry(window, textvariable = rollno_value, bg = "gray98")
    E1.grid(row = 6,column = 2, columnspan = 2, padx = 4, pady = 4, sticky = W+E)
    E1.insert(END, roll)



    window.mainloop()


if __name__ == '__main__':
    book_selection(0)

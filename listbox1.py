from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry('300x450')
win.configure(bg="brown")
#====Function ================
def insert():
    name = ent_name.get()  
    
    lst_name.insert(END,name)
    ent_name.delete(0, END)

def clear():
    ent_name.delete(0,END)
    lst_name.delete(0,END)

def delete():
    index=lst_name.curselection()
    ige = messagebox.askquestion("delete","r u sure?")
    if ige== "yes":
        
        lst_name.delete(index)


def fetch():
    index=lst_name.curselection()
    iget=lst_name.get(index)
    ent_name.insert(0,iget)
    lst_name.delete(0,iget)


#====Widget ================
lbl_name = Label(win, text= 'Name: ',bg="brown", font='arial 14 bold')
lbl_name.place(x=10 , y= 10)

ent_name = Entry(win,width=25)
ent_name.place(x=100 , y= 13)

lst_name = Listbox(win, font='arial 11 bold')
lst_name.place(x=100 , y=50)

for i in range(5):
    lst_name.insert(END,f'{i+1}- This is a test')

btn_insert = Button(win, text= 'Insert', command= insert)
btn_insert.place(x= 140, y= 260)
btn_clear = Button(win, text= 'Clear', command= clear)
btn_clear.place(x= 140, y= 300)
btn_delete = Button(win, text= 'Delete', command= delete)
btn_delete.place(x= 140, y= 340)
btn_fetch = Button(win, text= 'Fetch', command= fetch)
btn_fetch.place(x= 140, y= 380)


win.mainloop()

















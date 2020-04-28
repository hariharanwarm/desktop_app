from tkinter import *
def click():
    list1.delete(0,END)
    hello='Hello'
    list1.insert(END,hello)
def delete():
    pass
def get_selected_row1(event):
    global selected_row
    index=list1.curselection()
    selected_row=list1.get(index)
window=Tk()
button1=Button(window,text="insert",width=10,command=click)
button1.grid(row=0,column=0)
button2=Button(window,text='delete',width=5,command=delete)
button2.grid(row=1,column=0)
list1=Listbox(window,width=10,height=10)
list1.grid(row=2,column=0,rowspan=2,columnspan=2)
list1.bind('<<ListboxSelect>>',get_selected_row1)
window.mainloop()


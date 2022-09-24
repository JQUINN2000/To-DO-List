from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pickle

# Functions
def submit(event):
    element = entry.get()
    if element:
        list.insert(list.size(), element)
    else:
        messagebox.showerror(title='Error', message='Empty!!!')

def delete():
    for index in reversed(list.curselection()):
        list.delete(index)

def clear_list():
    list.delete(0, END)

def clear_text(event):
    entry.delete(0, END)

def saveFile():
    file_name = filedialog.asksaveasfilename(initialdir='/home/joker/Desktop/Teste',
                                             title='Save File',
                                             filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*'))
                                             )
    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'

        elements = list.get(0, END)

        output_file = open(file_name, 'wb')

        pickle.dump(elements, output_file)

def openFile():
    file_name = filedialog.askopenfilename(initialdir='/home/joker/Desktop/Teste',
                                           title='Open File',
                                           filetypes=(('Dat Files', '*.dat'), ('All Files', '*.*'))
                                           )
    if file_name:

        list.delete(0, END)

        input_file = open(file_name, 'rb')

        elements = pickle.load(input_file)

        for item in elements:
            list.insert(END, item)

# WindowRun
window = Tk()

window.geometry("1080x600")
window.title("To Do List")
window.resizable(False, False)

window.bind('<Return>', submit)
window.bind('<Return>', clear_text, add='+')

# Labels
photo = PhotoImage(file='bg.png')
label = Label(window,
              text="What do I have to do?",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg="black",
              image=photo,
              compound='bottom')
label.place(x=0, y=0)

# Buttons
#submit_button = Button(window,
#              text="Submit",
#              font=('Comic Sans',15),
#              fg='#00FF00',
#              bg='black',
#              activebackground='black',
#              activeforeground='#00FF00',
#              command=lambda:[submit(),clear_text()]
#              )
#submit_button.place(x=950,y=540)

delete_button = Button(window,
              text="Delete",
              font=('Comic Sans', 15),
              fg='#00FF00',
              bg='black',
              activebackground='black',
              activeforeground='#00FF00',
              command=delete
              )
delete_button.place(x=950, y=490)

# Menubar
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='Save', command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Clear', command=clear_list)

# Entry
entry = Entry(window,
              font=('Arial', 15),
              bg='black',
              fg='#00FF00'
              )
entry.place(x=10, y=150)

# ListBox
scrollbar = Scrollbar(window, orient=HORIZONTAL)
list = Listbox(window,
               font=('Arial', 25, 'bold'),
               bg='black',
               fg='#00FF00',
               height=8,
               width=20,
               selectmode=MULTIPLE,
               xscrollcommand=scrollbar.set
               )
scrollbar.config(command=list.xview)
scrollbar.pack(side=BOTTOM, fill=X)
list.place(x=350, y=150)

window.mainloop()

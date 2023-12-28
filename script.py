from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


'''def on_window_resize(event):
    # Function to make widgets expand with window size change
    # Configure rows and columns to resize proportionally with window resizing
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_rowconfigure(5, weight=1)
    window.grid_rowconfigure(6, weight=1)
    list1.grid(row=2, column=0, columnspan=4, rowspan=5, sticky=(N, S, E, W))
    sb1.grid(row=2, column=4, rowspan=5, sticky=(N, S))
'''

def view_command():
    for row in backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),year_text.get(),isbn_text.get()))


def delete_command():
    selected_item = list1.curselection()  # Retrieve the selected item index
    if selected_item:
        index = selected_item[0]
        selected_tuple = list1.get(index)
        backend.delete(selected_tuple[0])  # Delete the record using its ID
        view_command()  # Refresh the list after deletion


def update_command():
    selected_item = list1.curselection()  # Retrieve the selected item index
    if selected_item:
        index = selected_item[0]
        selected_tuple = list1.get(index)
        backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_command()  # Refresh the list after updating


window = Tk()

window.wm_title("BookStore")

# Increase window size (width x height)
# window.geometry("500x300")  # Set your desired dimensions

# Bind window resize event to the resizing function
# window.bind("<Configure>", on_window_resize)


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=15, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=15, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=15, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=15, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=15, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=15, command=window.destroy)
b6.grid(row=7, column=3)
window.mainloop()
from tkinter import *
from tkinter import ttk
from TodoDAO import TodoDAO

def hello():
    print("hello")


def main():
    root = Tk()
    frame = Frame(root)

    tree = ttk.Treeview(frame,columns=('id','title','completed'),show="headings")
    tree.heading("id",text="#")
    tree.heading("title",text="Title")
    tree.heading("completed",text="done ?")
    
    dao = TodoDAO()

    for todo in dao.find_all():
        tree.insert("",index=todo.id,values=[todo.id,todo.title,todo.completed])

    tree.pack(fill=BOTH,expand=True)
    frame.pack(fill=BOTH,expand=True)

    root.mainloop()

if __name__ == '__main__':
    main()
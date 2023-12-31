# todo_app_gui.py
from tkinter import *
from todo_app_backend import ToDoBackend

class ToDoGUI:
    def __init__(self, master, backend):
        self.master = master
        self.backend = backend
        self.screen()

    # ... (remaining GUI code)

def main():
    root = Tk()
    root.title("ToDo Application")
    root.iconbitmap("icon/todo.ico")
    root.resizable(0, 0)
    root.config(bg="black")

    backend = ToDoBackend()  # Create an instance of the backend
    ToDoGUI(root, backend)

    root.mainloop()

if __name__ == "__main__":
    main()

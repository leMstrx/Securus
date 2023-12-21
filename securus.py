import tkinter as tk 
from frontend.login_window import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.resizable(False, False)
    root.mainloop()
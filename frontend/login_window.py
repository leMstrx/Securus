import tkinter as tk 
from tkinter import messagebox
from backend.user_manager import create_user, find_user, get_users
from backend.encryption import decrypt_password, encrypt_password

class LoginWindow: 
    def __init__(self, master):
        #General Window Settings
        self.master = master
        self.master.title("Securus - Login")
        self.master.geometry("350x200")
        #self.master.resizeable(False, False)

        #Create widgets
        self.label_username = tk.Label(master, text="Username:")
        self.entry_username = tk.Entry(master)
        self.label_password = tk.Label(master, text="Password:")
        self.entry_password = tk.Entry(master, show="✝")
        self.button_login = tk.Button(master, text="Login", command=self.login)
        self.label_not_signed_in = tk.Label(master, text="Not signed in?")
        self.button_signup = tk.Button(master, text="Sign Up", command=self.signup)

        #Grid Layout
        self.label_username.grid(row=0, column=0, padx=10, pady=10)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)
        self.label_password.grid(row=1, column=0, padx=10, pady=10)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)
        self.button_login.grid(row=2, column=1, columnspan=2, pady=10)
        self.label_not_signed_in.grid(row=3, column=0, padx=10, pady=10)
        self.button_signup.grid(row=3, column=1,columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password: 
            user = find_user(username)
            if user and decrypt_password(user["key"], user["password"]) == password:
                self.show_main_window(username)
            else: 
                messagebox.showwarning("Warning", "Invalid Username or password")
        else: 
                messagebox.showwarning("Warning", "Please enter both correct username and password.")

    def signup(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username and password: 
            user = find_user(username)
            if not user:
                create_user(username=username, password=password)
                messagebox.showinfo("Success", "User was created successfully")
            else: 
                messagebox.showwarning("Warning", "Username already in system")
        else: 
            messagebox.showwarning("Warning", "Please fill out both username and password correctly")

    def show_main_window(self, username):
        #Close the login window and show main interface
        self.master.destroy()
        root = tk.Tk()
        main_window = Interface(root, username)
        root.resizable(False, False)
        root.mainloop()

from frontend.interface import Interface
    
            
                
    

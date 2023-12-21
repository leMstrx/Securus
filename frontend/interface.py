import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from backend.encryption import encrypt_password, decrypt_password, decrypt_data, encrypt_data

class Interface: 
    def __init__(self, master, username):
        self.master = master
        self.master.title(f"Welcome {username}")
        self.master.geometry("550x700")
        self.username = username

        # Upper Part 
        self.frame_upper = tk.Frame(master)
        self.frame_upper.pack(side=tk.TOP, fill=tk.X)

        self.button_new_entry = tk.Button(self.frame_upper, text="New Entry", command=self.new_entry_popup)
        self.button_delete_selected = tk.Button(self.frame_upper, text="Delete selected", command=self.delete_selected)
        self.button_logout = tk.Button(self.frame_upper, text="Logout", command=self.logout)

        self.button_new_entry.pack(side=tk.LEFT, padx=10)
        self.button_delete_selected.pack(side=tk.LEFT, padx=10)
        self.button_logout.pack(side=tk.RIGHT, padx=10)

        # Lower Part - Treeview
        self.tree = ttk.Treeview(master, columns=("Index", "Title", "Password"), show="headings", height=15)
        self.tree.heading("Index", text="Index")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Password", text="Password")
        self.tree.column("Index", width=10)  # Set the width of the "Index" column
        self.tree.column("Title", width=70)  # Set the width of the "Title" column
        self.tree.column("Password", width=200)  # Set the width of the "Password" column
        self.tree.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Load data from file
        self.load_data()

    def new_entry_popup(self):
        # Create a popup window for adding a new entry
        popup = tk.Toplevel(self.master)
        popup.title("Securus - New Entry")

        # Widgets for the popup-Window
        label_title = tk.Label(popup, text="Title")
        entry_title = tk.Entry(popup)
        label_password = tk.Label(popup, text="Password")
        entry_password = tk.Entry(popup)
        button_add = tk.Button(popup, text="Add", command=lambda: self.add_new_entry(entry_title.get(), entry_password.get(), popup))

        # Grid layout for the pop-up window
        label_title.grid(row=0, column=0, padx=10, pady=10)
        entry_title.grid(row=0, column=1, padx=10, pady=10)
        label_password.grid(row=1, column=0, padx=10, pady=10)
        entry_password.grid(row=1, column=1, padx=10, pady=10)
        button_add.grid(row=2, column=0, columnspan=2, pady=10)

    def add_new_entry(self, title, password, popup):
        # Add a new entry to the Treeview
        item_id = self.tree.insert("", "end", values=(self.tree.index(""), title, password))

        # Save data to file
        self.save_data()

        # Close the popup window
        popup.destroy()

    def delete_selected(self):
        # Delete selected items in the Treeview
        selected_items = self.tree.selection()
        for item_id in selected_items:
            self.tree.delete(item_id)

        # Save data to file after deletion
        self.save_data()

    def logout(self):
        # Save data to file before logout
        self.save_data()

        # Close the main window and show the login window again
        self.master.destroy()
        show_login_window()

    def save_data(self):
        # Save data to a file with encryption
        with open(f"data_{self.username}.txt", "wb") as file:
            for item_id in self.tree.get_children():
                values = self.tree.item(item_id, "values")
                encrypted_line = encrypt_data(f"{values[0]},{values[1]},{values[2]}\n")
                file.write(encrypted_line)

    def load_data(self):
        # Load and decrypt data from a file
        try:
            with open(f"data_{self.username}.txt", "rb") as file:
                for encrypted_line in file:
                    decrypted_line = decrypt_data(encrypted_line).strip()
                    values = decrypted_line.split(",")
                    self.tree.insert("", "end", values=(values[0], values[1], values[2]))
        except FileNotFoundError:
            # If the file is not found, it means there is no saved data yet
            pass


def show_login_window():
    root = tk.Tk()
    login_window = LoginWindow(root)
    root.mainloop()

from frontend.login_window import LoginWindow

if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root, "USERNAME_PLACEHOLDER")
    root.mainloop()

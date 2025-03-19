import sqlite3
from tkinter import *
from tkinter import ttk


class DisplayUsers:
    def __init__(self, master):
        self.master = master
        self.master.title("User Database")
        self.master.geometry("500x300")

        # Title Label
        Label(self.master, text="Users Database", font=("Arial", 18, "bold")).pack(pady=10)

        # Creating a Table
        self.tree = ttk.Treeview(self.master, columns=("ID", "Username", "Password", "Role"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Role", text="Role")

        self.tree.column("ID", width=50)
        self.tree.column("Username", width=150)
        self.tree.column("Password", width=150)
        self.tree.column("Role", width=100)

        self.tree.pack(pady=10, fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = Scrollbar(self.master, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.load_users()

    def load_users(self):
        """Fetches and displays users from the database."""
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")  # Fetch all users
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert("", END, values=row)

        conn.close()


# Run the Application
root = Tk()
app = DisplayUsers(root)
root.mainloop()

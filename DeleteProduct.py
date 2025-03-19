import sqlite3
import tkinter as tk
from tkinter import messagebox, Frame, Label, Entry, Button, Text, END
from datetime import datetime

# Database Connection
conn = sqlite3.connect('inventory_system.db')
cursor = conn.cursor()

class DeleteProduct:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")
        self.master.title("Delete Product")
        self.master.configure(bg="#A3D1C6")  # Light Green Background

        # Frame for UI
        frame = Frame(self.master, bg="#B3D8A8", padx=20, pady=20, relief="groove", bd=3)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        Label(frame, text="🗑 Delete Product", font=('Arial', 20, 'bold'), fg="white", bg="#3D8D7A").pack(pady=10, fill="x")

        # Label & Entry for Product ID
        Label(frame, text="Enter Product ID:", font=('Arial', 14, 'bold'), bg="#B3D8A8").pack()
        self.id_entry = Entry(frame, width=20, font=('Arial', 14), bg="white")
        self.id_entry.pack(pady=10)

        # Delete Button
        self.delete_btn = Button(frame, text="❌ Delete Product", font=('Arial', 14, 'bold'),
                                 bg="#3D8D7A", fg="white", width=20, height=1, cursor="hand2",
                                 command=self.delete_product)
        self.delete_btn.pack(pady=10)

        # Hover Effect for Button
        self.delete_btn.bind("<Enter>", lambda e: self.delete_btn.config(bg="#FBFFE4", fg="black"))
        self.delete_btn.bind("<Leave>", lambda e: self.delete_btn.config(bg="#3D8D7A", fg="white"))

        # Log Section
        Label(frame, text="Log:", font=('Arial', 14, 'bold'), bg="#B3D8A8").pack(pady=10)
        self.log_box = Text(frame, width=50, height=5, font=('Arial', 12), wrap="word")
        self.log_box.pack()

    def delete_product(self):
        product_id = self.id_entry.get().strip()

        # Validate input
        if not product_id.isdigit():
            messagebox.showerror("Error", "Product ID must be a valid number!")
            return

        product_id = int(product_id)

        # Check if product exists
        cursor.execute("SELECT * FROM inventory WHERE id=?", (product_id,))
        product = cursor.fetchone()

        if not product:
            messagebox.showerror("Error", f"Product ID {product_id} not found!")
            return

        # Confirm before deleting
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete {product[1]}?")
        if not confirm:
            return

        # Delete the product
        cursor.execute("DELETE FROM inventory WHERE id=?", (product_id,))
        conn.commit()

        # Update log with timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_box.insert(END, f"[{timestamp}] Deleted Product ID: {product_id}, Name: {product[1]}\n")
        self.log_box.see(END)  # Auto-scroll log
        messagebox.showinfo("Success", f"Deleted {product[1]} successfully!")

# Run the App
root = tk.Tk()
app = DeleteProduct(root)
root.mainloop()

# Close DB Connection when the window closes
conn.close()

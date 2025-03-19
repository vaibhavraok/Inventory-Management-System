📌 Overview

The Inventory Management System is a desktop application built using Python (Tkinter for GUI) and SQLite for database management. This system allows businesses to efficiently track and manage their inventory, search for products, update stock levels, process transactions, and generate bills.

🔹 Key Features

✅ Product Management:

Add and update product details (name, stock, price). Search for products using product ID.

✅ Stock Management:

Displays current stock levels. Prevents adding items to the cart if stock is insufficient. Alerts when stock falls below a critical level (e.g., less than 5).

✅ Cart System:

Add products to the cart. Update quantity dynamically. Calculate total cost in real-time.

✅ Transaction Processing:

Generate invoices when the customer purchases items. Deduct purchased quantity from stock. Save transactions in a database for future reference.

✅ User-Friendly Interface:

Two-panel UI (left for product search & input, right for invoice display). Color-coded interface for better visibility.

✅ Data Persistence (SQLite Database):

inventory Table: Stores product details. transactions Table: Stores purchase records with date, product name, quantity, and total amount.

🔹 Technologies Used

Python: Core programming language. Tkinter: GUI framework for the desktop application. SQLite: Lightweight database for storing product and transaction details. OS Module: Configures environment paths for Tcl/Tk. Datetime Module: Fetches current date for transactions.

🔹 Workflow

1️⃣ User enters a product ID → Searches the product in the database.

2️⃣ Product details are displayed → User enters the quantity.

3️⃣ Stock validation occurs → Ensures stock availability.

4️⃣ Product is added to the cart → Updates the total price dynamically.

5️⃣ User confirms the purchase → Updates stock and saves transaction history.

6️⃣ Bill is generated → Clears UI for the next transaction.

🔹 Future Enhancements (Optional Upgrades)

🚀 Generate PDF invoices for billing.

🚀 Add Admin Panel for adding/removing products.

🚀 Implement Barcode Scanning for faster product search.

🚀 Connect to an Online Database (MySQL/PostgreSQL) for remote access.

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/14c33451321463f34205602827340fa2fc92c28b/Screenshot%202025-03-19%20220324.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/e5264d79454adb2134f4fe14b9e72d1f6324cd74/Screenshot%202025-03-19%20221329.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/e5264d79454adb2134f4fe14b9e72d1f6324cd74/Screenshot%202025-03-19%20221446.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/e5264d79454adb2134f4fe14b9e72d1f6324cd74/Screenshot%202025-03-19%20221422.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/8783b9e46be918bcb356c79918d314179907167a/Screenshot%202025-03-19%20231525.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/8783b9e46be918bcb356c79918d314179907167a/Screenshot%202025-03-19%20230218.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/8783b9e46be918bcb356c79918d314179907167a/Screenshot%202025-03-19%20221612.png)

![image alt](https://github.com/vaibhavraok/Inventory-Management-System/blob/8783b9e46be918bcb356c79918d314179907167a/Screenshot%202025-03-19%20221510.png)


💻 Installation & Setup Follow these steps to run the project locally:

📥 1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git cd your-repo-name

2️⃣ Install Dependencies

pip install tkinter sqlite3

3️⃣ Run the Application

python login.py

📞 Contact

📧 Email: vaibhavraok0123@gmail.com

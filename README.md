📦 Inventory Management System

A simple Python program to manage inventory, track stock, process sales, and calculate revenue.
This project was built as a learning exercise for practicing functions, error handling, and dictionary usage in Python.

🚀 Features

Add items with price and stock quantity

Update stock levels after sales

Generate sales reports with total revenue

Handle errors:

Item not found

Insufficient stock

Invalid input format

🛠 Tech Stack

Language: Python 3

📂 Project Structure
inventory-management/
│── main.py            # Main source code
│── README.md          # Project documentation
│── requirements.txt   # Dependencies (if any)

▶️ How to Run

Clone the repository:

git clone https://github.com/HeyitzSahil/inventory-management.git
cd inventory-management


Run the script:

python main.py

📊 Example Usage
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)

sales = {"Apple": 30, "Banana": 20, "Orange": 10}
print(sales_report(sales))


Output:

Item 'Apple' added successfully.
Item 'Banana' added successfully.
Error: Item 'Orange' not found.
Total revenue: $19.00

📌 Future Improvements

Add user input support (interactive CLI)

Save/load inventory from a file (CSV/JSON)

Add discounts and categories

✨ Author

Sahil Swarnakar
👨‍💻 BTech CSE (AI) Student | Python & ML Enthusiast

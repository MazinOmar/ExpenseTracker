import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import csv

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        
        self.expenses = []

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Entry for Expense Description
        tk.Label(self.root, text="Description:").grid(row=0, column=0, padx=10, pady=10)
        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.grid(row=0, column=1, padx=10, pady=10)

        # Entry for Expense Amount
        tk.Label(self.root, text="Amount:").grid(row=1, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Add Expense Button
        tk.Button(self.root, text="Add Expense", command=self.add_expense).grid(row=2, column=0, columnspan=2, pady=10)

        # Expense List
        self.expense_list = ttk.Treeview(self.root, columns=("Description", "Amount"), show='headings')
        self.expense_list.heading("Description", text="Description")
        self.expense_list.heading("Amount", text="Amount")
        self.expense_list.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Total Expenses Label
        self.total_label = tk.Label(self.root, text="Total: $0.00")
        self.total_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Save to CSV Button
        tk.Button(self.root, text="Save to CSV", command=self.save_to_csv).grid(row=5, column=0, columnspan=2, pady=10)

    def add_expense(self):
        desc = self.desc_entry.get()
        amount = self.amount_entry.get()
        
        if desc and amount:
            try:
                amount = float(amount)
                self.expenses.append((desc, amount))
                self.expense_list.insert("", "end", values=(desc, f"${amount:.2f}"))
                self.update_total()
                self.desc_entry.delete(0, "end")
                self.amount_entry.delete(0, "end")
            except ValueError:
                messagebox.showerror("Invalid Input", "Amount must be a number.")
        else:
            messagebox.showwarning("Input Error", "Please enter both description and amount.")

    def update_total(self):
        total = sum(expense[1] for expense in self.expenses)
        self.total_label.config(text=f"Total: ${total:.2f}")

    def save_to_csv(self):
        with open('expenses.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Description", "Amount"])
            writer.writerows(self.expenses)
        messagebox.showinfo("Save Successful", "Expenses saved to expenses.csv.")

# Create the main window
root = tk.Tk()
app = ExpenseTrackerApp(root)
root.mainloop()
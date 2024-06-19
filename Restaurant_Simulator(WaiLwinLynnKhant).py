#Resturant Simulator by Wai Lwin Lynn Khant

import tkinter as tk
from tkinter import ttk

class RestaurantSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Simulator")
        
        # Set window size
        self.root.geometry("600x600")
        
        # Create a main frame
        self.main_frame = tk.Frame(root, bg="#f2f2f2", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")
        
        # Create a title label
        self.label = tk.Label(self.main_frame, text="Welcome to the Restaurant!", font=("Helvetica", 20, "bold"), bg="#4CAF50", fg="white")
        self.label.pack(pady=10)
        
        # Create the menu frame
        self.menu_frame = tk.Frame(self.main_frame, bg="#f2f2f2")
        self.menu_frame.pack(pady=20)
        
        self.create_menu()

    def create_menu(self):
        # Sample menu items
        self.menu_items = {
            "Pizza": 10.0,
            "Burger": 8.0,
            "Pasta": 12.0,
            "Salad": 6.0,
            "Soup": 5.0,
            "Steak": 20.0,
            "Fish": 15.0,
            "Ice Cream": 4.0,
            "Coffee": 3.0,
            "Tea": 2.5
        }
        
        # Display the menu
        tk.Label(self.menu_frame, text="Menu", font=("Helvetica", 16, "bold"), bg="#f2f2f2", fg="#333").grid(row=0, column=0, columnspan=3, pady=10)
        
        row = 1
        self.order_vars = {}
        
        for item, price in self.menu_items.items():
            tk.Label(self.menu_frame, text=f"{item}: ${price}", font=("Helvetica", 12), bg="#f2f2f2", fg="#333").grid(row=row, column=0, sticky="w", padx=10, pady=5)
            
            # Create quantity control
            quantity_frame = tk.Frame(self.menu_frame, bg="#f2f2f2")
            quantity_frame.grid(row=row, column=1, padx=10, pady=5)
            
            self.order_vars[item] = tk.IntVar(value=0)
            
            btn_decrease = tk.Button(quantity_frame, text="-", command=lambda i=item: self.update_quantity(i, -1), font=("Helvetica", 12), width=2, bg="#ffcccc", fg="#333")
            btn_decrease.pack(side="left")
            
            quantity_label = tk.Label(quantity_frame, textvariable=self.order_vars[item], font=("Helvetica", 12), width=3, bg="#fff", fg="#333")
            quantity_label.pack(side="left", padx=5)
            
            btn_increase = tk.Button(quantity_frame, text="+", command=lambda i=item: self.update_quantity(i, 1), font=("Helvetica", 12), width=2, bg="#ccffcc", fg="#333")
            btn_increase.pack(side="left")
            
            row += 1
        
        # Button to place the order
        self.order_button = tk.Button(self.main_frame, text="Place Order", font=("Helvetica", 14, "bold"), command=self.show_order_summary, bg="#4CAF50", fg="white")
        self.order_button.pack(pady=20)
    
    def update_quantity(self, item, change):
        current_value = self.order_vars[item].get()
        new_value = current_value + change
        if new_value >= 0:
            self.order_vars[item].set(new_value)
    
    def show_order_summary(self):
        # Calculate the bill
        total_bill = 0.0
        orders = []

        for item, price in self.menu_items.items():
            quantity = self.order_vars[item].get()
            if quantity > 0:
                item_total = price * quantity
                total_bill += item_total
                orders.append((item, quantity, item_total))
        
        # Create a new window for the order summary
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Order Summary")
        summary_window.geometry("500x500")
        summary_window.configure(bg="#f2f2f2")
        
        # Create the Treeview widget
        tree = ttk.Treeview(summary_window, columns=("Item", "Quantity", "Total"), show='headings')
        tree.heading("Item", text="Item")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Total", text="Total ($)")
        tree.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Insert order items into the Treeview
        for order in orders:
            tree.insert("", "end", values=order)
        
        # Display the total bill
        total_label = tk.Label(summary_window, text=f"Total Bill: ${total_bill:.2f}", font=("Helvetica", 14), bg="#f2f2f2", fg="#333")
        total_label.pack(pady=10)
        
        # Payment section
        payment_frame = tk.Frame(summary_window, bg="#f2f2f2", padx=10, pady=10)
        payment_frame.pack(pady=10)
        
        tk.Label(payment_frame, text="Enter Payment Amount: ", font=("Helvetica", 12), bg="#f2f2f2", fg="#333").grid(row=0, column=0, padx=5)
        self.payment_var = tk.DoubleVar()
        tk.Entry(payment_frame, textvariable=self.payment_var, font=("Helvetica", 12), width=10, bg="#fff", fg="#333").grid(row=0, column=1, padx=5)
        
        # Button to calculate change
        self.pay_button = tk.Button(payment_frame, text="Pay", font=("Helvetica", 12), command=lambda: self.calculate_change(total_bill), bg="#4CAF50", fg="white")
        self.pay_button.grid(row=0, column=2, padx=5)
        
        # Label to display change
        self.change_label = tk.Label(summary_window, text="", font=("Helvetica", 14), bg="#f2f2f2", fg="#333")
        self.change_label.pack(pady=10)

        # Add a protocol to clear orders when window is closed
        summary_window.protocol("WM_DELETE_WINDOW", lambda: self.clear_orders(summary_window))
    
    def calculate_change(self, total_bill):
        payment = self.payment_var.get()
        if payment >= total_bill:
            change = payment - total_bill
            self.change_label.config(text=f"Change: ${change:.2f}")
        else:
            self.change_label.config(text="Insufficient payment. Please pay the full amount.")

    def clear_orders(self, window):
        # Reset all order quantities to zero
        for item in self.order_vars:
            self.order_vars[item].set(0)
        
        # Clear the payment input
        self.payment_var.set(0.0)
        
        # Destroy the summary window
        window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantSimulator(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists.")
        else:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            return "No contacts found."
        else:
            return "\n".join([f"Name: {name}, Phone: {details['phone']}" for name, details in self.contacts.items()])

    def search_contact(self, search_term):
        found_contacts = []
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                found_contacts.append(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
        if not found_contacts:
            return "No contact found."
        else:
            return "\n".join(found_contacts)

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            messagebox.showinfo("Success", "Contact updated successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showerror("Error", "Contact not found.")

class ContactApp:
    def __init__(self, root):
        self.contact_book = ContactBook()
        
        self.root = root
        self.root.title("Contact Management System")
        
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, padx=10, pady=10)
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=4, column=1, padx=10, pady=10)
        
        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=5, column=0, padx=10, pady=10)
        self.search_entry = tk.Entry(root)
        self.search_entry.grid(row=5, column=1, padx=10, pady=10)
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, padx=10, pady=10)
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=6, column=1, padx=10, pady=10)
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=7, column=0, padx=10, pady=10)
        
        self.result_text = tk.Text(root, width=40, height=10)
        self.result_text.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contact_book.add_contact(name, phone, email, address)
        self.clear_entries()
        
    def view_contacts(self):
        contacts = self.contact_book.view_contacts()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, contacts)
        
    def search_contact(self):
        search_term = self.search_entry.get()
        result = self.contact_book.search_contact(search_term)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)
        
    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name:
            self.contact_book.update_contact(name, phone, email, address)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter a name to update the contact.")
        
    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            self.contact_book.delete_contact(name)
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter a name to delete the contact.")
        
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()

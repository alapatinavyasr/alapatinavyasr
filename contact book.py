import tkinter as tk
from tkinter import messagebox, ttk
import json


class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("700x500")
        self.root.configure(bg="#f0f8ff")

        # Contact data
        self.contacts = {}
        self.file_name = "contacts.json"

        # Title Label
        title_label = tk.Label(
            self.root, text="Contact Manager", font=("Helvetica", 20, "bold"), bg="#4682b4", fg="white"
        )
        title_label.pack(fill=tk.X, pady=10)

        # Input Fields
        input_frame = tk.Frame(self.root, bg="#f0f8ff")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Name:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Phone:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=30)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Email:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=30)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Address:", font=("Helvetica", 12), bg="#f0f8ff").grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=30)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        add_button = tk.Button(
            button_frame, text="Add Contact", command=self.add_contact, font=("Helvetica", 12), bg="#32cd32", fg="white"
        )
        add_button.grid(row=0, column=0, padx=10)

        update_button = tk.Button(
            button_frame,
            text="Update Contact",
            command=self.update_contact,
            font=("Helvetica", 12),
            bg="#1e90ff",
            fg="white",
        )
        update_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(
            button_frame, text="Delete Contact", command=self.delete_contact, font=("Helvetica", 12), bg="#ff6347", fg="white"
        )
        delete_button.grid(row=0, column=2, padx=10)

        search_button = tk.Button(
            button_frame, text="Search Contact", command=self.search_contact, font=("Helvetica", 12), bg="#ffa500", fg="white"
        )
        search_button.grid(row=0, column=3, padx=10)

        # Contact List
        self.contact_list = ttk.Treeview(self.root, columns=("Phone", "Email", "Address"), show="headings")
        self.contact_list.heading("Phone", text="Phone")
        self.contact_list.heading("Email", text="Email")
        self.contact_list.heading("Address", text="Address")
        self.contact_list.pack(fill=tk.BOTH, expand=True, pady=10)

        self.load_contacts()

    def add_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name or not phone:
            messagebox.showwarning("Input Error", "Name and Phone are required fields!")
            return

        if name in self.contacts:
            messagebox.showwarning("Duplicate Entry", "A contact with this name already exists!")
            return

        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        self.update_contact_list()
        self.save_contacts()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added successfully!")

    def update_contact(self):
        selected_item = self.contact_list.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return

        name = self.contact_list.item(selected_item, "text")
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()
        address = self.address_entry.get().strip()

        if not phone:
            messagebox.showwarning("Input Error", "Phone is a required field!")
            return

        self.contacts[name] = {"phone": phone, "email": email, "address": address}
        self.update_contact_list()
        self.save_contacts()
        self.clear_entries()
        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        selected_item = self.contact_list.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "No contact selected!")
            return

        name = self.contact_list.item(selected_item, "text")
        del self.contacts[name]
        self.update_contact_list()
        self.save_contacts()
        messagebox.showinfo("Success", "Contact deleted successfully!")

    def search_contact(self):
        query = self.name_entry.get().strip()
        if not query:
            messagebox.showwarning("Input Error", "Enter a name or phone to search!")
            return

        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details["phone"]:
                self.contact_list.delete(*self.contact_list.get_children())
                self.contact_list.insert("", "end", text=name, values=(details["phone"], details["email"], details["address"]))
                return

        messagebox.showinfo("No Results", "No contact found with the given details!")

    def update_contact_list(self):
        self.contact_list.delete(*self.contact_list.get_children())
        for name, details in self.contacts.items():
            self.contact_list.insert("", "end", text=name, values=(details["phone"], details["email"], details["address"]))

    def save_contacts(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file)

    def load_contacts(self):
        try:
            with open(self.file_name, "r") as file:
                self.contacts = json.load(file)
            self.update_contact_list()
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = {}

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

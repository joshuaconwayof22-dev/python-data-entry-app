
import tkinter as tk
from tkinter import messagebox
import csv

root = tk.Tk()
root.title("Information Form")
root.geometry("500x300")

#creates labels
#title
title_label = tk.Label(
    root, text="Please Enter Your Information",
    font=("Arial", 14, "bold")
)
title_label.grid(row=0, column=0, columnspan=4, pady=(10, 20))


# Name
tk.Label(root, text="Name:").grid(row=1, column=0, sticky="e", padx=10, pady=2)
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=1, column=1, columnspan=3, sticky="w", pady=2)

# Email Address
tk.Label(root, text="Email Address:").grid(row=2, column=0, sticky="e", padx=10, pady=2)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=2, column=1, columnspan=3, sticky="w", pady=2)

# Phone Number
tk.Label(root, text="Phone Number:").grid(row=3, column=0, sticky="e", padx=10, pady=2)
phone_entry = tk.Entry(root, width=40)
phone_entry.grid(row=3, column=1, columnspan=3, sticky="w", pady=2)

# Address
tk.Label(root, text="Address:").grid(row=4, column=0, sticky="e", padx=10, pady=2)
address_entry = tk.Entry(root, width=40)
address_entry.grid(row=4, column=1, columnspan=3, sticky="w", pady=2)

# City
tk.Label(root, text="City:").grid(row=5, column=0, sticky="e", padx=10, pady=2)
city_entry = tk.Entry(root, width=18)
city_entry.grid(row=5, column=1, sticky="w", pady=2)

#State
tk.Label(root, text="State:").grid(row=5, column=2, sticky="e", padx=10, pady=2)
state_entry = tk.Entry(root, width=5)
state_entry.grid(row=5, column=3, sticky="w", pady=2)

#Zip
tk.Label(root, text="Zip:").grid(row=6, column=0, sticky="e", padx=10, pady=2)
zip_entry = tk.Entry(root, width=8)
zip_entry.grid(row=6, column=1, sticky="w", pady=2)

#Validates requested data is in correct format
def validate_data(name, email, phone, address, city, state, zip_code):

    if not name.strip():
        return False, "Name cannot be blank."
    if not email.strip():
        return False, "Email address cannot be blank."
    if not phone.strip():
        return False, "Phone number cannot be blank."
    if not address.strip():
        return False, "Address cannot be blank."
    if not city.strip():
        return False, "City cannot be blank."
    if not state.strip():
        return False, "State cannot be blank."
    if not zip_code.strip():
        return False, "Zip code cannot be blank."


    if "@" not in email or "." not in email:
        return False, "Email address is not in a valid format."


    digits_only = "".join(ch for ch in phone if ch.isdigit())
    if len(digits_only) < 10:
        return False, "Phone number must contain at least 10 digits."


    if len(state.strip()) != 2 or not state.isalpha():
        return False, "State should be a 2-letter abbreviation (e.g., DE)."


    if not zip_code.isdigit() or len(zip_code) != 5:
        return False, "Zip code must be exactly 5 digits."

    return True, ""

def clear_form():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    zip_entry.delete(0, tk.END)


def submit_form():
    # Get values from the entry boxes
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()

    # 1) VALIDATE
    is_valid, error_message = validate_data(
        name, email, phone, address, city, state, zip_code
    )

    if not is_valid:
        messagebox.showerror("Invalid Data", error_message)
        return  # stop here, do not save

    # 2) SAVE TO CSV
    try:
        with open("people_data.csv", mode="a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email, phone, address, city, state, zip_code])
    except Exception as e:
        messagebox.showerror("File Error", f"Could not save data:\n{e}")
        return

    # 3) SUCCESS MESSAGE
    messagebox.showinfo("Success", "Information saved successfully.")

    # 4) CLEAR THE FORM
    clear_form()



submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=7, column=0, columnspan=4, pady=20)

root.mainloop()





































































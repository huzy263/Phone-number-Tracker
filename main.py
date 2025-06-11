import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type, PhoneNumberFormat, is_valid_number, is_possible_number, format_number
from opencage.geocoder import OpenCageGeocode
key = "1740964dc9724b92a8b6e5eb05bfc55f"
def analyze():
    phone_number = entry.get()
    try:
        parsed = phonenumbers.parse(phone_number)
        info = ""
                                                      
        info += f"📍 Location: {geocoder.description_for_number(parsed, 'en')}\n"
        location_name = geocoder.country_name_for_number(parsed,'en')
        cage = OpenCageGeocode(key)
        results = cage.geocode(location_name)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        info += f"🌍 Latitude: {lat}\n"
        info += f"🌍 Longitude: {lng}\n"
        info += f"📡 Carrier: {carrier.name_for_number(parsed, 'en')}\n"
        info += f"🕒 Timezones: {timezone.time_zones_for_number(parsed)}\n"
        info += f"✅ Valid: {is_valid_number(parsed)}\n"
        info += f"🛠️ Possible: {is_possible_number(parsed)}\n"
        info += f"🌐 Format (Intl): {format_number(parsed, PhoneNumberFormat.INTERNATIONAL)}\n"
        info += f"🌐 Format (Natl): {format_number(parsed, PhoneNumberFormat.NATIONAL)}\n"

        output.config(state="normal")
        output.delete(1.0, tk.END)
        output.insert(tk.END, info)
        output.config(state="disabled")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid number or format\n{e}")

# GUI window
root = tk.Tk()
root.configure(bg = "skyblue")
root.title("Phone Number Tracker")
root.geometry("500x500")

label = tk.Label(root, text ="Enter phone number (with + countrycode):",bg="skyblue",fg="black",font=("Arial",15,"bold"))
label.pack(pady=35)
placeholder_text = "e.g +234...."
def on_entry_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, placeholder_text)
        entry.config(fg="gray")
entry = tk.Entry(root, width=35,font=("Arial",13,"italic"))
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focus_out)

entry.pack()
entry.insert(0,placeholder_text)

btn = tk.Button(root, text="Track...", command=analyze,bg="green",fg="white",font=("Arial",13,"bold"),activebackground="darkgreen")
btn.pack(pady=10)

output = tk.Text(root, height=15, width=35, state="disabled",bg="skyblue")
output.pack()
 
root.mainloop()

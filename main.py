import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password) :
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]" , password) :
        score += 1
    if re.search(r"[a-z]" , password) :
        score += 1
    if re.search(r"[0-9]" , password) :
        score += 1
    if re.search("r[@$!%*?#]" , password) :
        score += 1

    return score


def evaluate_password():
    password = entry.get()
    score = check_password_strength(password)

    if score <= 2:
        result = "❌ رمز خیلی ضعیف "
        color = "red"
    elif 3 <= score <= 4 :
        result = "⚠️ رمز متوسط"
        color = "orange"
    else:
        result = "✅ رمز قوی"
        color = "green"


    label_result.config(text = result , fg = color)
    messagebox.showinfo("نتیجه" , result)


root = tk.Tk()
root.title("Password Advisor")
root.geometry("350x200")

label = tk.Label(root , text = "رمز عبور را وارد کنید:")
label.pack(pady = 10)

entry = tk.Entry(root , show = "*" , width = 30)
entry.pack()

btn = tk.Button(root , text = "بررسی" , command = evaluate_password)
btn.pack()

label_result = tk.Label(root , text = "" , font = ("Arial" , 12))
label_result.pack()

root.mainloop()
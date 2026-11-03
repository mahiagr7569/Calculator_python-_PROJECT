import tkinter as tk
import math

# ---------------- FUNCTIONS ----------------

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expr = entry.get().replace("^", "**")
        result = eval(expr)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        save_history(f"{expr} = {result}")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def square():
    try:
        num = float(entry.get())
        result = num ** 2
        entry.delete(0, tk.END)
        entry.insert(0, result)
        save_history(f"{num}^2 = {result}")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        num = float(entry.get())
        if num < 0:
            raise ValueError
        result = math.sqrt(num)
        entry.delete(0, tk.END)
        entry.insert(0, result)
        save_history(f"√{num} = {result}")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def save_history(text):
    with open("history.txt", "a") as f:
        f.write(text + "\n")

def show_history():
    win = tk.Toplevel(root)
    win.title("History")
    win.geometry("250x300")

    text = tk.Text(win, bg="#1e1e1e", fg="white")
    text.pack(fill="both", expand=True)

    try:
        with open("history.txt", "r") as f:
            text.insert(tk.END, f.read())
    except:
        text.insert(tk.END, "No history found")

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("320x500")
root.configure(bg="#121212")

# Display
entry = tk.Entry(root, font=("Segoe UI", 22), bd=0,
                 bg="#1e1e1e", fg="white", justify="right")
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Button Frame
frame = tk.Frame(root, bg="#121212")
frame.pack()

# Button Style
btn = {
    "font": ("Segoe UI", 14),
    "width": 5,
    "height": 2,
    "bd": 0
}

# Row-wise Buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+", "="]
]

for i, row in enumerate(buttons):
    for j, val in enumerate(row):
        if val == "=":
            action = calculate
            color = "#00C853"
        else:
            action = lambda x=val: press(x)
            color = "#2c2c2c"

        tk.Button(frame, text=val, bg=color, fg="white",
                  command=action, **btn)\
            .grid(row=i, column=j, padx=5, pady=5)

# Extra Buttons
extra = [
    ("C", clear, "#D50000"),
    ("x²", square, "#3a3a3a"),
    ("√", sqrt, "#3a3a3a"),
    ("^", lambda: press("^"), "#3a3a3a")
]

for i, (text, cmd, color) in enumerate(extra):
    tk.Button(frame, text=text, bg=color, fg="white",
              command=cmd, **btn)\
        .grid(row=4, column=i, padx=5, pady=5)

# History Button
tk.Button(root, text="History", font=("Segoe UI", 12),
          bg="#2962FF", fg="white", command=show_history)\
    .pack(fill="x", padx=10, pady=10)

# Run
root.mainloop()
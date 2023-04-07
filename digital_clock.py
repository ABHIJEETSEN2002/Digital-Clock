import tkinter as tk
import time

# Create a window
window = tk.Tk()
window.title("Clock")

# Create a label to display the time
label = tk.Label(window, font=("Arial", 80), bg="white")
label.pack(padx=50, pady=50)

# Update the clock every second
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    window.after(1000, update_clock)

update_clock()
window.mainloop()

import tkinter as tk
from time import strftime

clock = tk.Tk()
clock.title("Digital Clock")
clock.geometry("300x100")

time_label = tk.Label(clock, font=("Arial", 36), bg="black", fg="lime")
time_label.pack(expand=True, fill="both")

def update_time():
    time_label.config(text=strftime("%H:%M:%S"))
    clock.after(1000, update_time)

update_time()
clock.mainloop()
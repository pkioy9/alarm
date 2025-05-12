import tkinter as tk
from tkinter import messagebox
import time
import threading


def start_alarm():
    try:
        seconds = int(entry.get())
        if seconds <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Введите положительное целое число секунд.")
        return

    button.config(state='disabled')
    label.config(text="Будильник установлен...")

    def wait_and_ring():
        time.sleep(seconds)
        label.config(text="⏰ Время вышло!")
        playsound('alarm.wav') 
        button.config(state='normal')

    threading.Thread(target=wait_and_ring, daemon=True).start()

root = tk.Tk()
root.title("Будильник")

root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="Введите время (в секундах):")
label.pack(pady=10)

entry = tk.Entry(root, justify='center')
entry.pack()

button = tk.Button(root, text="Установить будильник", command=start_alarm)
button.pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox
import FirstPage as F1


root = tk.Tk()
root.title("Mr. Doctor")
root.geometry("500x700")
root.resizable(False,False)

F1.FirstPage(root,tk)

root.mainloop()

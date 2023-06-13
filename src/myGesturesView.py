import tkinter as tk
from tkinter import *
import MLScript_2
import mainView
import os
class MyGesturesView(tk.Frame):
    back_button = None
    showAllGestures_button = None
    listbox = None
    title_label = None
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.back_button = tk.Button(self, text="Back", font=("Arial",15), command=self.backToMainView)
        self.showAllGestures_button = tk.Button(self, text="Show All Gestures", font=("Arial",20), command=self.showAllGestures)
        self.back_button.pack(side=tk.BOTTOM, pady=50)
        self.showAllGestures_button.pack(side=tk.TOP, pady=50)
        self.listbox = Listbox(self)
       
    def showAllGestures(self):
        if not self.title_label:
            self.title_label = tk.Label(self, text="Defined gestures")
            self.title_label.pack()
        self.listbox.delete(0, tk.END)
        items = os.listdir(MLScript_2.DATA_PATH)
        folders = [item for item in items if os.path.isdir(os.path.join(MLScript_2.DATA_PATH, item))]
        for i in folders:
            self.listbox.insert(tk.END, i)
        self.listbox.pack()

    def backToMainView(self):
        self.pack_forget()
        mainView.MainView(self.parent).pack()

     

        
        
        
  


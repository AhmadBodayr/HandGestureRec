import tkinter as tk
from tkinter import *
import MLScript
import shutil
import mainView
import os
class ModelTestingView(tk.Frame):
    back_button = None
    modelsBox = None
    models_label = None
    testModel_button = None

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.howTo = tk.Label(self, text=" Select a model from below and press test model", pady=10)
        self.howTo.pack()
        self.back_button = tk.Button(self, text="Back", font=("Arial",15), command=self.backToMainView)
        self.back_button.pack(side=tk.BOTTOM)
        self.modelsBox= Listbox(self, selectmode=SINGLE)
        self.createdModels_label = tk.Label(self, text="Created Models")
        self.createdModels_label.pack()
        for entry in os.scandir(MLScript.DATA_PATH3):
            if entry.is_dir() and entry.name != ".DS_Store":
                self.modelsBox.insert(tk.END, entry.name)
        self.modelsBox.pack()
        self.testModel_button = tk.Button(self, text="Test Model", font=("Arial",15), command=self.testModel)
        self.testModel_button.pack(pady=20)

    def backToMainView(self):
        self.pack_forget()
        mainView.MainView(self.parent).pack()
    
    def testModel(self):
        selected_index = self.modelsBox.curselection() 
        if selected_index:
            selectedModel = self.modelsBox.get(selected_index)
            MLScript.realtime_testing(selectedModel)


            
            
            
                

            
        


     

        
        
        
  


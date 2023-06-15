import tkinter as tk
from tkinter import *
import MLScript
import shutil
import mainView
import os
class MyModelsView(tk.Frame):
    back_button = None
    modelsBox = None
    dataSetsBox = None
    models_label = None
    dataSets_label = None
    createModel_button = None
    modelName_entry = None

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.howTo = tk.Label(self, text="To create a model, select a predefined dataset then press create model", pady=10)
        self.howTo.pack()
        self.back_button = tk.Button(self, text="Back", font=("Arial",15), command=self.backToMainView)
        self.back_button.pack(side=tk.BOTTOM)
        self.dataSetsBox = Listbox(self, selectmode=tk.SINGLE)
        self.modelsBox= Listbox(self)
        sets = os.listdir(MLScript.DATA_PATH2)
        models = os.listdir(MLScript.DATA_PATH3)
        self.dataSets_label = tk.Label(self, text="Defined DataSets")
        self.dataSets_label.pack()    
        folders = [item for item in sets if os.path.isdir(os.path.join(MLScript.DATA_PATH2, item))]
        for i in folders:
            self.dataSetsBox.insert(tk.END, i)
        self.dataSetsBox.pack()
        self.createdModels_label = tk.Label(self, text="Created Models")
        self.createdModels_label.pack()
        for entry in os.scandir(MLScript.DATA_PATH3):
            if entry.is_dir():
                self.modelsBox.insert(tk.END, entry.name)
        self.modelsBox.pack()
        self.createModel_button = tk.Button(self, text="create Model", font=("Arial",15), command=self.createModel)
        self.createModel_button.pack(pady=20)
        
        
        
       

    def backToMainView(self):
        self.pack_forget()
        mainView.MainView(self.parent).pack()
    
    def createModel(self):
        selected_index = self.dataSetsBox.curselection()  # Get the index of the selected item
        if selected_index:
            self.creationInProgress_label = tk.Label(self, text="Creating your model this might take a few minutes !", font=("Arial", 25, "bold"), pady=10)
            self.creationInProgress_label.pack()
            selectedSet = self.dataSetsBox.get(selected_index)
            MLScript.build_data_and_labels(selectedSet)
            MLScript.build_ML_model(selectedSet)
            self.creationInProgress_label.pack_forget()
            self.modelsBox.insert(tk.END, selectedSet)


            
            
            
                

            
        


     

        
        
        
  


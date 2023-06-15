import tkinter as tk
from tkinter import *
import MLScript
import shutil
import mainView
import os
class MyDataSetsView(tk.Frame):
    back_button = None
    
    definedGesturesBox = None
    selectedGesturesBox = None
    dataSetsBox = None
    gestures_label = None
    dataSets_label = None
    addSelected_button = None
    delete_button = None
    createDataSet_button = None
    dataSetName_entry = None

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.howTo = tk.Label(self, text="To create a dataset choose a name for it, then choose gestures from the predefined getsures, then select create Dataset", pady=10)
        self.howTo.pack()
        self.definedGesturesBox = Listbox(self, selectmode=tk.MULTIPLE)
        self.dataSetsBox = Listbox(self)
        self.selectedGesturesBox = Listbox(self)
        self.gestures_label = tk.Label(self, text="Defined Gestures")
        self.gestures_label.pack()
        gestures = os.listdir(MLScript.DATA_PATH)
        sets = os.listdir(MLScript.DATA_PATH2)
        folders = [item for item in gestures if os.path.isdir(os.path.join(MLScript.DATA_PATH, item))]
        for i in folders:
            self.definedGesturesBox.insert(tk.END, i)
        self.definedGesturesBox.pack()
        self.dataSets_label = tk.Label(self, text="Defined DataSets")
        self.dataSets_label.pack()    
        folders = [item for item in sets if os.path.isdir(os.path.join(MLScript.DATA_PATH2, item))]
        for i in folders:
            self.dataSetsBox.insert(tk.END, i)
        self.dataSetsBox.pack()
        self.selectedGestures_label = tk.Label(self, text="Selected Gestures")
        self.selectedGestures_label.pack()
        self.selectedGesturesBox.pack()
        self.name_label = tk.Label(self, text="Enter Your DataSet Name: ")
        self.name_label.pack(side=tk.LEFT)
        self.dataSetName_entry = tk.Entry(self)
        self.dataSetName_entry.pack(side=tk.LEFT)
        self.addSelected_button = tk.Button(self, text="Add Selected", font=("Arial",15), command=self.add_selected_items)
        self.back_button = tk.Button(self, text="Back", font=("Arial",15), command=self.backToMainView)
        self.createDataSet_button = tk.Button(self, text="create Dataset", font=("Arial",15), command=self.createDataSet)
        self.delete_button = tk.Button(self, text="Remove All", font=("Arial",15), command=self.emptySet)
        self.createDataSet_button.pack(side=tk.LEFT, pady=20)
        self.delete_button.pack(side=tk.LEFT, pady=20)
        self.addSelected_button.pack(side=tk.LEFT, pady=20)
        self.back_button.pack(side=tk.RIGHT)
        
       

    def backToMainView(self):
        self.pack_forget()
        mainView.MainView(self.parent).pack()
    
    def add_selected_items(self):
        selected_items = self.definedGesturesBox.curselection()
        for index in selected_items:
            item = self.definedGesturesBox.get(index)
            self.selectedGesturesBox.insert(tk.END, item)

    def emptySet(self):
        self.selectedGesturesBox.delete(0, tk.END)

    def createDataSet(self):
        if self.dataSetName_entry.get() != "" and self.selectedGesturesBox.size != 0:
            dest_dir = os.path.join(MLScript.DATA_PATH2, self.dataSetName_entry.get())
            if os.path.exists(dest_dir):
                print(f"Directory {dest_dir} already exists.")
                return
            os.makedirs(dest_dir)
            selected_items = self.selectedGesturesBox.get(0, tk.END)
            for gesture in selected_items:
                src_dir = os.path.join(MLScript.DATA_PATH, gesture)
                dest_dir = os.path.join(MLScript.DATA_PATH2, self.dataSetName_entry.get(), gesture)
                if os.path.isdir(src_dir):
                    shutil.copytree(src_dir, dest_dir)
                else:
                    shutil.copy(src_dir, dest_dir)
            self.dataSetsBox.insert(tk.END, self.dataSetName_entry.get())
            self.dataSetName_entry.delete(0, tk.END)
            self.selectedGesturesBox.delete(0, tk.END) 
            
            
                

            
        


     

        
        
        
  


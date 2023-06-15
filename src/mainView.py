import tkinter as tk
from tkinter import *
import MLScript
import myGesturesView
import myModelsView
import myDataSetsView
import modelTestingView
import os
class MainView(tk.Frame):
    definedGestures = 0
    header_label = None
    gestureName_label = None
    gestureName_entry = None
    createGesture_button = None
    myModels_button = None
    myGestures_button = None
    testModels_button = None
    myDataSets_button = None
    listbox = None
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack()
        if self.definedGestures == 0:
            self.header_label = tk.Label(self, text="Enter a gesture name then press Create Gesture to define a new gesture", font=("Arial", 15, "bold"), pady=10)
            self.header_label.pack()
        self.gestureName_label = tk.Label(self, text="Enter Gesture Name")
        self.gestureName_entry = tk.Entry(self)
        self.createGesture_button = tk.Button(self, text="Create Gesture", font=("Arial",20), command=lambda:self.gestureTaking(self.gestureName_entry.get()))
        self.myGestures_button = tk.Button(self, text="My Gestures", font=("Arial",20), command=self.goToMyGesturesView)
        self.myModels_button = tk.Button(self, text="My Models", font=("Arial",20), command=self.goToMyModels)
        self.testModels_button = tk.Button(self, text="Test a Model", font=("Arial",20), command=self.goToModelsTesting)
        self.myDataSets_button = tk.Button(self, text="My DataSets", font=("Arial",20), command=self.showMyDatasetsView)
        self.myGestures_button.pack(side=tk.BOTTOM, pady=10)
        self.gestureName_label.pack(side=TOP)
        self.gestureName_entry.pack(side=TOP)
        self.createGesture_button.pack(side=tk.TOP, pady=50)
        self.myModels_button.pack(side=tk.BOTTOM, pady=10)
        self.testModels_button.pack(side=tk.BOTTOM, pady=10)
        self.myDataSets_button.pack(side=tk.BOTTOM, pady=10)
    
    def gestureTaking(self, gesture):
        if gesture == "":
            return
        MLScript.define_gestures(gesture)
        MLScript.create_Gestures_folder()
        MLScript.data_collection_cam_loop()
        self.gestureName_entry.delete(0, tk.END) 
        self.definedGestures += 1
        self.pack_forget()
        self.pack()

    def goToMyGesturesView(self):
        self.pack_forget()
        myGesturesView.MyGesturesView(self.parent).pack()

    def goToMyModels(self):
        self.pack_forget()
        myModelsView.MyModelsView(self.parent).pack()
        
    def showMyDatasetsView(self):
        self.pack_forget()
        myDataSetsView.MyDataSetsView(self.parent).pack()
    def goToModelsTesting(self):
        self.pack_forget()
        modelTestingView.ModelTestingView(self.parent).pack()

    
    



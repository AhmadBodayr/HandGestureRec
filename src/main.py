
import os
import sys
import time
import MLScript
import mainView
import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Main window
root = tk.Tk()
root.title("ML Based Hand Gesture Detection")
root.geometry("600x600")
# Header
header_frame = tk.Frame(root, bg="#222831", width=600, height=80)
header_frame.pack(side=tk.TOP, fill=tk.X)
header_label = tk.Label(header_frame, text="Dynamic Hand Gesture Recognition", font=("Arial", 24, "bold"), fg="#986ff7", bg="#222831", pady=20)
header_label.pack()
# Main View
MainWindow = mainView.MainView(root)

root.mainloop()




# def plot_results():
#     gesture_names = list(MLScript.result_mapa.keys())
#     prediction_accuracy = list(MLScript.result_mapa.values())
#     # Bar chart
#     fig, ax = plt.subplots(figsize=(8, 6))
#     ax.bar(gesture_names, prediction_accuracy)
#     ax.set_xlabel("Gesture Name")
#     ax.set_ylabel("Prediction Accuracy")
#     ax.set_title("Gesture Recognition Accuracy")
#     plt.xticks(rotation=45)
#     # Pie chart
#     fig, ax = plt.subplots(figsize=(8, 6))
#     ax.pie(prediction_accuracy, labels=gesture_names, autopct='%1.1f%%', startangle=90)
#     ax.axis('equal')
#     ax.set_title("Gesture Recognition Accuracy")
#     plt.show()
# def realTime_testing():
#     MLScript.realtime_testing()
# def initModelTraining():
#     MLScript.build_ML_model()
# def initPipeline():
#     noOfGestures = 0
#     gestures = []
#     if noOfGestures_entry.get():e
#         noOfGestures = int(noOfGestures_entry.get())
#     if gesturesNames_entry.get():
#         gestures = gesturesNames_entry.get().split(',')
#     if noOfGestures != len(gestures) or noOfGestures == 0:
#         print("error: check input data")
#         return
#     print("ML Pipeline Initiated")
#     # Define user gestures
#     MLScript.define_gestures(gestures)
#     # Creating folders
#     MLScript.create_folders()
#     # openCv & mediapipe cam loop for collecting data
#     MLScript.data_collection_cam_loop()
#     # Making the x andy tensors and splitting
#     MLScript.build_data_and_labels()
# # Header
# header_frame = tk.Frame(root, bg="#222831", width=600, height=80)
# header_frame.pack(side=tk.TOP, fill=tk.X)
# header_label = tk.Label(header_frame, text="Dynamic Hand Gesture Recognition", font=("Arial", 24, "bold"), fg="#986ff7", bg="#222831", pady=20)
# header_label.pack()
# # Central Frame
# main_frame = tk.Frame(root) 
# main_frame.pack()
# listbox = Listbox(main_frame)
# listbox.pack()
# noOfGestures_label = tk.Label(main_frame, text="Number of gestures")
# noOfGestures_entry = tk.Entry(main_frame)
# gesturesNames_label = tk.Label(main_frame, text=".csv format gestures names")
# gesturesNames_entry = tk.Entry(main_frame)
# noOfGestures_label.pack(side=tk.TOP)
# noOfGestures_entry.pack(side=tk.TOP)
# gesturesNames_label.pack(side=tk.TOP)
# gesturesNames_entry.pack(side=tk.TOP)

# start_button = tk.Button(main_frame, text="Start", command=initPipeline)
# train_button = tk.Button(main_frame, text="Train", command=initModelTraining)
# test_button = tk.Button(main_frame, text="Realtime Testing", command=realTime_testing)
# plot_button = tk.Button(main_frame, text="plot results", command=plot_results)
# start_button.pack(side=tk.TOP, pady=10)
# train_button.pack(side=tk.TOP, pady=10)
# test_button.pack(side=tk.TOP, pady=10)
# plot_button.pack(side=tk.TOP, pady=10)




# working params
# learning_rate = .001
# adam = Adam(learning_rate)

# working model
    # model = Sequential()
    # model.add(LSTM(32, return_sequences=True, activation='relu'))
    # model.add(LSTM(64, return_sequences=True, activation='relu'))
    # model.add(LSTM(32, return_sequences=False, activation='relu'))
    # model.add(Dense(32, activation='relu'))
    # model.add(Dense(16, activation='relu'))
    # model.add(Dense(actions.shape[0], activation='softmax'))
    # # Compiling the model
    # model.compile(optimizer=adam ,loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    # # Fitting the model
    # model.fit(X_train, y_train, epochs=120)

# Imports   
import os
import time
import sys
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import tensorflow as tf
import mediapipe as mp
import cv2
import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers.legacy import Adam
from tensorflow.keras.utils import plot_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score

baseCounter = 0

learning_rate = .001
adam = Adam(learning_rate)
# Setting up the learning rate
# learning_rate = 0.0001 
# adam = adam(learning_rate)

possible = False
global model
actions = np.array([])
# Number of videos worth of data
no_sequences = 80
# Datapath
# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Create a subdirectory in the script directory to store the data
DATA_PATH = os.path.join(script_dir, "Gestures") 
DATA_PATH2 = os.path.join(script_dir, "DataSets") 
DATA_PATH3 = os.path.join(script_dir, "Models") 

try:
    os.makedirs(os.path.join(DATA_PATH2))
except:
    pass
try:
    os.makedirs(os.path.join(DATA_PATH3))
except:
    pass
# Videos frames as input and labels as result
sequences, labels = [], []

# Videos are going to be 30 frames in length
sequence_length = 30

action = ""
X = np.array([])
y = np.array([])
mp_holistic = mp.solutions.holistic 
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic

# Get the absolute path of the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the holistic model file
model_path = os.path.join(script_dir, 'models', 'holistic.pb')


# Early stopping class
class earlyStop(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        global baseCounter
        if logs.get("categorical_accuracy") > 0.9:
            if baseCounter == 3:
                self.model.stop_training = True
            else:
                baseCounter += 1
        else:
            baseCounter = 0

# definning gesture /////////////////
def define_gestures(gesture):
    global action
    global result_mapa
    global result_helper
    action = gesture
    print("Gesture defined successfully")

# Setting up mediapipe /////////////////////  

# Draws the landmarks on screen ++++++++++++++++++
def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS) # Draw right hand connections
    print("Landmarks drawn successfully")
    
# Starts the mediapipe detection ++++++++++++++++++++++++++++
def mediapipe_detection(image, model): 
    # Converting from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Image is no longer writeable
    image.flags.writeable = False
    # Make prediction 
    results = model.process(image)
    # setting back to writeable
    image.flags.writeable = True
    # Converting again to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

# Extracts the keypoints +++++++++++++++++++++++++
def extract_keypoints(results): 
    # Initializing land marks arrays
    rh, lh = [], []
    # Extracting right hand landmarks    
    if results.right_hand_landmarks:
        for res in results.right_hand_landmarks.landmark:
            test = np.array([res.x, res.y, res.z])
            rh.append(test)
        rh = np.array(rh).flatten()
    else:    
        rh.append(np.zeros(3 * 21))
        rh = np.array(rh).flatten()
    # Extracting left hand landmarks
    if results.left_hand_landmarks:
        for res in results.left_hand_landmarks.landmark:
            test = np.array([res.x, res.y, res.z])
            lh.append(test)
        lh = np.array(lh).flatten()
    else:    
        lh.append(np.zeros(3 * 21))
        lh = np.array(lh).flatten()
    
    return np.concatenate([lh, rh])



def create_Gestures_folder():
    global action
    global DATA_PATH
    global sequences
    global no_sequences 
    for sequence in range(no_sequences):
        try: 
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass     
    print("Folders created successfully")

# The camera loop for data gathering
def data_collection_cam_loop():
    global action
    global sequences
    global sequence_length
    global DATA_PATH
    sequence_length = 30
    print("Started Collecting data")
    cap = cv2.VideoCapture(0)
    # Set mediapipe model 
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.8) as holistic:
        for sequence in range(no_sequences):
            for frame_num in range(sequence_length):
                # Read feed
                ret, frame = cap.read()
                # Make detections
                image, results = mediapipe_detection(frame, holistic)
                # Draw landmarks
                draw_landmarks(image, results)
                # Wait logic
                if frame_num == 0: 
                    cv2.putText(image, f'collecting video {sequence} for {action}', (120,200), 
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255, 0), 4, cv2.LINE_AA)
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                    cv2.waitKey(500)
                else: 
                    cv2.putText(image, 'Collecting frames for {} Video Number {}'.format(action, sequence), (15,12), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    # Show to screen
                    cv2.imshow('OpenCV Feed', image)
                # Export keypoints
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)
                # Break
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)



# Building the input data and labels
def build_data_and_labels(selectedSet):
    global DATA_PATH2
    global sequences
    global sequence_length
    global labels
    global possible
    global X
    global y   
    global actions
    # Building the data and labels
    temp = []
    for entry in os.scandir(os.path.join(DATA_PATH2, selectedSet)):
        if entry.is_dir():
            temp.append(entry.name)
    actions = np.array(temp)
    actions.sort()
    label_map = {label:num for num, label in enumerate(actions)}
    for action in actions:
        for sequence in os.listdir(os.path.join(DATA_PATH2, selectedSet, action)):
            if sequence != '.DS_Store':
                sequence_int = int(sequence)
                window = []
                for frame_num in range(sequence_length):
                    res = np.load(os.path.join(DATA_PATH2, selectedSet, action, sequence, "{}.npy".format(frame_num)))
                    window.append(res)
                window = np.array(window)
                sequences.append(window)
                labels.append(label_map[action])
    # Setting up the data and labels
    X = np.array(sequences)
    y = to_categorical(labels).astype(int)
    possible = True
    print(" Training and testing tesnsors are ready!!!")

# Building the ML model
def build_ML_model(modelName):
    global possible
    global X
    global y
    global DATA_PATH3   
    global model
    global adam
    global baseCounter
    global actions
    if possible == False:
        print("Error: Cant build the model yet, data not ready")
        return
    baseCounter = 0
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, activation='relu'))
    model.add(LSTM(128, return_sequences=True, activation='relu'))
    model.add(LSTM(64, return_sequences=False, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(actions.shape[0], activation='softmax'))
    # Compilling the model
    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['categorical_accuracy'])
    # Fitting the model
    model.fit(X, y, epochs=500, callbacks=[earlyStop()])
    # Saving the model
    model.save(os.path.join(DATA_PATH3, modelName))
    print("Model finished training successfully!")

def realtime_testing(modelName):
    # actions dont forget
    global sequence_length
    global DATA_PATH3
    temp = []
    for entry in os.scandir(os.path.join(DATA_PATH2, modelName)):
        if entry.is_dir():
            temp.append(entry.name)
    newActions = np.array(temp)
    newActions.sort()
    loadedModel = tf.keras.models.load_model(os.path.join(DATA_PATH3, modelName))
    # The sequence of frames
    sequence = []
    # The prediction thresh hold 
    threshold = .90
    # Screen video capture and realtime detection
    cap = cv2.VideoCapture(0)
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.8) as holistic:
        while cap.isOpened():
            # Read feed
            ret, frame = cap.read()
            # Make detections
            image, results = mediapipe_detection(frame, holistic)
            # Draw landmarks
            draw_landmarks(image, results)
            # Realtime prediction logic
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            if len(sequence) >= sequence_length:
                currVid = np.array([sequence[-sequence_length:]])
                prediction = np.squeeze(loadedModel.predict(currVid))
                accuracy = prediction[prediction.argmax()]
                if accuracy >= threshold:
                    outputToScreen = newActions[prediction.argmax()]
                    cv2.putText(image, outputToScreen, (120, 200), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255, 0), 4, cv2.LINE_AA)
                else:
                    cv2.putText(image, "No Action Detected", (120,200), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0, 0), 4, cv2.LINE_AA)  
            # Presenting to the screen
            cv2.imshow("OpenCV Feed", image)
            # Breaking
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break          
        # Safe release
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)
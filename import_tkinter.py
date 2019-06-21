import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time

import os
import cv2
import numpy as np
import faceRecognition as fr
from excel import *
import threading


class App:
     def __init__(self, window, window_title, video_source=0):
        self.label=0
        self.window = window
        self.window.title(window_title)
        #self.window.iconbitmap("E:/project/isro.png")  
        self.video_source = video_source
 
         # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
         # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()

        
        terminate=0
        x1=0
        y1=0
        
           
        # Button that lets the user take a snapshot

        self.btn_snapshot=tkinter.Button(window, text='Take attandence', width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        self.btn_check=tkinter.Button(window, text='CHeck again', width=50, command=self.check)
        self.btn_check.pack(anchor=tkinter.CENTER, expand=True)
 
 
         # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        print("out")
        self.update()
 
        self.window.mainloop()
 
     def snapshot(self):
         # Get a frame from the video source
         print(self.label)
         record(self.label+1)
         self.window.quit()
         #ret, frame = self.vid.get_frame()
 
         #if ret:
             #cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

     def check(self):
          self.window.after(self.delay, self.update)
 

     def update(self):
         # Get a frame from the video source
         
         ret, frame,a ,label= self.vid.get_frame()
         self.btn_snapshot['text']=a
         
         self.label=label
 
         if ret:

             self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
             self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
            
         #
         if  a=='Take attandence':
            self.window.after(self.delay, self.update)
 
 


class MyVideoCapture:
     def __init__(self, video_source=0):
         # Open the video source
         self.vid = cv2.VideoCapture(video_source)
         if not self.vid.isOpened():
             raise ValueError("Unable to open video source", video_source)
 
         # Get video source width and height
         self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
         self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
     def get_frame(self):


         if self.vid.isOpened():
             ret, frame = self.vid.read()
             predicted_name='Take attandence'
             label=0

             if ret:
                 # Return a boolean success flag and the current frame converted to BGR
                 faces_detected,gray_img=fr.faceDetection(frame)

                 for (x,y,w,h) in faces_detected:
                     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=7)

                 resized_img = cv2.resize(frame, (1000, 700))
                 
                 #print(faces_detected)

                 for face in faces_detected:
                    (x,y,w,h)=face
                    roi_gray=gray_img[y:y+w, x:x+h]

                    label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
                    if confidence<39:
                       print("confidence:",confidence)
                       print("label:",label)
                       fr.draw_rect(frame,face)

                       predicted_name=name[label]
                       print(predicted_name)
                       fr.put_text(frame,predicted_name,x,y)
                       break

             
                 
                 return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),predicted_name,label)
             else:
                 return (ret, None,'Take attandence',0)
         else:
             return (ret, None,'Take attandence',0)
 
     # Release the video source when the object is destroyed
     def __del__(self):
         if self.vid.isOpened():
             self.vid.release()
 
 # Create a window and pass it to the Application object

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#Load saved training data

name = {0 : "Priyanka",1 : "Kangana",3:"kuldeep"}

terminate=0
x1=0
y1=0
btn_text='snapshot'
App(tkinter.Tk(), "ISRO attandence System")

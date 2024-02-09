import tkinter as tk
from tkinter import filedialog
from tkinter import * 
from PIL import Image,ImageTk
import numpy as np

# Initializing the GUI
top=tk.Tk()
top.geometry("800x600")
top.title("Age and Gender Detector")
top.configure(background="#CDCDCD")

# loading the model
from keras.models import load_model
model=load_model("Age_Sex_Detection.keras")

# Initializing the labels (1 for age and 1 for sex)
Label1=Label(top,background="#CDCDCD",font=("arial",15,"bold"))
Label2=Label(top,background="#CDCDCD",font=("arial",15,"bold"))
sign_image=Label(top)

# Defining Defect function which detects the age and gender of the person in the image using the model
def Defect(file_path):
    global Label1, Label2
    image = Image.open(file_path)
    image = image.resize((48, 48))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0                  # Normalize the image
    print(image.shape)
    sex_f = ["Male", "Female"]
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    sex = int(np.round(pred[0][0]))
    print("Predicted age is:", age)
    print("Predicted gender is:", sex_f[sex])
    Label1.configure(foreground="#011638", text=age)
    Label2.configure(foreground="#011638", text=sex_f[sex])



# Defining show_detect button function
def show_Detect_Button(file_path):
    Detect_b=Button(top,text="Detect image",command=lambda: Defect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#364156",foreground="white",font=("arial",10,"bold"))
    Detect_b.place(relx=0.79,rely=0.46) 

# Defining upload image function
def upload_image():
    global sign_image
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        Label1.configure(text="")
        Label2.configure(text="")
        show_Detect_Button(file_path)    
    except:
        pass    

Upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
Upload.configure(background="#364156",foreground="white",font=("arial",10,"bold"))
Upload.pack(side="bottom",pady=50)
sign_image.pack(side="bottom",expand=True)

Label1.pack(side="bottom",expand=True)
Label2.pack(side="bottom",expand=True)
heading=Label(top,text="Age and Gender Detector",pady=20,font=("arial",20,"bold"))
heading.configure(background="#CDCDCD",foreground="#364156")
heading.pack()
top.mainloop()

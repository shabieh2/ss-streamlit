import os
import shutil
import streamlit as st
from PIL import Image

st.title("Ember Optics Yolov5 Object Detection")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying using Ember Optics Proprietary Technology...")
    image.save("image.jpg", format='JPEG', quality=75)
    os.system("python yolov5/detect.py --source image.jpg --weights ./model/best.pt  --save-txt")

    image = Image.open("app/streamlit-ss/yolov5/runs/detect/exp/image.jpg")
    st.image(image, caption='Prediction.', use_column_width=True)
    st.write("")

    if os.path.exists("app/streamlit-ss/yolov5/runs/detect/exp/labels/image.txt"):
        st.write("Detected :sunglasses: :")
        with open ("yolov5/runs/detect/exp/labels/image.txt", 'r') as f:
            line = f.readlines()
            for i in range(len(line)):
                with open("label.txt", 'r') as f:
                    st.write(i, " ", f.read().split(",")[int(line[i].split(" ")[0])].replace("'", ""))
    else: 
        st.write("No detection.")

    #os.system("del image.jpg")
    os.remove("image.jpg")
    shutil.rmtree("yolov5/runs/")
    



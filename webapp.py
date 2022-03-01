import os
import io
import shutil
import streamlit as st
from PIL import Image
import torch
import tempfile
import streamlit as st
from configparser import ConfigParser
#import gdown
import os
import subprocess
import random
from PIL import Image

im1 = Image.open('./a.png')
st.image(im1, use_column_width=True)
st.title("Wildfire Detection")

uploaded_file = st.file_uploader("Choose an image or video", type=["jpg","jpeg","png","mp4"])
if uploaded_file is not None:
    

    image = Image.open(uploaded_file)
    model =torch.hub.load('./yolov5', 'custom', path='./model/best.pt',source='local')  #  source='local',force_reload = recache latest code
    model.eval()

    
    #st.image(image, caption='Uploaded Image.', use_column_width=True)
    imgs2=[image]
    results = model(imgs2, size=640)
    az=results.pandas().xyxy[0].name.unique()
    #st.text(az)
    results.render()
    
    
    
    
    
    
    
    
   
    image2 = Image.fromarray(results.imgs[0])
    
    st.image(image2, caption='Predicted Image.', use_column_width=True)
    
    #imgfile = Image.open(results)
    #results.render()
    #results.show()
    #image2 = Image.open(results)
    
    
    
    #st.image(imgfile, caption='prediction Image.', use_column_width=True)
    
    
    st.write("")
    
    
    #st.image(results, caption='Uploaded Image.', use_column_width=True)
    #st.write("Classifying using Ember Optics Proprietary Technology...")
    image.save("image.jpg", format='JPEG', quality=75)
    #os.system("python yolov5/detect.py --source image.jpg --weights ./model/best.pt --save-txt")
    
    #image = Image.open("yolov5/runs/detect/exp/image.jpg")
    #mage = Image.open("/home/appuser/venv/lib/python3.7/site-packages/streamlit/static/image.jpg")


    #st.image(image, caption='Predictions.', use_column_width=True)
    
    
    
    
    
        

    #image = Image.open("app/streamlit-ss/yolov5/runs/detect/exp/image.jpg")

    #st.image(image, caption='Prediction.', use_column_width=True)

    st.write("")

    if len(results.pandas().xyxy[0])!=0:
           
           st.write('WARNING!!! FOLLOWING RISK FACTORS FOUND: ', use_column_width=True)
           st.text(''.join([str(az[i]).upper()+' ' for i in range(len(az))]))
    else:
        st.write("No detection.")

    #os.system("del image.jpg")
    #os.remove("image.jpg")
    #shutil.rmtree("yolov5/runs/")
    



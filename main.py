import os
from fastapi import FastAPI, File, Request, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import tensorflow as tf
from absl import app, flags, logging
from absl.flags import FLAGS
from tensorflow.python.saved_model import tag_constants

global interpreter

# model path
model_path_tflite = "./checkpoints/yolov4-416-fp32.tflite"

# model loading
interpreter = tf.lite.Interpreter(model_path=model_path_tflite)

templates = Jinja2Templates(directory="templates")
app = FastAPI()

app.mount("/detections", StaticFiles(directory="detections"), name="detections")
op_text_path = "detections/ocr_output.txt"


@app.post("/results/")
async def create_files(request:Request, file:UploadFile = File(...)):
    if (file.filename != ""):
        file_name = "Test_images"+"/"+ file.filename
        print(file_name)

        if(os.path.isdir("Test_images") != True):
            os.mkdir("Test_images")

        contents = await file.read()
        # example of how you can save the file
        with open(file_name, "wb") as f:
            f.write(contents)
            f.close()
        os.system('python detect.py --images ' + file_name)
        
        return templates.TemplateResponse("result.html", {"request":request})
    else:
        return{"ERROR":"Please select the input png images."}


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("dash.html", {"request":request})

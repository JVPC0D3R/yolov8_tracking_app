from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
result = model.track(source =0, show = True, stream = True)

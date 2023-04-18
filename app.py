from ultralytics import YOLO
import supervision as sv
import cv2

# Load the model
model = YOLO("yolov8n.pt") 

# Use the model
for result  in model.track(source =0, show = False, stream = True):

    frame = result.orig_img
    detections = sv.Detections.from_yolov8(result)

    cv2.imshow("yolov8", frame)

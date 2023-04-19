from ultralytics import YOLO
import supervision as sv
import cv2

from modules.view import draw_trasnparent_bbox, draw_label, resize_img

# Load the model
model = YOLO("yolov8n.pt") 

# Use the model
for result  in model.track(source =0, show = False, stream = True):

    # Get frame
    frame = result.orig_img

    # Transform the detections format
    detections = sv.Detections.from_yolov8(result)

    # If YOLOv8 tracked something
    if result.boxes.id is not None:
        
        detections.tracker_id = result.boxes.id.cpu().numpy().astype(int)

        # Get object information
        for bbox, _, conf, class_id, tracker_id in detections:
            
            # Get bbox coordinates
            x0,y0,x1,y1 = bbox

            # Get label
            label = f'#{tracker_id} {model.model.names[class_id]}'

            # Draw transparent bounding box and write label
            draw_label(frame, label, int(x0), int(y0), int(x1), int(y1), id = tracker_id, font_scale = 1.5)
            draw_trasnparent_bbox(frame, int(x0), int(y0), int(x1), int(y1),tracker_id)

    # Show resized frame
    cv2.imshow("yolov8", resize_img(frame, 50))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

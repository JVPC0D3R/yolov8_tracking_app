# Welcome to YOLOv8 tracking app

<p align="justify">
This is a simple tracking application using native <a href="https://github.com/ultralytics/ultralytics">YOLOv8</a>  tracking features and custom ones.

## 🤠 tracker manager

YOLOv8 outputs usefull information about the tracks freatured in the present frame, but no information about the past, that is why I implemented a <a href='https://github.com/JVPRUGBIER/yolov8_tracking_app/blob/main/utils/tracker_manager.py'> Tracker Manager</a>. 

The TM stores the bounding box of each track from the last frame, so if your application demands speed measurements you can get such info and calculate the traveled distance (in pixels), if case you need to measure the distance in the real world you can use <a href='https://medium.com/hal24k-techblog/how-to-track-objects-in-the-real-world-with-tensorflow-sort-and-opencv-a64d9564ccb1'>this solution</a>.

</p>

## 📦 installation

To install the packages with pip run:

```
pip install -r requirements.txt
```

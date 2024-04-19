from ultralytics import YOLO

model1 = YOLO("yolov8n-pose.pt")
model2 = YOLO("yolov8n-seg.pt")

prediction = model1.predict(source='C:/Users/ok/Jupter Lab Files/video.mp4', show=True, save=True)

segmentation = model2.predict(source='C:/Users/ok/Jupter Lab Files/video.mp4', show=True, save=True)

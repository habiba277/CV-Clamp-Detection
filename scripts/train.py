from ultralytics import YOLO

# Download YOLOv11n
model = YOLO("yolo11n.pt")

# train the model 
model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=4
)
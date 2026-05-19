from ultralytics import YOLO

#load the trained model
model = YOLO("runs/detect/train-4/weights/best.pt")

# perform inference on the video
model.predict(
    source="video\Task.mp4",
    save=True,
    conf=0.25
)
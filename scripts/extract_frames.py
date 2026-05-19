import cv2
import os

video_path = "video/Task.mp4"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0
saved_count = 0

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % 15 == 0:

        output_path = f"{output_folder}/frame_{saved_count}.jpg"

        cv2.imwrite(output_path, frame)

        print(f"Saved: {output_path}")

        saved_count += 1

    frame_count += 1


    if saved_count == 50:
        break

cap.release()

print("Frames extraction completed.")
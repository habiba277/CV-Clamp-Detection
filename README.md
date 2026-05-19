# Clamp Detection using YOLO11

## Overview
This project trains a YOLO11 object detection model to detect clamps in industrial images.

## Dataset
- Custom annotated dataset
- YOLO format
- 1 class: clamp

## Training
Model: YOLO11n  
Epochs: 20  
Image Size: 640  
Device: CPU

## Results
- mAP50: 0.593
- Precision: 0.622
- Recall: 0.499

## Run Training

```bash
python scripts/train.py
```

## Run Inference

```bash
python inference.py
```
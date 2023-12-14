from ultralytics import YOLO

# Load the configuration
model = YOLO('yolov8m.yaml')

# Start training
results = model.train(data='bee_train.yaml', epochs=20, imgsz=640)
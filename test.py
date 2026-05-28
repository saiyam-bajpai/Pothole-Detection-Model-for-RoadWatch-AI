import os
os.chdir(r"C:\Users\asus\Downloads\RoadWatch AI")

from ultralytics import YOLO

model_path = r"C:\Users\asus\Downloads\RoadWatch AI\outputs\best.pt"
image_path = r"C:\Users\asus\Downloads\RoadWatch AI\testing\OIP.jpeg"

model = YOLO(model_path)

results = model.predict(
    source=image_path,
    conf=0.45,
    save=True,
    project=r"C:\Users\asus\Downloads\RoadWatch AI\runs",
    name="test_result"
)

print("Number of detections:", len(results[0].boxes))
print(f"Result saved to: C:\\Users\\asus\\Downloads\\RoadWatch AI\\runs\\test_result\\")
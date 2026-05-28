# 🚧 RoadWatch AI — Pothole Detection Model

> This is my individual contribution to **RoadWatch AI**, a team hackathon project that detects road damage in real-time using AI.

---

## 🏆 About the Hackathon Project

**RoadWatch AI** is a team-built system that automatically detects potholes and road damage from live video feeds using computer vision. The goal is to help municipalities and citizens identify and report road damage faster, reducing accidents and repair delays.

My role in the team was to **build and train the core AI detection model** — the brain of the entire system.

---

## 🧠 What This Repo Contains

This repository contains my part: the **YOLOv8-based pothole detection model**, trained from scratch on real road images.

| File | Description |
|------|-------------|
| `outputs/best.pt` | Trained YOLOv8 model (main deliverable) |
| `test.py` | Script to run detection on any road image |
| `README.md` | Project documentation |

---

## 🔍 How It Works

1. A road image or video frame is passed to the model
2. YOLOv8 scans the image and finds potholes
3. It draws a **bounding box** around each pothole with a confidence score
4. Output is passed to the rest of the team's pipeline for reporting

---

## 🛠️ Tech Stack

- **Model:** YOLOv8n (Ultralytics)
- **Language:** Python 3.10
- **Training Platform:** Google Colab (Tesla T4 GPU)
- **Dataset:** Roboflow Pothole Detection Dataset
- **Libraries:** `ultralytics`, `opencv-python`, `numpy`

---

## 📦 Model Details

| Property | Value |
|----------|-------|
| Architecture | YOLOv8n |
| Classes | `Pothole` |
| Confidence Threshold | `0.45` |
| Image Size | `640x640` |
| Epochs | `50` |

---

## 🚀 How to Use

### 1. Install dependencies
```bash
pip install ultralytics opencv-python
```

### 2. Run detection on an image
```bash
python test.py
```

Or use it directly in your code:
```python
from ultralytics import YOLO

model = YOLO("outputs/best.pt")

results = model.predict(
    source="your_road_image.jpg",
    conf=0.45,
    save=True
)
```

---

## 👥 Team

This model is **Part 1** of a multi-person hackathon project — RoadWatch AI.

- **Person 1 (Me):** AI model training — YOLOv8 pothole detection
- **Person 2:** Video processing pipeline — real-time frame detection
- **Person 3:** Backend & reporting system
- **Person 4:** Frontend & dashboard

---

## 📄 Dataset Credit

Dataset sourced from [Roboflow Universe — Pothole Detection](https://universe.roboflow.com/joseph-nelson/pothole-detection), licensed under CC BY 4.0.

## 👨‍💻 About

**Saiyam Bajpai** — B.Tech in Computer Science & Design @ MITS Gwalior | BS in Data Science @ IIT Madras.

This project taught me that great HCI is about removing friction between human intent and machine response — and that the best interface is the one you already have: your hands.

[![GitHub](https://img.shields.io/badge/GitHub-saiyam--bajpai-black?style=flat-square&logo=github)](https://github.com/saiyam-bajpai/Computer-Vision-based-Hand-Gesture-Control)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-saiyam--bajpai-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/saiyam-bajpai/)

---


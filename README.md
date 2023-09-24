# Aerial Maritime Object Detection with DETR-ResNet-50



## Project Overview:

This project utilizes the powerful **DETR-ResNet-50 model**, initially designed for COCO object detection, and fine-tuned it on the **Aerial Maritime Image Dataset** The dataset consists of 74 aerial maritime photographs captured via a Mavic Air 2 drone, containing 1,151 annotated bounding boxes for various objects, including docks, boats, lifts, jetskis, and cars. This is a multi-class problem aimed at maritime object detection from drone imagery.

**https://huggingface.co/spaces/TuningAI/DETR-BASE_Marine**

![download](https://github.com/Kirouane-Ayoub/DETR-Aerial-Maritime-Object-Detection/assets/99510125/657f331f-e8d9-4b3f-baa0-7adb8e4c4513)

## Dataset Description:

+ Dataset Name: Aerial Maritime Image Dataset
+ Number of Images: 74
+ Number of Bounding Boxes: 1,151
+ Object Classes: Docks, Boats, Lifts, Jetskis, Cars
+ Collection Method: Drone captured at 400 ft altitude

**https://universe.roboflow.com/jacob-solawetz/aerial-maritime**

## Use Cases:

+ **Boat Counting**: Detect and count the number of boats on water bodies (e.g., lakes) using quadcopter or drone imagery.
+ **Boat Lift Detection**: Identify if boat lifts have been taken out on the waterfront via drone surveillance.
+ **Car Detection**: Detect and locate cars within the maritime area using UAV drones.
+ **Habitability Assessment**: Determine which lakes are inhabited and to what extent based on detected objects.
+ **Property Monitoring**: Identify if visitors are present at lake houses or properties via quadcopter surveillance.
+ **Proof of Concept**: Demonstrates the feasibility of using UAV imagery for maritime projects and aerial object detection.

## Project Outcomes:

+ A fine-tuned **DETR-ResNet-50** model for maritime object detection.
+ Detection and classification of boats, docks, lifts, jetskis, and cars in aerial images.
+ Insights into the presence and density of objects in maritime areas.
+ Proof of concept for various UAV and maritime projects.

## License: MIT License (for the Aerial Maritime Image Dataset)

## Usage : 
```
pip install -r requirements.txt
python app.py
```
![Screenshot at 2023-09-21 11-52-11](https://github.com/Kirouane-Ayoub/DETR-Aerial-Maritime-Object-Detection/assets/99510125/3957385d-2900-4b70-bb07-5bfd88170432)

- **By Kirouane Ayoub**

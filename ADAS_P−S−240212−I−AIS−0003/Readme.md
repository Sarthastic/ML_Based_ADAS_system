# Advanced Driver Assistance System - ADAS (Yolov8) Project

Reference number: **P−S−240212−I−AIS−0003**

## **Overview**

This project implements an Advanced Driver Assistance System (ADAS) using YOLOv8 for object detection and lane detection. The system includes two custom-trained models: one for detecting pedestrians and vehicles and the other for recognizing traffic signs. Additionally, it features a lane detection algorithm for road lane analysis.

## **Google Colab Integration**

To run this project in Google Colab (Link at the end of this documentation), follow these steps:

1. Open the Colab Notebook provided in the repository.
2. Ensure that the Colab environment is configured with GPU acceleration. If not, navigate to **`Edit -> Notebook settings -> Hardware accelerator`** and set it to GPU.
3. Execute the code cells in the notebook sequentially, following the provided instructions.
4. When prompted for API keys, input the necessary keys for model download.
5. Upload images or videos at specified places in the notebook for inference.
6. Download processed results from the Colab "Files" section.

## **Setup**

1. **API Key Setup:**
    - API keys have been hard-coded for simplicity. No manual input is required in the documentation.
2. **Model Training (Optional):**
    - If you choose to train models, follow the provided steps for dataset export and training configuration.

## **Object Detection**

### **Pedestrians and Vehicles Model**

1. **Inference on Images:**
    - Upload images for inference using the **`Pedestrians-Vehicles`** model.
    - Results will be displayed, and images saved with bounding boxes.
2. **Inference on Videos:**
    - Upload videos for inference using the **`Pedestrians-Vehicles`** model.
    - Processed videos will be saved with bounding boxes.

### **Traffic Signs Model**

1. **Inference on Images:**
    - Upload images for inference using the **`Traffic Signs`** model.
    - Results will be displayed, and images saved with bounding boxes.
2. **Inference on Videos:**
    - Upload videos for inference using the **`Traffic Signs`** model.
    - Processed videos will be saved with bounding boxes.

## **Lane Detection**

1. **Lane Detection on Images:**
    - Upload images for lane detection.
    - Processed images will be saved with highlighted lane regions.
2. **Lane Detection on Videos:**
    - Upload videos for lane detection.
    - Processed videos will be saved with highlighted lane regions.

## **Result Statistics**

- Model result statistics, such as precision, recall, and F1 score, are given in the zipped folders accompanying this documentation.
- Users are encouraged to analyze model performance based on their specific use case and dataset.

## **Downloading Results**

- After processing images or videos, results can be downloaded from the Colab "Files" section.
- Results include processed videos and images.

## **Colab Notebook Link (Limited Period Support)**

- https://colab.research.google.com/drive/162MQbm5ZvcGGc-qMltoKcBQFaqR8LDfd?usp=sharing
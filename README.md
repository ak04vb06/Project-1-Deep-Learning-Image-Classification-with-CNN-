# Animal Image Classification (CNN)

This repository contains the work of **Group 2** on developing an image classifier using Convolutional Neural Networks (CNNs). The project compares custom implementations, optimized models, and *Transfer Learning* techniques.

<img src="/Users/ia_dev/Desktop/Project Folder/Project 1 (G2) Deep Learning-Image Classification with CNN/png/output.png" alt="Project Banner" width="600">

##  Objective & Data

The goal is to correctly classify images into **10 distinct categories** (Animals-10 dataset with Italian labels: *cane, ragno, gallina, cavallo...*).

* **Strategy:** Each notebook is self-contained and includes its own **Exploratory Data Analysis (EDA)** and preprocessing phase at the beginning.
* **Approach:** We aim to surpass the limitations of basic models by implementing deeper architectures and Transfer Learning.

## 🏆 Results Analysis

After extensive experimentation, **Model 7** proved to be the final solution.

| Notebook | Description | Status |
| :--- | :--- | :--- |
| `Model_1` - `Model_5` | **Initial Iterations** <br> Tests with different variables and simple architectures. Low accuracy results. | Discarded |
| `Model_6` | **Optimized Model** <br> Significant improvement over base models through hyperparameter tuning. | Good |
| `Model_7` | **Transfer Learning (ResNet50)** <br> 🚨 **FINAL & BEST MODEL** 🚨 <br> This notebook contains the **entire Evaluation phase**
| `Model_1(w:py.torch)` | **PyTorch Comparison** <br> Alternative implementation of the base model using PyTorch libraries to contrast results. | Extra |

> **⚠️ IMPORTANT: Deployment & Evaluation**
> All detailed evaluation metrics, confusion matrices, and the **Gradio Deployment demo** are exclusively located in **`Model_7.ipynb`**.

> **Demo / Deployment:** The deployment logic and interactive demo are integrated at the end of the **`Model_7.ipynb`** notebook.
>
> ![Gradio Demo](http://127.0.0.1:7860)

## ⚙️ Installation

Python 3.8+ is required along with the dependencies listed in `requirements.txt`.

```bash
# Virtual Environment Setup
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

------------------------------------------------------------------------------------------
PyTorch Image Classification Suite (Personal Contribution)
This section details the development of three distinct image classification models built using the PyTorch framework. The goal was to demonstrate the evolution from a simple custom architecture to a high-performance system.

Model 1: Preliminary CNN

Architecture: A lightweight Convolutional Neural Network built from scratch.

Focus: Initial testing of data loading pipelines and basic feature extraction.

Results: Provided a baseline for the project, identifying the core challenges of the dataset.


Model 2: Optimized Custom Architecture

Architecture: Deepened CNN with added regularization layers.

Improvements: Integration of Dropout and Batch Normalization to stabilize training and reduce overfitting.

Results: Showed a significant increase in validation accuracy (~85%), proving the effectiveness of architectural tuning.


Model 3: ResNet50 Transfer Learning (Final Expert Model)

Architecture: State-of-the-art ResNet50 leveraging pre-trained ImageNet weights.

Technical Detail: Implemented Residual Learning (skip connections) to allow deep feature extraction across 50 layers.

Performance: Achieved an expert-level accuracy of 98%. This model was selected for final external testing on real-world images and deployment.

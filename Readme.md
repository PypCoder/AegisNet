# 🛡️ Aegis Net — Cyber Threat Detection System

![Aegis Net — Cyber Threat Detection System](Aegis-Net.png)

Aegis Net is a machine-learning–based cyber threat detection system designed to analyze network flow data and classify traffic as **Safe** or **Attack**.  
The project focuses on **clarity, explainability, and practical deployment** using a Streamlit-based web interface.

## 1. Project Overview

Modern networks generate massive amounts of traffic, making manual threat detection impossible.  
Aegis Net addresses this problem by using a trained **Random Forest classifier** to automatically identify malicious network flows based on statistical traffic features.

The system allows users to:
- Upload network flow data
- Manually enter feature values
- Generate synthetic flows for testing
- View predictions and model explanations interactively

## 2. Dataset & Features

The model is trained using network flow data derived from the **CIC-IDS 2017 dataset**, a widely used benchmark in intrusion detection research.

Each prediction is based on the following flow-level features:

- Flow Duration  
- Total Forward Packets  
- Total Backward Packets  
- Total Length of Forward Packets  
- Total Length of Backward Packets  
- Flow Bytes per Second  
- Flow Packets per Second  
- Packet Length Mean  
- Packet Length Variance  
- Initial Window Bytes (Forward)  
- Initial Window Bytes (Backward)

All input data is validated and preprocessed before prediction.

Dataset Link: https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

## 3. System Architecture

The project is structured in a modular and maintainable way:

aegis-net/  
├─ app.py # Main Streamlit application  
├─ models/  
    ├─ an_rf_model.joblib  
    ├─ an_rf_scaler.joblib  
    └─ predictor.py # Loads trained model and runs predictions  
├─ input_handler.py # Handles CSV, manual, and random input  
├─ display.py # Formats and presents results  
├─ visuals.py # Graphs and visual components  
├─ utils/  
    └─ formatter.py # Feature importance formatting  
├─ requirements.txt  
├─ README.md  
└─ .gitignore  

This separation ensures the UI, model logic, and visualization components remain independent.

## 4. Application Workflow

1. User selects an input method (CSV upload, manual entry, or random generation)
2. Data is validated and formatted
3. Pre-trained model performs classification
4. Results are displayed with:
   - Prediction label (Safe / Attack)
   - Attack probability score
   - Top contributing features
5. Users can download prediction results as a CSV file

## 5. Results & Explainability

To improve transparency and trust, Aegis Net provides:

- **Probability-based predictions** instead of binary outputs
- **Feature importance rankings** showing which attributes influenced decisions
- **Visual summaries** of model behavior
- Clear differentiation between single-flow and batch predictions

This makes the system suitable for both learning and demonstration purposes.

![Aegis Net — Cyber Threat Detection System](recall_report.PNG)

## 6. Installation & Usage

### Requirements
- Python 3.9+
- pip

### Setup
```bash
git clone https://github.com/PypCoder/AegisNet.git
cd AegisNet
pip install -r requirements.txt
```
After installation:

```python
streamlit run app.py
```

Your app will be live at **port: 8501**

![Aegis Net — Cyber Threat Detection System](Aegis-Net(1).png)  
![Aegis Net — Cyber Threat Detection System](Aegis-Net(2).png)

## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


<p align="center">
  <a href="https://github.com/PypCoder" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-PypCoder-181717?style=for-the-badge&logo=github&logoColor=white" alt="PypCoder GitHub"/>
  </a>
</p>
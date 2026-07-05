# ☀️ Solar Operations Console

### Physics-Aware Solar Flare Decision Support Prototype

A modular decision support prototype developed for the **ISRO Bharatiya Antariksha Hackathon (BAH)**.

The system integrates complementary **SoLEXS (Soft X-ray Solar Spectrometer)** and **HEL1OS (Hard X-ray Spectrometer)** observations to characterize current solar activity, estimate operational readiness, and generate an explainable short-term operational outlook.

Rather than functioning as a black-box prediction model, the prototype provides transparent, evidence-based assessments to assist scientific interpretation and operational decision-making.

---

# Problem Statement

Solar flares can significantly affect satellites, communication systems, navigation services, and space missions.

Although large volumes of solar observations are continuously collected, converting these observations into actionable operational information remains a challenge.

This prototype demonstrates a structured workflow that transforms complementary solar observations into an explainable operational assessment through validation, activity characterization, readiness estimation, and short-term forecasting.

---

# Solution Overview

The Solar Operations Console performs the following tasks:

- Validates uploaded observation datasets
- Detects current solar activity using thermal and non-thermal trends
- Computes a Solar Readiness Index (SRI)
- Generates an explainable operational assessment
- Produces a short-term operational outlook
- Visualizes observation trends using interactive graphs

---

# Workflow

```text
Observation Dataset
        │
        ▼
Dataset Validation
        │
        ▼
Analysis Configuration
        │
        ▼
Activity Detection
        │
        ▼
Decision Engine
        │
        ├── Solar Readiness Index
        ├── Operational Status
        ├── Operational Outlook
        ▼
Operational Assessment
        │
        ▼
Interactive Visualization
```

---

# Features

- Observation dataset validation
- Configurable analysis thresholds
- Physics-aware activity detection
- Solar Readiness Index (SRI)
- Explainable decision engine
- Operational recommendation generation
- Short-term operational outlook
- Interactive Plotly visualizations
- Modular software architecture

---

# Project Architecture

```text
Solar Operations Console

│

├── app.py
│      Streamlit user interface

├── modules
│
│   ├── validation.py
│   │      Dataset integrity verification
│   │
│   ├── activity.py
│   │      Solar activity classification
│   │
│   ├── decision_engine.py
│   │      Operational assessment engine
│   │
│   ├── sri.py
│   │      Solar Readiness Index calculation
│   │
│   ├── forecast.py
│   │      Short-term operational outlook
│   │
│   ├── status.py
│   │      Observation status generation
│   │
│   └── plots.py
│          Interactive visualization
│
├── sample_data.csv
│
├── requirements.txt
│
└── README.md
```

---

# Module Description

### validation.py

Performs quality checks before analysis by verifying:

- Required columns
- Missing values
- Duplicate timestamps
- Negative observation values
- Overall validation score

---

### activity.py

Analyzes Soft X-ray and Hard X-ray observations to classify current solar activity into:

- QUIET
- BUILD-UP
- PRE-FLARE

---

### decision_engine.py

Generates the final operational assessment by integrating:

- Activity classification
- Assessment confidence
- Solar Readiness Index
- Operational recommendation
- Operational outlook

---

### sri.py

Computes the **Solar Readiness Index (SRI)**, representing the operational preparedness level (0–100) based on current observations.

---

### forecast.py

Produces an explainable short-term operational outlook using complementary thermal and non-thermal observations.

The forecast represents the expected trend during the next observation interval and is not intended as a long-term flare prediction model.

---

### status.py

Generates the operational status associated with the current assessment.

---

### plots.py

Creates interactive Plotly visualizations for:

- Thermal Observation (SoLEXS)
- Non-Thermal Observation (HEL1OS)

---

# Input Dataset

The application accepts CSV files containing synchronized observations.

| Column | Description |
|----------|-------------|
| Time | Observation timestamp |
| Soft_Xray | Soft X-ray flux |
| Hard_Xray | Hard X-ray flux |

Example

| Time | Soft_Xray | Hard_Xray |
|------|-----------|-----------|
|10:00|0.20|0.03|
|10:01|0.22|0.04|
|10:02|0.25|0.04|

---

# Technology Stack

- Python 3.12
- Streamlit
- Pandas
- Plotly
- Git
- GitHub
- VS Code

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
```

Navigate to the project

```bash
cd your-repository
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Future Enhancements

- Integration with real-time Aditya-L1 observations
- Dynamic threshold adaptation
- Physics-informed machine learning models
- Multi-instrument data fusion
- Automated operational alert generation
- Advanced visualization dashboard

---

# Disclaimer

This software is an engineering prototype developed for the **ISRO Bharatiya Antariksha Hackathon (BAH)**.

The generated assessments and forecasts are intended solely for demonstration and educational purposes and should not be interpreted as official space weather predictions.

---

# Team CIRCUIT SOLVERS
Krishnaswamy K V
Sridaya T M
Manoranjan
Monishwar B

Developed for the **ISRO Bharatiya Antariksha Hackathon (BAH)**.
<img width="995" height="620" alt="image" src="https://github.com/user-attachments/assets/13bb8d7e-659e-4cf2-a11b-32874e18bdf5" />
<img width="989" height="526" alt="image" src="https://github.com/user-attachments/assets/798870e0-8faf-4632-b553-8e8869e7d726" />
<img width="994" height="479" alt="image" src="https://github.com/user-attachments/assets/13db61ba-c6bd-4c33-be25-d371c2a34c45" />
<img width="1019" height="472" alt="image" src="https://github.com/user-attachments/assets/372e974b-f44a-4614-9cd5-8f20ab704959" />

# Intrusion Detection System (IDS)

This repository contains the source code and resources for an **Intrusion Detection System (IDS)**, developed as part of a college project in the Network and Security specialization.

## Project Overview
The Intrusion Detection System is designed to detect and mitigate malicious traffic targeting web applications. It utilizes machine learning models to classify requests and prevent security threats effectively. The IDS integrates with the web application layer to provide real-time intrusion prevention.

## Features
- **Machine Learning-Based Detection:** Utilizes trained models for classifying web traffic.
- **Customizable Firewall Rules:** Enhance security by defining additional rules.
- **Real-Time Monitoring:** Live tracking of incoming and outgoing traffic.
- **Scalability:** Can handle increased traffic loads efficiently.
- **Python-Powered Implementation:** Developed using Python libraries and frameworks for ease of use and extensibility.

## Files in the Repository

### Python Scripts
- **`my_web_appp.py`:** Main script for the web application, integrating IDS functionality.
- **`idss.py`:** Core Intrusion Detection System logic.
- **`scappy.py`:** Script for handling packet sniffing and network traffic analysis.
- **`wabapplicationn.py`:** Script managing web application functionality alongside WAF.

### Model Files
- **`trained_model.joblib`:** Machine learning model trained to classify traffic as safe or malicious.
- **`vectorizer.joblib`:** Vectorizer used to process input data for the machine learning model.

## Getting Started

### Prerequisites
- Python 3.8+
- Required libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ids-project.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ids-project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Start the web application:
   ```bash
   python my_web_appp.py
   ```
2. Access the web application in your browser at `http://localhost:5000`.
3. The IDS will automatically monitor traffic and alert/block malicious activity.

## Project Structure
```plaintext
ids-project/
├── my_web_appp.py         # Web application script
├── idss.py                # IDS logic
├── scappy.py              # Packet sniffing and traffic analysis
├── wabapplicationn.py     # WAF and application integration
├── trained_model.joblib   # Machine learning model
├── vectorizer.joblib      # Vectorizer for ML model
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Technologies Used
- **Programming Language:** Python
- **Machine Learning:** scikit-learn, joblib
- **Web Framework:** Flask
- **Networking Library:** scapy


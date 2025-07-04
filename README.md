
# 🧠 Disease Prediction & Handwritten Prescription OCR Web App

This web application allows users to:
- Predict a possible disease based on entered symptoms.
- Upload handwritten prescriptions to extract medication details using OCR (Optical Character Recognition).

---

## 📌 Features

### 🔍 Disease Prediction
- Users can enter symptoms such as `fever, cough, headache` into a text box.
- Upon clicking the **Predict** button, the system suggests a probable disease using a trained machine learning model.

### 📷 OCR-based Prescription Analysis
- Users can upload a scanned or photographed handwritten prescription.
- The system extracts readable medical content (like medication names and dosage) using OCR.
- This helps digitize and interpret handwritten doctor notes.

---

## 🛠️ Tech Stack

| Layer           | Tools Used                                           |
|----------------|------------------------------------------------------|
| Frontend       | HTML, CSS, JavaScript                                |
| Backend        | Python (Flask Framework)                             |
| ML Model       | Trained classifier (RandomForest, DecisionTree, etc.) on symptoms |
| OCR Tool       | Tesseract OCR (`pytesseract`)                        |
| Deployment     | Localhost or web server (e.g., Heroku, Render)       |

---

## 📂 Project Structure

```
disease_prediction_ocr/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── model/
│   └── disease_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How it Works

### 1. Disease Prediction Flow
- User enters symptoms like: `itching, vomiting, fatigue`.
- The input is preprocessed and passed to the trained ML model.
- Output: Predicted disease (e.g., **Jaundice**).

### 2. Handwritten Prescription OCR Flow
- User uploads a handwritten prescription image.
- The app uses `pytesseract` to extract text from the image.
- Output: Extracted medical instructions (e.g., `paracetamol 500mg, twice a day`).

---

## ▶️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/disease-prediction-ocr.git
cd disease-prediction-ocr
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure **Tesseract-OCR** is installed and added to system PATH:  
🔗 [Install Instructions](https://github.com/tesseract-ocr/tesseract)

### 3. Run the App

```bash
python app.py
```

Navigate to `http://localhost:5000` in your browser.

---

## 📦 Requirements

```
Flask
pytesseract
Pillow
scikit-learn
numpy
pandas
joblib
```

---

## 💡 Future Improvements

- Add multilingual OCR support.
- Connect to drug databases for medicine explanation or alternatives.
- Enable PDF export for extracted prescriptions.
- Add user authentication for saved medical history.

---

## 📸 Demo Screenshots

 Home Page                             

 ![image](https://github.com/user-attachments/assets/287b21bf-245e-4c06-bc9e-3dab480912d7)    
 
 
  Disease Prediction Result            
 
 ![image](https://github.com/user-attachments/assets/77994e52-b0eb-4fdd-a0ce-038c8d160f01)  


   OCR Extraction Result               
 
![image](https://github.com/user-attachments/assets/d1c77a7f-3915-41d8-9dbc-6228b39fe288)




## 👨‍⚕️ Author

**Saranragav K**  
Open for collaboration on healthcare + AI projects.



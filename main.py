from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
from PIL import Image
import pytesseract
import io
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


# ---------- FastAPI App Initialization ----------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Load and Train Model ----------
df_train = pd.read_csv("C:\\Users\\saran\\Downloads\\Disease_Prediction_System-master\\Disease_Prediction_System-master\\Data\\Training.csv")

def symptoms_to_string(row):
    return ' '.join([col for col in df_train.columns[:-1] if row[col] == 1])

df_train['symptoms'] = df_train.apply(symptoms_to_string, axis=1)
X_train = df_train['symptoms']
y_train = df_train['prognosis']

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

model = SVC(kernel='linear')
model.fit(X_train_vec, y_train)

# ---------- Endpoint: Predict from Text ----------
class SymptomInput(BaseModel):
    symptoms: str

@app.post("/predict")
async def predict(symptom_input: SymptomInput):
    vec = vectorizer.transform([symptom_input.symptoms])
    prediction = model.predict(vec)[0]
    return {"prediction": prediction}

# ---------- Endpoint: OCR + Predict ----------
@app.post("/ocr-predict")
async def ocr_predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Extract text using pytesseract
    extracted_text = pytesseract.image_to_string(image)

    # Clean and process OCR result (remove newlines etc.)
    symptoms_input = extracted_text.replace('\n', ' ').strip()
    vec = vectorizer.transform([symptoms_input])
    prediction = model.predict(vec)[0]

    return {
        "extracted_text": symptoms_input,
        "prediction": prediction
    }

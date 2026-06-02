from fastapi import FastAPI

app= FastAPI()
@app.get("/")
def home():
  return {"status":"success","message": "My First ML service is running!"}
@app.post("/predict")
def predict(data:dict):
  return {"prediction":Model received your data successfully!"}

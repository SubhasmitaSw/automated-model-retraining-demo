from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# columns for breast cancer dataset
columns = ['mean radius', 'mean texture', 'mean perimeter', 'mean area', 'mean smoothness', 'mean compactness', 'mean concavity', 'mean concave points', 'mean symmetry', 'mean fractal dimension', 'radius error', 'texture error', 'perimeter error', 'area error', 'smoothness error', 'compactness error', 'concavity error', 'concave points error', 'symmetry error', 'fractal dimension error', 'worst radius', 'worst texture', 'worst perimeter', 'worst area', 'worst smoothness', 'worst compactness', 'worst concavity', 'worst concave points', 'worst symmetry', 'worst fractal dimension']

# dict_res for breast cancer dataset
dict_res = {0: 'Benign', 1: 'Malignant'}

pipeline_path = 'model/pipeline.pkl'
with open(pipeline_path, 'rb') as pipeline_file:
    pipeline = pickle.load(pipeline_file)

class DataInput(BaseModel):
    data: list

@app.post("/predict")
async def predict(input_data: DataInput):
    try:
        df = pd.DataFrame(input_data.data, columns=columns)
        predictions = pipeline.predict(df)
        results = [dict_res[pred] for pred in predictions]
    
        return {"predictions": results}
    
    except Exception as e:
        print("Error:", str(e))
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
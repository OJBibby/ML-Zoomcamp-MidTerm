import bentoml
from typing import Literal
from bentoml.io import JSON
from pydantic import BaseModel

class MedicalInfo(BaseModel):
	age: int
	sex: Literal['female', 'male']
	bmi: float
	children: int
	smoker: Literal['yes', 'no']
	region: Literal['northwest', 'northeast', 'southwest', 'southeast']

model_ref = bentoml.xgboost.get("medical_cost_model:latest")
dv = model_ref.custom_objects['dictVectorizer']

model_runner = model_ref.to_runner()

svc = bentoml.Service("medical_cost_regressor", runners=[model_runner])

@svc.api(input=JSON(pydantic_model=MedicalInfo), output=JSON())
def classify(medical_info):
	medical_data = medical_info.dict()
	vector = dv.transform(medical_data)
	prediction = model_runner.predict.run(vector)
	return prediction
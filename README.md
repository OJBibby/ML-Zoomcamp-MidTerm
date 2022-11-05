dataset from: https://www.kaggle.com/datasets/mirichoi0218/insurance

It is important for insurers to accurately predict the medical costs of a customer to determine their premium.
This model predicts medical costs of customers based on where they live, sex, age, bmi, and whether or not they smoke.

To build the model run
	python train.py

To start the service type
	bentoml serve service.py:svc

To containerize type
	bentoml build
	bentoml containerize medical_cost_regressor:latest
To then run through docker type
	docker run -it --rm -p 3000:3000 "image id" serve --production
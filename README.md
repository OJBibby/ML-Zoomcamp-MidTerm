Dataset is included in the repository as insurance.csv.
dataset from: https://www.kaggle.com/datasets/mirichoi0218/insurance

It is important for insurers to accurately predict the medical costs of a customer to determine their premium.
This model predicts medical costs of customers based on where they live, sex, age, bmi, number of children, and whether or not they smoke.

Input data must be in the form of:

{
	"age": Int,
	"sex": String ("female" || "male"),
	"bmi": Float,
	"children": Int,
	"smoker": String ("yes" || "no"),
	"region": String ("northwest" || "southwest" || "northeast" || "southeast")
}

(This is checked with pydantic)

Creating the model service:

Enter pipenv by typing:

	pipenv install
	pipenv shell

To build the model run:

	python train.py

To start the service type:

	bentoml serve service.py:svc

Alternatively to pipenv, run through docker by typing (might take some time):

	docker build -t medical-cost .
	docker run -p 3000:3000 -it --rm medical-cost

To containerize via bentoml type (make sure docker is running):

	bentoml build

	bentoml containerize medical_cost_regressor:latest

To then run through docker type (replace "image id" with id generated in last step):

	docker run -it --rm -p 3000:3000 "image id" serve --production

Images from successful hosting on the AWS elastic beanstalk cloud are in the folder "cloud_pics"

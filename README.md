Dataset is included in the repository as insurance.csv.  
Dataset from: https://www.kaggle.com/datasets/mirichoi0218/insurance.  
Dataset contains information on medical costs and factors that may contribute to medical costs.

It is important for insurers to accurately predict the likely medical costs of a customer.  
This allows an insurer to set the premium for each customer in a way that allows the insurer to operate as a business (and make money!).  
This model predicts medical costs of customers based on where they live, sex, age, bmi, number of children, and whether or not they smoke.  
These predictions could be used to set the price of a customer's insurance plan.

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

Model will be running on localhost:3000

To containerize via bentoml type (make sure docker is running):

	bentoml build

	bentoml containerize medical_cost_regressor:latest

To then run through docker type (replace "image id" with id generated in last step):

	docker run -it --rm -p 3000:3000 "image id" serve --production

Alternatively to pipenv, run through docker using my Dockerfile by typing (might take some time):

	docker build -t medical-cost .
	docker run -p 3000:3000 -it --rm medical-cost

Images from successful hosting on the AWS elastic beanstalk cloud are in the folder "cloud_pics".  
cloud_prep.txt shows the commands that were used to set the model up on the cloud.

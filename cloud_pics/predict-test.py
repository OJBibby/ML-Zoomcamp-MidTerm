#!/usr/bin/env python
# coding: utf-8

import requests

host = 'medical-cost-env.eba-ghjpan9t.eu-west-1.elasticbeanstalk.com'
url = f'http://{host}/classify'

medical_info = {
	"age": 19,
 	"sex": "female",
	"bmi": 27.9,
 	"children": 0,
 	"smoker": "yes",
 	"region": "southwest"
}

response = requests.post(url, json=medical_info)
print(response.text)

# This is the code that was used to send the case to the server and get the return shown in successful_response.png
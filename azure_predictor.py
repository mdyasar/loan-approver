import urllib.request
import json
import os

def call_endpoint(features):
    # Request data goes here
    data = {
        "Inputs": {
            "WebServiceInput0":
            [
                {
                    'Loan_ID': "LP100102",
                    'Gender': "0",
                    'Married': f"{features[2]}",
                    'Dependents': "0",
                    'Education': "Graduate",
                    'Self_Employed': "0",
                    'ApplicantIncome': "6000",
                    'CoapplicantIncome': "0",
                    'LoanAmount': f"{features[0]}",
                    'Loan_Amount_Term': f"{features[1]}",
                    'Credit_History': f"{features[3]}",
                    'Property_Area': "Urban",
                },
            ],
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = os.environ['END_POINT']

    api_key = os.environ['KEY']

    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers)

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        res= str(result).split("[")[1].split(",")[1].split(":")[1].strip()
        return res

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
import pickle
import flask

from flask import Flask, request, Response, jsonify

## loading the model
model_pickle = open("classifier.pkl", 'rb')
clf = pickle.load(model_pickle)

app = Flask(__name__)


# defining the function which will make the prediction using the data which the user inputs
@app.route('/predict', methods = ['POST'])
def predict():
    # Pre-processing user input
    loan_req = request.get_json()
    print(loan_req)

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000

    # Making predictions
    prediction = clf.predict(
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    result = {
        'loan_approval_status': pred
    }

    return jsonify(result)


@app.route("/")
def hello_world():
    return "<p>Hello, Deepak!</p>"

@app.route("/ping", methods=['GET'])
def ping():
    return "<p>Hey man! why are you pinging me</p>"

@app.route("/aboutus", methods=['GET'])
def aboutus():
    return "<p>We are Mlops learners</p>"
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
filename = 'telecom.pkl'
model = pickle.load(open(filename,'rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    if request.method == 'POST':
        seniorcitizen = int(request.form['SeniorCitizen'])
        tenure = float(request.form['tenure'])
        monthly = float(request.form['MonthlyCharges'])
        total = float(request.form['TotalCharges'])
        

        gender = request.form['gender_Male']
        if (gender == 'MALE'):
            gender = 1
        else:
            gender = 0

        partner = request.form['Partner']
        if (partner == 'YES'):
            partner = 1
        else:
            partner = 0

        dependent = request.form['Dependents']
        if (dependent == 'Yes'):
            dependent = 1
        else:
            dependent = 0


        phoneservices = request.form['PhoneService']
        if (phoneservices == 'Yes'):
            phoneservices = 1
        else:
            phoneservices = 0

        multiplelines = request.form['MultipleLines']
        if (multiplelines == 'Yes'):
            multiplelines = 1
        else:
            multiplelines = 0

        internetser_fo = request.form.get('InternetService_Fiberoptic')
        internetser_no = request.form.get('InternetService_No')
        if (internetser_fo == 'Fiberoptics'):
            internetser_fo = 1
            internetser_no = 0
        elif (internetser_no == 'No Service'):
            internetser_fo = 0
            internetser_no = 1
        else:
            internetser_fo = 0
            internetser_no = 0

        onlinesecur = request.form['OnlineSecurity']
        if (onlinesecur == 'Yes'):
            onlinesecur = 1
        else:
            onlinesecur = 0

        onlinebackup = request.form['OnlineBackup']
        if (onlinebackup == 'Yes'):
            onlinebackup = 1
        else:
            onlinebackup = 0

        deviceprotection = request.form['DeviceProtection']
        if (deviceprotection == 'Yes'):
            deviceprotection = 1
        else:
            deviceprotection = 0

        techsupport = request.form['TechSupport']
        if (techsupport == 'Yes'):
            techsupport = 1
        else:
            techsupport = 0

        streamingtv = request.form['StreamingTV']
        if (streamingtv == 'Yes'):
            streamingtv = 1
        else:
            streamingtv = 0

        streamingmovies = request.form['StreamingMovies']
        if (streamingmovies == 'Yes'):
            streamingmovies = 1
        else:
            streamingmovies = 0

        contract_one = request.form.get('Contract_One year')
        contract_two = request.form.get('Contract_Two year')
        if (contract_one == 'One Year'):
            contract_one = 1
            contract_two = 0
        elif (contract_two == 'Two Year'):
            contract_one = 0
            contract_two = 1
        else:
            contract_one = 0
            contract_two = 0
            
        paperless = request.form['PaperlessBilling']
        if (paperless == 'Yes'):
            paperless = 1
        else:
            paperless = 0

        paymentmethod_credit = request.form.get('PaymentMethod_CreditCard')
        paymentmethod_electronic = request.form.get('PaymentMethod_ElectronicCheck')
        paymentmethod_email = request.form.get('PaymentMethod_MailedCheck')
        if (paymentmethod_credit == 'Creditcard'):
            paymentmethod_credit = 1
            paymentmethod_electronic = 0
            paymentmethod_email = 0
        elif (paymentmethod_electronic == 'Electronic'):
            paymentmethod_credit = 0
            paymentmethod_electronic = 1
            paymentmethod_email = 0
        elif (paymentmethod_email == 'Email'):
            paymentmethod_credit = 0
            paymentmethod_electronic = 0
            paymentmethod_email = 1
        else:
            paymentmethod_credit = 0
            paymentmethod_electronic = 0
            paymentmethod_email = 0

        prediction = model.predict([[tenure,monthly,total,seniorcitizen,
                                    gender,partner,dependent,phoneservices,
                                    multiplelines,internetser_fo,internetser_no,
                                    onlinesecur,onlinebackup,deviceprotection,techsupport,
                                    streamingtv,streamingmovies,contract_one,contract_two,
                                    paperless,paymentmethod_credit,paymentmethod_electronic,
                                    paymentmethod_email]])
        output = int(prediction)
        
        if output == 0:
            return render_template('index.html',prediction_texts='The customer will likely to be active.')
        elif output == 1:
            return render_template('index.html',prediction_texts='The customer will likely to be churn.')
    else: 
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)       

        

        

        

        
            
        


        



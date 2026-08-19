from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# सेव किया हुआ मॉडल लोड करना
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # यूजर का इनपुट लेना
        exp = float(request.form['experience'])
        input_data = np.array([[exp]])
        
        # प्रेडिक्शन करना
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)
        
        return render_template('index.html', prediction_text=f'Estimated Salary: ${output}k')
    except Exception as e:
        return render_template('index.html', prediction_text='Kripya sahi number dalein!')

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask,request, render_template
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app=Flask(__name__)


@app.route('/submit',methods=['POST'])
def userInput():
    data = request.form.to_dict(flat=False)
    prediction=model.predict([[1,75,75,80,1,1,0,0,1,0,1,1,1,1,0,1]])
    print(prediction)
    return {"predicted_val":int(prediction[0])}

if __name__=="__main__":
    app.run(debug=True)
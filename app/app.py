from flask import Flask,request, render_template,json
import pickle

import numpy as np

model = pickle.load(open('model.pkl','rb'))

app=Flask(__name__)


@app.route('/',methods=['POST'])
def userInput():
    data = request.form.to_dict(flat=False)  
    gender=int(data["gender"][0])
    marks10th=int(data["10thMarks"][0])
    marks12th=int(data["12thMarks"][0])
    degreeMarks=int(data["degreeMarks"][0])
    workExp=int(data["workExp"][0])
    specialisation=int(data["specialisation"][0])

    X_test=[gender,marks10th,marks12th,degreeMarks,workExp,specialisation]

    subject12th=data["12thSubject"][0]
    if subject12th=="Science":
        X_test+=[0,0,1]
    elif subject12th=="Arts":
        X_test+=[1,0,0]
    else:
        X_test+=[0,1,0]

    degreeType=data["degreeType"][0]
    if degreeType=="Sci&Tech":
        X_test+=[0,0,1]
    elif degreeType=="Comm&Mgmt":
        X_test+=[1,0,0]
    else:
        X_test+=[0,1,0]

    board12th=data["12thBoard"][0]
    if board12th=="Central":
        X_test+=[1,0]
    else:
        X_test+=[0,1]

    board10th=data["10thBoard"]
    if board10th=="Central":
        X_test+=[1,0]
    else:
        X_test+=[0,1]
    prediction=model.predict([X_test])
    
    if prediction[0]==1:
        return render_template('placed.html') 
    else:
        return render_template('notplaced.html')  


    


@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
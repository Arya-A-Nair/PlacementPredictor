from flask import Flask,request, render_template



app=Flask(__name__)


@app.route('/submit',methods=['POST'])
def userInput():
    data = request.form.to_dict(flat=False)
    return data

if __name__=="__main__":
    app.run(debug=True)
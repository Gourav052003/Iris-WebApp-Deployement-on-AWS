from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open('iris_model.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict_placement():
    sepal_length = float(request.form.get('sepal length'))
    sepal_width = float(request.form.get('sepal width'))
    petal_length = float(request.form.get('petal length'))
    petal_width = float(request.form.get('petal width'))

    # prediction
    result = model.predict(np.array([sepal_length,sepal_width,petal_length,petal_width]).reshape(1,4))
    print(result)

    return render_template('index.html',result=result)


# if __name__ == '__main__':
#     app.run(host = '0.0.0.0',port = 8080)
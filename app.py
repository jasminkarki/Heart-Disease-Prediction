from flask import Flask, jsonify, request, render_template
from Flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


diseases=[
    {
        'name':'Diabetes',
        'serious':'mild',
        'medicine':
        [
            {
                'name':'Healthixon',
                'dose':'5 mg'
            },
            {
                'name': 'Sugar Free Biscuit',
                'dose': '50 mg'
            }
        ]
    },
    {
        'name': 'Common Cold',
        'serious': 'low',
        'medicine':
        [
            {
                'name':'De-cold',
                'dose':'20 mg'
            },
            {
                'name': 'Flexon',
                'dose':'2.5 mg'
            }
        ]
    }
]

@app.route('/')           ## http://www.google.com/  here / at the end is Home page
def home():
    return render_template('index.html')
 
## POST /disease POST method
@app.route('/disease', methods=['POST'])
def add_disease():
    request_data=request.get_json()
    new_disease={
        'name':request_data['name'],
        'serious':request_data['serious'],
        'medicine':[]
    }
    diseases.append(new_disease)
    return jsonify(new_disease)

## GET /disease/<string:name> 
@app.route('/disease/<string:name>')
def get_disease(name):
    for dis in diseases:
        if dis['name']==name:
            return jsonify(dis)
    return jsonify({'message':'Disease not found'})

## GET 
@app.route('/disease_list')
def get_disease_list():
    return jsonify({'disease':diseases})


@app.route('/predict', methods=['POST', 'GET'])
def predict_disease():
    pass

## GET medicine for a disease '/disease/<string:name>/item'
@app.route('/disease/<string:name>/item')
def get_medicine(name):
    for dis in diseases:
        if dis['name']==name:
            return jsonify({'medicine':dis['medicine']}) 
    return jsonify({'message':'Disease not found'})

@app.route('/disease/<string:name>/item', methods=['POST'])
def add_medicine(name):
    request_medicine = request.get_json()

    for dis in diseases:
        if dis['name'] == name:
            new_medicine= {
                'name':request_medicine['name'],
                'dose':request_medicine['dose']
            }
            dis['medicine'].append(new_medicine)
            return jsonify(new_medicine)
    return jsonify({'message':'Disease not found'})

app.run(port=5000)    ## Port can be used by other app. In that case change it.

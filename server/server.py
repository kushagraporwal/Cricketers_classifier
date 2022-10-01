from flask import Flask,request,jsonify, render_template
import util

app = Flask(__name__)


@app.route('/')
def on():
    return 'server'

@app.route('/classify_image',methods=['GET','POST'])
def classify_image():
    image_data = request.form['image_data']

    response=jsonify(util.classify_image(image_data))
    # response.header.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__=='__main__':
    print("Staring Python Flask Server For Sports Celebrity Image Classification ")
    util.load_saved_artifacts()
    app.run(port=5000,debug=True)
from flask import Flask,request,jsonify
import tensorflow as tf
#a=tf.__version__
app=Flask(__name__)
a=tf.__version__
a=str(a)
@app.route('/')
def home():
    return a




if __name__=="__main__":
    app.run()

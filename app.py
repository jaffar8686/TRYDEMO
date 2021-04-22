from flask import Flask,request,jsonify
import tensorflow
#a=tf.__version__
app=Flask(__name__)

model = tensorflow.keras.models.load_model('keras_model.h5')
print("model loaded")
#a=tf.__version__
#a=str(a)
@app.route('/')
def home():
    return "model loaded"




if __name__=="__main__":
    app.run()

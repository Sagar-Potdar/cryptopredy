from flask import Flask, render_template,redirect,url_for,request
import os
import cv2
import numpy as np
import base64


app = Flask(__name__)

@app.route('/' , methods =["GET", "POST"])
def index():
    dir_list = os.listdir('crypto_result')
    print(dir_list)
    return render_template('index.html', data = dir_list)

@app.route('/result' , methods =["GET", "POST"])
def result():
    if request.method == "POST":
        crypto_name = request.form.get("crypto_name")
        image1 = cv2.imread('crypto_result/'+ crypto_name+'/fig1.png')
        image2 = cv2.imread('crypto_result/'+ crypto_name+'/fig2.png')
        
        
        retval1, buffer1 = cv2.imencode('.png', image1)
        jpg_as_text1 = base64.b64encode(buffer1)
        data1 = str(jpg_as_text1)
        data_image1 = str(jpg_as_text1)


        retval2, buffer2 = cv2.imencode('.png', image2)
        jpg_as_text2 = base64.b64encode(buffer2)
        data2 = str(jpg_as_text2)
        data_image2 = str(jpg_as_text2)
        print()
        print()
        print()
        print(data_image2)
        print()
        print()
        print()
        
        a = np.load("crypto_result/"+ crypto_name+"/Myfile.npz") #make sure you use the .npz!
        b = a['arr_0']
        print(b)
    return render_template('result.html', data1=data_image1[2:-1],data2=data_image2[2:-1],data = b,crypto_name = crypto_name)
if __name__ == '__main__':
    app.run(debug = True)   
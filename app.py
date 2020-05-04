# Import libraries
import numpy as np
from flask import Flask, request
import pickle
from model import model
from flask import render_template


app = Flask(__name__)
# Load the model

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template ('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    # Get the data from the POST request.
    #data = request.get_json(force=True)
    message=""
    seq = request.form.get("sequence")
    a = 0;
    r = 0;
    n = 0;
    d = 0;
    c = 0;
    e = 0;
    q = 0;
    g = 0;
    h = 0;
    i = 0;
    l = 0;
    k = 0;
    m = 0;
    f = 0;
    p = 0;
    s = 0;
    t = 0;
    w = 0;
    y = 0;
    v = 0;
    for aa in seq:
        aa = aa.lower()
        for char in aa:
            if char == "a":
                a += 1
            if char == "r":
                r += 1
            if char == "n":
                n += 1
            if char == "d":
                d += 1
            if char == "c":
                c += 1
            if char == "e":
                e += 1
            if char == "q":
                q += 1
            if char == "g":
                g += 1
            if char == "h":
                h += 1
            if char == "i":
                i += 1
            if char == "l":
                l += 1
            if char == "k":
                k += 1
            if char == "m":
                m += 1
            if char == "f":
                f += 1
            if char == "p":
                p += 1
            if char == "s":
                s += 1
            if char == "t":
                t += 1
            if char == "w":
                w += 1
            if char == "y":
                y += 1
            if char == "v":
                v += 1
    TL = a + r + n + d + c + e + q + g + h + i + l + k + m + f + p + s + t + w + y + v
    values = [a, c, d, e, f, g, h, i, k, l, m, n, p, q, r, s, t, v, w, y]
    amino = []
    import numpy
    for x in values:
        AAC = x / TL
        AAC = round(AAC, 3)
        amino.append(AAC)
    values1 = numpy.array(values)
    tc=values1[0]*0+values1[1]*0+values1[2]*(-1)+values1[3]*(-1)+values1[4]*0+values1[5]*0 +values1[6]*0+values1[7]*0+values1[8]*(+1)+values1[9]*0+values1[10]*0+values1[11]*0+values1[12]*0+values1[13]*0+values1[14]*1+values1[15]*0+values1[16]*0+values1[17]*0+values1[18]*0+values1[19]*0
    amino.insert(13,tc)
    # Make prediction using model loaded from disk as per the data.
    amino1 = [amino, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    prediction = model.predict(amino1)
    output = prediction[0]
    if output==1:
        message = "ASP"
    else:
        message = "non ASP"

    return render_template('index.html',text=message)

""""@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)
"""

if __name__ == '__main__':
    app.run(port=5000, debug=True)

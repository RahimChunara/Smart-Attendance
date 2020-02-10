from flask import *
# from flask import request

app = Flask(__name__)

@app.route('/')  
def upload():  
    return render_template("upload_form.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  


if __name__ == '__main__':
    app.run(debug=True, port=5000)

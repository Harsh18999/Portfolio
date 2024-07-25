from flask import Flask,render_template
app = Flask(__name__)
app.secret_key = 'Secret'
@app.route('/')
def login_page():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0')

from flask import Flask,render_template
app = Flask(__name__)
app.secret_key = 'Secret'

projects = [
    {
        "title": "Shop Management System",
        "description": "A Flask-based web application that efficiently manages inventory, tracks orders, generates and sends bills, and provides detailed insights on revenue, profit, and costs. Designed as a capstone project with Python and MySQL.",
        "image": "Home.png",
        "link": "https://shopmanageroff.vercel.app",
        "category": "backend"
    },

    {
       "title": "Machine Learning Algorithms Animations",
        "description": "A Streamlit-powered tool that visualizes machine learning models training process and decision boundary, helping users understand the behaviour and predictions of the model through interactive graphs and userfriendly interface",
        "image": "ml-animation.png",
        "link": "https://ml-animation.streamlitapp",
        "category": "Machine-learning"
    },

    {
       "title": "Esophegal Cancer Case Study",
        "description": "Esophageal cancer case study, cleaning, and preprocessing to prepare a robust dataset. Leveraging machine learning techniques, developed a predictive model that achieved accuracy of 99.87%, demonstrating significant potential in early detection and diagnosis of esophageal cancer",
        "image": "esophegeal-case-study.png",
        "link": "",
        "category": "data-analytics"
    }
    
]

@app.route('/')
def login_page():
   return render_template('index.html', projects = projects)

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0')

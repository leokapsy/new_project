from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/')
def contact():
    return render_template("contact.html")

@app.route('/project-details')
def project_details():
    return render_template("project-details.html")

@app.route('/services-details')
def services_details():
    return render_template("services.html")





if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template

app = Flask('__name__',template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/articles')
def articles():
    return render_template("articles.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug = True)

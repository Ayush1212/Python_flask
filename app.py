from flask import Flask, render_template
# import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True)

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)

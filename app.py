from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    html = "<h1> hello, world </h1>"
    return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
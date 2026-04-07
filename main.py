from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    # This looks inside the /templates folder automatically
    return render_template("index.html", title="Home Page")
if __name__ == '__main__':
    # Cloud Shell usually uses port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
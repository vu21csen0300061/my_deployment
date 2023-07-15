
from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def marks():
    if request.method == "POST":
        hrs = request.form['hrs']
        marks_pred = m.marks_prediction(hrs)
        #mk = marks_pred
        print(marks_pred)
    return render_template("index.html")

    # Handle GET requests separately
    #return "Hello! Please submit the form."

if __name__ == '__main__':
    app.run(debug=True)

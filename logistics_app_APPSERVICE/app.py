from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])                    # Currently hosted at https://ext-nsa-webapp-stg.azurewebsites.net/
def index():
    result = ""
    if request.method == "POST":
        command = request.form.get("search")
        try:
            result = os.popen(command).read()
        except Exception as e:
            result = str(e)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

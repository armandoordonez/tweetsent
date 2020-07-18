from flask import Flask, render_template, request, redirect
import processing as p


app = Flask(__name__)

@app.route("/")
def inicio():
	return render_template("inicio.html")


@app.route("/results", methods=['POST'])
def about():

    return render_template("results.html", text=request.form['text'])


if __name__ == "__main__":
	app.run(debug=True)
from flask import Flask, render_template, request

from azure_predictor import call_endpoint

app= Flask(__name__)

@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/predict", methods=["POST","GET"])
def pred():
  features= [x for x in request.form.values()]
  res= call_endpoint(features)
  if(res == "true"):
    return render_template("index.html", pred="Approved", c="green-text")
  else:
    return render_template("index.html", pred="Not Approved", c="red-text")

if __name__ == "__main__":
  app.run()
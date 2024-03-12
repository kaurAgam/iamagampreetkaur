from flask import Flask  # creating a class

app = Flask(__name__)  # creating object of class


@app.route("/")  # url route
def hello_world():  # function name
  return "<p>Hello, World!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

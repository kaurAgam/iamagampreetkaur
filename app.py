from flask import Flask, render_template  # creating a class

app = Flask(__name__)  # creating object of class

poems = [
    {
        'id': 1,
        'title': 'Are we Home yet?',
        'description': 'abc',
        'link': 'https://www.poetryfoundation.org/poems/46464/the-raven-5874d'
    },
    {
        'id': 2,
        'title': 'The Raven',
        'description': 'abc',
        'link': 'https://www.poetryfoundation.org/poems/46464/the-raven-5874d'
    },
    {
        'id': 3,
        'title': 'The Raven',
        'description': 'abc',
        'link': 'https://www.poetryfoundation.org/poems/46464/the-raven-5874d'
    },
    {
        'id': 4,
        'title': 'The Raven',
        'description': 'abc',
        'link': 'https://www.poetryfoundation.org/poems/46464/the-raven-5874d'
    },
]


@app.route("/")  # url route
def hello_world():  # function name
  return render_template('home.html', poems=poems)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

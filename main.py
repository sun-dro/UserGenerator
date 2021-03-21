from flask import Flask
import requests

app = Flask(__name__)


def random_user():
    result = requests.get('https://randomuser.me/api/?inc=name,email,picture&noinfo')
    return result.json()


def create_html(people, visual):
    for person in people:
        visual += f"""
        <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Title</title>
            </head>
            <body>
            <h1 class="title"> Random User Generator</h1>
            <div class="user-profile">
	        <img id="avatar" src={person['picture']['large']} class="imagestyle"</div>
            <div id="fullname">{person['name']['first']} {person['name']['last']}</div>
            <div class="description">
            <div>Email: <span id="email">{person['email']}</span></div>
            </div>
            </div>
            </body>
            </html>
            """
    return visual


style_css = """

<html>
        <body style="background-color:B98484">
        <style>
body {
  background: #ecf0f1;
  padding: 2.23em;
}

.title {
  color:030000;
  font-family: "Coda", sans-serif;
  text-align: center;
}
.user-profile {
  margin: auto;
	width: 27em;
  height: 11em;
  background: #fff;
  border-radius: .3em;
}

.user-profile  #fullname {
  margin: auto;
  margin-top: -4.40em;
  margin-left: 5.80em;
  color: #16a085;
  font-size: 1.53em;
  font-family: "Coda", sans-serif;
  font-weight: bold;
}

.user-profile > .description {
  margin: auto;
  margin-top: 1.35em;
  margin-right: 3em;
  width: 18em;
  color: #7f8c8d;
  font-size: .87em;
  font-family: "varela round", sans-serif;
}

.user-profile > img#avatar {
	padding: .7em;
  margin-left: .3em;
  margin-top: .3em;
  height: 6.23em;
  width: 6.23em;
  border-radius: 18em;
}


.footer {
	margin: 2em auto;
	height: 3.70em;
  background: #16a085;
  text-align: center;
  border-radius: 0 0 .3em .3em;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: background 0.1s;
}

.footer:hover {
  background: #1abc9c;
}
        </style>
"""


@app.route('/')
def show_page():
    data = random_user()['results']
    return create_html(data, style_css)


if __name__ == '__main__':
    app.run(debug=True)
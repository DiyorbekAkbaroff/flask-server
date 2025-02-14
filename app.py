import json
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def bosh_sahifa():
    return render_template('index.html')


@app.route('/about')
def about_sahifa():
    return render_template('about.html')


@app.route('/greeting')
def greeting():

    params = request.args
    
    name = params.get('name', '')

    return render_template('greeting.html', name=name)

@app.route('/calc')
def calc():

    params = request.args

    a = int(params.get("a", 0))
    b = int(params.get("b", 0))
    operator = params.get('operator', '-')

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '/':
        result = a / b
    elif operator == '*':
        result = a * b

    return render_template("calc.html", a=a, b=b, result=result)


@app.route("/register", methods=['GET', 'POST'])
def register_view():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        form = request.form
        
        name = form['name']
        username = form['username']
        email = form['email']
        password = form['password']
        
        with open('users.json') as f:
            users: list = json.loads(f.read())

            users.append({
                'name': name,
                'username': username,
                'email': email,
                'password': password
            })

        with open('users.json', 'w') as f:
            f.write(json.dumps(users, indent=4))

        return render_template('register.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)


from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable the stupid cache mechanism


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('form.html')


@app.route('/register', methods=["POST"])
def register():
    display_name = request.form['display-name']
    price = request.form['price']
    description = request.form['description']
    email = request.form['email']
    psw = request.form['psw']
    print(display_name, price, description, email, psw)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

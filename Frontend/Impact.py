from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
# app.secret_key = "supersecretkey"

# ---------------- HOME ----------------
@app.route('/')
def index():
    return render_template('index.html')

# ---------------- ABOUT ----------------
@app.route('/about')
def about():
    return render_template('about.html')

# # ---------------- SIGN UP ----------------
@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')


# ---------------- LOGIN ----------------
@app.route('/login')
def login_page():
    return render_template('login.html')

# ----------------dashboard---------------
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        return redirect(url_for('dashboard'))
    return render_template('login.html')






# ---------------- MAIN ----------------
if __name__ == '__main__':
    app.run(debug=True)

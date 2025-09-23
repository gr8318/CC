from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin123":
            return redirect("/welcome")
        else:
            return "Invalid Credentials! Try again."
    
    return '''
        <form method="post">
            Username: <input type="text" name="username" required><br>
            Password: <input type="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/welcome")
def welcome():
    return "<h2>Welcome! You are successfully logged in.</h2>"

if __name__ == "__main__":
    app.run(debug=True)
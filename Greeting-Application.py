from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greeting():
    if request.method == "POST":
        name = request.form["name"]
        return f"<h2>Hello, {name}! Welcome to Cloud Computing Lab.</h2>"
    
    return '''
        <form method="post">
            Enter your name: <input type="text" name="name" required><br>
            <input type="submit" value="Greet Me">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
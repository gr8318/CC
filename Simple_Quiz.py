from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = None
    if request.method == "POST":
        answer = request.form["q1"]
        score = 1 if answer == "Cloud Computing" else 0
    
    return f'''
        <h2>Simple Quiz</h2>
        <form method="post">
            Q1: Which technology provides on-demand computing resources
            over the internet?<br>
            <input type="radio" name="q1" value="Cloud Computing"> Cloud Computing<br>
            <input type="radio" name="q1" value="Networking"> Networking<br>
            <input type="radio" name="q1" value="OS"> Operating System<br>
            <input type="submit" value="Submit">
        </form>
        {f"<h3>Your Score: {score}/1</h3>" if score is not None else ""}
    '''

if __name__ == "__main__":
    app.run(debug=True)

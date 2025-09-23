from flask import Flask, request

app = Flask(__name__)
feedback_list = []

@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        fb = request.form["feedback"]
        feedback_list.append(fb)
    
    return '''
        <h2>Feedback Form</h2>
        <form method="post">
            Enter Feedback: <input type="text" name="feedback" required><br>
            <input type="submit" value="Submit">
        </form>
        <h3>Previous Feedback:</h3>
    ''' + "<br>".join(feedback_list)

if __name__ == "__main__":
    app.run(debug=True)

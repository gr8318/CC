from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def age_calculator():
    age = None
    if request.method == "POST":
        dob = request.form["dob"]
        dob_date = datetime.strptime(dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - dob_date.year - (
            (today.month, today.day) < (dob_date.month, dob_date.day)
        )
    
    return f'''
        <h2>Age Calculator</h2>
        <form method="post">
            Enter Date of Birth: <input type="date" name="dob" required><br>
            <input type="submit" value="Calculate Age">
        </form>
        {f"<h3>Your Age: {age} years</h3>" if age is not None else ""}
    '''

if __name__ == "__main__":
    app.run(debug=True)
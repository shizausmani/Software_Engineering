import os
from flask import Flask, render_template_string, request

app = Flask(__name__)


# Simple spam detection function
def predict_email(email):

    spam_words = [
        "won", "free", "prize", "claim",
        "bank details", "reward", "urgent",
        "lottery", "winner"
    ]

    for word in spam_words:
        if word in email:
            return "Spam"

    return "Not spam"


# HTML webpage
html = """
<!DOCTYPE html>
<html>

<head>
    <title>Email Spam Classifier</title>

    <style>

        body {
            font-family: Arial;
            background-colour: #f2f2f2;
            text-align: center;
            padding: 50px;
        }

        .container {
            background: white;
            padding: 30px;
            width: 450px;
            margin: auto;
            border-radius: 10px;
        }

        textarea {
            width: 90%;
            height: 120px;
            padding: 10px;
        }

        button {
            background-color: blue;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        h3 {
            color: green;
        }

        .spam {
            color: red;
        }

        .not-spam {
            color: green;
        }

    </style>

</head>

<body>

<div class="container">

    <h1>Email Spam Classifier</h1>

    <form method="POST">

        <textarea
            id="email"
            name="email"
            placeholder="Enter your email here"
            required
        >{{ email }}</textarea>

        <br><br>

        <button type="submit" id="predit">
            Check Email
        </button>

    </form>


    {% if result %}

        {% if result == "Spam" %}

            <h3 class="spam" id="result">
                Prediction: {{ result }}
            </h3>

        {% else %}

            <h3 class="not-spam" id="result">
                Prediction: {{ result }}
            </h3>

        {% endif %}

    {% endif %}

</div>

</body>

</html>
"""


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    email = ""
    count = 0

    if request.method == "POST":

        email = request.form["emial"]

        result = predict_email(email)

    return render_template_string(
        html,
        result=result,
        email=email
    )


# Run application
if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

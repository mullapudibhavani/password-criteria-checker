from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):
    errors = []


    if len(password) < 8:
        errors.append("At least 8 characters")

    if not re.search(r'[A-Z]',password):
        errors.append("At least one uppercase letter")

    if not re.search(r'[a-z]',password):
        errors.append("At least one lowercase letter")

    if not re.search(r'\d',password):
        errors.append("At least one number")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        errors.append("At least one special character")

    return errors
def password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    if score <= 2:
        return "Weak", "red", 33
    elif score <= 4:
        return "Medium", "orange", 66
    else:
        return "Strong", "green", 100

@app.route("/",methods=["GET","POST"])
def index():
    errors = []
    result = None
    strength = None
    color = None
    percentage = 0

    if request.method == "POST":
        password = request.form.get("password")
        errors = check_password(password)
        strength, color, percentage = password_strength(password)

        if len(errors) == 0:
            result = "✅ Valid Password"
        else:
            result = "❌ Password does not meet requirements"
    return render_template("index.html",result=result,errors=errors,strength=strength,
    color=color,
    percentage=percentage)

if __name__ == "__main__":
    app.run(debug=True)

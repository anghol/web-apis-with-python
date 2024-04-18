from flask import Flask, jsonify, request, render_template

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if not fname and not lname:
        response = jsonify({"status": "error"})
    elif fname and not lname:
        response = jsonify({"data": f"Hello, {fname}!"})
    elif lname and not fname:
        response = jsonify({"data": f"Hello, Mr. {lname}!"})
    else:
        response = jsonify({"data": f"Is your name {fname} {lname}?"})
    return response
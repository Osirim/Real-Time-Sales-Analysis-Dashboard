from flask import Flask, request, jsonify
from upload_to_mysql import upload_sale

app = Flask(__name__)

@app.route("/add_sale", methods=["POST"])
def add_sale():

    data = request.json

    upload_sale(data)

    return jsonify({
        "message":"Sale added successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)
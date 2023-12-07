from flask import Flask, jsonify

app = Flask(__name__)

def logme(func):
    def wrapper():
        print("we received call")
        return func()

    return wrapper

@app.route('/', methods=["GET"])
@logme
def getstring():
    return '{\
        "Name": "Pravin",\
        "Subjects": {\
            "Maths",\
            "English",\
            "Computer Science",\
            "Graphics"\
        }\
    }'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
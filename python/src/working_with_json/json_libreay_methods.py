import json

data = {
    "name": "john",
    "age": 99,
    "nicknames": ["johny", "jj", "bob", "j"],
    "kids":[
        {
            "name" : "Sara",
            "age" : 55
        },
        {
            "name" : "jr. john",
            "age": 50
        }
    ],
    "address": "SFO, USA"
}

print(type (data))

jdata = json.dumps(data)

print(jdata, type(jdata))

jdata_loads = json.loads(jdata)

print(jdata_loads, type(jdata_loads))

with open("json_data.txt", 'w') as write_file:
    json.dump(jdata_loads, write_file, indent=4)

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST"])
def root():
    data = request.data
    print(json.loads(data), "\n", type(data))
    print("base-url is ----> ", request.base_url)
    print("--------> ", request.content_type, request.content_length, request.content_md5)
    print(request.headers)
    print("request.cookies ---> ", request.cookies)
    print("request.endpoint ----> ",request.endpoint)

    return json.loads(data)

import requests

@app.route('/api/v1/todos', methods=["GET"])
def getTodos():

    taskNumber = request.args.get("task")
    for k,v in request.args.items():
        print(f"key : {k} and val : {v}")

    if not taskNumber.isdecimal():
        return {
            "error": "task should be numeric e.g. task=1",
            "code": 500
        }, 500

    print("taskNumber.....",taskNumber)

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "fromMyPC"
    }

    response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{taskNumber}', headers=headers, verify=False)

    return json.loads(response.text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5432)

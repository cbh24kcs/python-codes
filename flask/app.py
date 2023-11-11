from flask import Flask

app = Flask(__name__)


@app.get("/hello")
def hello():
    return "你好"



app.run(port=8080)

import time
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/blocking")
def blocking():
    start_time = time.time()
    time.sleep(5)
    end_time = time.time()
    duration = end_time - start_time
    return {
        "start_time": datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration,
    }
